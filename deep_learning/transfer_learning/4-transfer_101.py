#!/usr/bin/env python3
"""Train a Caltech-101 image classifier using transfer learning."""

import tensorflow as tf
from tensorflow import keras


def train_transfer_model():
    """Train, fine-tune, save, and return a Caltech-101 classifier."""
    data_dir = "101_ObjectCategories"
    image_size = (224, 224)
    batch_size = 32
    seed = 42

    train_ds = keras.utils.image_dataset_from_directory(
        data_dir,
        validation_split=0.2,
        subset="training",
        seed=seed,
        image_size=image_size,
        batch_size=batch_size,
        label_mode="int",
    )

    val_ds = keras.utils.image_dataset_from_directory(
        data_dir,
        validation_split=0.2,
        subset="validation",
        seed=seed,
        image_size=image_size,
        batch_size=batch_size,
        label_mode="int",
    )

    num_classes = len(train_ds.class_names)

    train_ds = train_ds.prefetch(tf.data.AUTOTUNE)
    val_ds = val_ds.prefetch(tf.data.AUTOTUNE)

    data_augmentation = keras.Sequential([
        keras.layers.RandomFlip(
            "horizontal",
            seed=seed
        ),
        keras.layers.RandomRotation(
            0.05,
            seed=seed
        ),
        keras.layers.RandomZoom(
            0.1,
            seed=seed
        ),
        keras.layers.RandomContrast(
            0.1,
            seed=seed
        ),
    ])

    base_model = keras.applications.EfficientNetB0(
        weights="imagenet",
        include_top=False,
        input_shape=(224, 224, 3),
    )

    base_model.trainable = False

    inputs = keras.Input(shape=(224, 224, 3))

    x = data_augmentation(inputs)
    x = keras.applications.efficientnet.preprocess_input(x)

    x = base_model(
        x,
        training=False
    )

    x = keras.layers.GlobalAveragePooling2D()(x)
    x = keras.layers.Dropout(0.3)(x)

    outputs = keras.layers.Dense(
        num_classes,
        activation="softmax"
    )(x)

    model = keras.Model(
        inputs=inputs,
        outputs=outputs
    )

    checkpoint = keras.callbacks.ModelCheckpoint(
        "caltech101_model.h5",
        monitor="val_accuracy",
        save_best_only=True,
        mode="max",
        verbose=1,
    )

    early_stopping = keras.callbacks.EarlyStopping(
        monitor="val_accuracy",
        patience=4,
        mode="max",
        restore_best_weights=True,
    )

    reduce_lr = keras.callbacks.ReduceLROnPlateau(
        monitor="val_loss",
        factor=0.2,
        patience=2,
        min_lr=1e-7,
        verbose=1,
    )

    model.compile(
        optimizer=keras.optimizers.Adam(
            learning_rate=1e-3
        ),
        loss="sparse_categorical_crossentropy",
        metrics=["accuracy"],
    )

    print("\nPhase 1: Training classification head\n")

    model.fit(
        train_ds,
        validation_data=val_ds,
        epochs=12,
        callbacks=[
            checkpoint,
            early_stopping,
            reduce_lr,
        ],
    )

    print("\nPhase 2: Fine-tuning EfficientNetB0\n")

    base_model.trainable = True

    fine_tune_at = len(base_model.layers) - 30

    for layer in base_model.layers[:fine_tune_at]:
        layer.trainable = False

    for layer in base_model.layers[fine_tune_at:]:
        if isinstance(layer, keras.layers.BatchNormalization):
            layer.trainable = False
        else:
            layer.trainable = True

    model.compile(
        optimizer=keras.optimizers.Adam(
            learning_rate=1e-5
        ),
        loss="sparse_categorical_crossentropy",
        metrics=["accuracy"],
    )

    model.fit(
        train_ds,
        validation_data=val_ds,
        epochs=15,
        callbacks=[
            checkpoint,
            early_stopping,
            reduce_lr,
        ],
    )

    best_model = keras.models.load_model(
        "caltech101_model.h5"
    )

    loss, accuracy = best_model.evaluate(
        val_ds,
        verbose=1
    )

    print(
        "\nFinal validation accuracy: "
        f"{accuracy * 100:.2f}%"
    )

    return best_model


if __name__ == "__main__":
    train_transfer_model()
