from base import base_model
import tensorflow as tf


class ExampleModel(base_model.BaseModel):
    def __init__(self, config):
        self.config = config
        X = tf.placeholder(tf.float32, shape=[None, self.config.n_timesteps, self.config.n_inputs])
        Y = tf.placeholder(tf.int32, shape=[None])
        super(ExampleModel, self).__init__(config, X, Y)

    def build_model(self, X):
        X = tf.unstack(X, self.config.n_timesteps, 1)
        cell = tf.nn.rnn_cell.BasicRNNCell(self.config.n_units, name='RNN')
        outputs, states = tf.nn.static_rnn(cell, X, dtype=tf.float32)
        logits = tf.layers.dense(states, self.config.n_classes)
        return logits
