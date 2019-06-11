from base import base_model
import tensorflow as tf


class Model(base_model.BaseModel):
    def __init__(self, config):
        self.config = config
        self.X = tf.placeholder(tf.float32, shape=[None, 28, 28], name='X')
        self.Y = tf.placeholder(tf.int32, shape=[None], name='Y')
        self.keep_prob = tf.placeholder(tf.float32, shape=[], name='keep_prob')
        super(Model, self).__init__(config)

    def build_model(self):
        X = self.X
        X = tf.expand_dims(X, axis=3)

        net = tf.layers.conv2d(X, 32, [5, 5], padding='same')
        net = tf.layers.max_pooling2d(net, [2, 2], [2, 2], padding='same')

        net = tf.layers.conv2d(net, 64, [5, 5], padding='same')
        net = tf.layers.max_pooling2d(net, [2, 2], [2, 2], padding='same')

        net = tf.reshape(net, [-1, 7 * 7 * 64])
        net = tf.layers.dense(net, self.config.n_units)
        logits = tf.layers.dense(net, self.config.n_classes)
        return logits
