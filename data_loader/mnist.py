from tensorflow.examples.tutorials.mnist import input_data
from base import base_dataset


class MNIST():

    def __init__(self, config):
        dataset = input_data.read_data_sets(config.data_dir, one_hot=False)
        self.train = base_dataset.BaseDataSet(X=dataset.train.images, Y=dataset.train.labels)
        self.test = base_dataset.BaseDataSet(X=dataset.test.images, Y=dataset.test.labels)
