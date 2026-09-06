#!/usr/bin/env python3
"""Module for configuring SGD with learning rate schedules."""

from tensorflow import keras


def get_optimizer_SGD_with_schedule(
        schedule_type, initial_lr, decay_steps, decay_rate, momentum):
    """
    Create an SGD optimizer with a learning rate schedule.

    Args:
        schedule_type: Type of schedule, 'exponential' or 'inverse_time'.
        initial_lr: Initial learning rate.
        decay_steps: Number of steps between learning rate decay.
        decay_rate: Rate used to decrease the learning rate.
        momentum: Momentum factor for SGD.

    Returns:
        optimizer: Configured Keras SGD optimizer.
        lr_schedule: Configured learning rate schedule.
    """
    if schedule_type == 'exponential':
        lr_schedule = keras.optimizers.schedules.ExponentialDecay(
            initial_learning_rate=initial_lr,
            decay_steps=decay_steps,
            decay_rate=decay_rate,
            staircase=True
        )

    elif schedule_type == 'inverse_time':
        lr_schedule = keras.optimizers.schedules.InverseTimeDecay(
            initial_learning_rate=initial_lr,
            decay_steps=decay_steps,
            decay_rate=decay_rate,
            staircase=True
        )

    optimizer = keras.optimizers.SGD(
        learning_rate=lr_schedule,
        momentum=momentum
    )

    return optimizer, lr_schedule
