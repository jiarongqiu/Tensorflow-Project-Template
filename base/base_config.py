import os
from utils import utils


class BaseConfig(object):
    remove_and_create = True    # remove and create dir every time
    save_steps = 5              # save freq
    max_to_keep = 5             # models to keep
    display_steps = 100         # display freq
    evaluate_steps = 5          # evaluate freq
    max_grad_norm = 5           # grad clip
    learning_rate = 3e-4        # default learning rate

    def __init__(self, exp_name, exp_dir, dataset):
        self.log_dir = os.path.join(exp_dir, dataset, exp_name, "log")
        self.save_path = os.path.join(exp_dir, dataset, exp_name, exp_name)
        self.model_dir = os.path.join(exp_dir, dataset, exp_name)
        print("Model save path {}\n "
              "model dir {}\n "
              "log dir {}\n".format(self.save_path, self.model_dir, self.log_dir))

        if self.remove_and_create:
            utils.rm_and_create_dir(self.model_dir)
            utils.create_dir(self.log_dir)
            print("Remove and create {}\n {}".format(self.log_dir, self.model_dir))
