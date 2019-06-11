from base import base_model
import tensorflow as tf


class ExampleModel(base_model.BaseModel):
    def __init__(self, config):
        self.config = config

        # define model inputs, such as X,Y placeholders
        super(ExampleModel, self).__init__(config,)

    def build_model(self):
        pass

    def compute_loss(self):
        pass

    def compute_metric(self):
        pass
