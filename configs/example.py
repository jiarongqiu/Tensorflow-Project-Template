import os
from base import base_config


class ExampleConfig(base_config.BaseConfig):
    # Base configuration
    exp_name = "mnist_rnn"
    dataset = "mnist"
    exp_dir = "D:/models/"
    data_dir = "D:/data/mnist"

    # Training configuration
    num_epochs = 50
    learning_rate = 1e-4
    batch_size = 32
    test_batch_size = 64

    # Model configuration
    model = "rnn"
    n_timesteps = 28
    n_inputs = 28
    n_units = 64
    n_classes = 10

    def __init__(self):
        super(ExampleConfig, self).__init__(self.exp_name, self.dataset, self.exp_dir)
