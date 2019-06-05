from utils import logger
import tensorflow as tf


class BaseRunner(object):

    def __init__(self, model, dataset, config):
        self.model = model
        self.dataset = dataset
        self.config = config
        self._sess = self.init_sess()
        self.logger = logger.Logger(self.sess, config)
        self.global_init(self.sess)

    @property
    def sess(self):
        return self._sess

    def evaluate(self, subset):
        raise NotImplementedError

    def train_step(self, epoch):
        raise NotImplementedError

    def init_sess(self):
        config = tf.ConfigProto()
        config.gpu_options.allow_growth = True
        sess = tf.Session(config=config)
        return sess

    def global_init(self, sess):
        sess.run(tf.global_variables_initializer())
