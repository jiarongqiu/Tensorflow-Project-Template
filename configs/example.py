import os
from base import base_config


class Config(base_config.BaseConfig):
    # Base configuration
    exp_name = "mnist_cnn"
    dataset = "mnist"
    exp_dir = "D:/models/"
    data_dir = "D:/data/mnist"

    # Training configuration
    num_epochs = 50
    learning_rate = 1e-4
    batch_size = 32
    test_batch_size = 1

    # Model configuration
    model = "cnn"
    n_units = 64
    n_classes = 10

    def __init__(self, is_training):
        super(Config, self).__init__(self.exp_name, self.exp_dir, self.dataset, is_training)
