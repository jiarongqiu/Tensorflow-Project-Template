import os
from base import base_config


class ExampleConfig(base_config.BaseConfig):
    # Base configuration
    exp_name = "mnist_rnn"
    dataset_name = "mnist"
    exp_dir = "D:/models/"
    data_dir = "D:/data/mnist"

    # Training configuration
    num_epochs = 50
    learning_rate = 1e-4
    batch_size = 32
    test_batch_size = 64
    display_steps = 10
    evaluate_steps = 5
    optimizer = 'adam'

    # Model configuration
    model = "rnn"
    n_timesteps = 28
    n_inputs = 28
    n_units = 64
    n_classes = 10

    def __init__(self):
        super(ExampleConfig, self).__init__(self.exp_name, self.dataset_name, self.exp_dir)
        self.min_max_log_path = os.path.join(self.exp_dir, self.dataset_name, self.exp_name, "min_max_log.json")
