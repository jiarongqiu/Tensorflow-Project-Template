import os
from utils import utils


class BaseConfig(object):
    save_steps = 5  # save freq
    max_to_keep = 5  # models to keep
    display_steps = 100  # display freq
    evaluate_steps = 5  # evaluate freq

    # Default hyper-parameters, usually need fine-tuning
    max_grad_norm = 5  # gradients clip
    regularization_weight = 1e-7
    learning_rate = 3e-4
    keep_rate = 0.5

    def __init__(self, exp_name, exp_dir, dataset, is_training=False):
        """
        exp_name: name of the experiment
        exp_dir: path of the experiment, shall store logs and models
        dataset: name of the dataset
        is_training: training or testing
        log_dir: exp_dir/datasets/log/[exp_name], easy for tensorboard to visualize
        """
        self.log_dir = os.path.join(exp_dir, dataset, "logs", exp_name)
        self.save_path = os.path.join(exp_dir, dataset, exp_name, exp_name)
        self.model_dir = os.path.join(exp_dir, dataset, exp_name)
        print("Model save path {}\n "
              "model dir {}\n "
              "log dir {}\n".format(self.save_path, self.model_dir, self.log_dir))

        if is_training:
            utils.rm_and_create_dir(self.model_dir)
            utils.rm_and_create_dir(self.log_dir)
