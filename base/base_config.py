import os
from utils import utils


class BaseConfig(object):
    remove_and_create = True
    save_steps = 5
    max_to_keep = 5

    def __init__(self, exp_name, exp_dir, dataset_name):
        self.log_dir = os.path.join(exp_dir, dataset_name, exp_name, "log")
        self.save_path = os.path.join(exp_dir, dataset_name, exp_name, exp_name)
        self.checkpoint_dir = os.path.join(exp_dir, dataset_name, exp_name)
        print("Model save path {}\n "
              "checkpoint dir {}\n "
              "log dir {}\n".format(self.save_path, self.checkpoint_dir, self.log_dir))

        if self.remove_and_create:
            utils.rm_and_create_dir(self.checkpoint_dir)
            utils.create_dir(self.log_dir)
            print("Remove and create {}\n {}".format(self.log_dir,self.checkpoint_dir))
