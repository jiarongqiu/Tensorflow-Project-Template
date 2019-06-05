import tensorflow as tf


class BaseModel:
    def __init__(self, config, X, Y):
        self.config = config
        self.X = X
        self.Y = Y
        self.logits = self.build_model(X)

        self.prob = tf.nn.softmax(self.logits)
        self.pred = tf.argmax(self.prob, 1)
        self.accuracy = tf.reduce_mean(tf.cast(tf.equal(tf.cast(self.pred, tf.int32), self.Y),tf.float32))

        loss = tf.losses.sparse_softmax_cross_entropy(logits=self.logits, labels=Y)

        # add regularization loss
        self.loss = loss + sum(tf.get_collection(tf.GraphKeys.REGULARIZATION_LOSSES))
        self.global_step = self.init_global_step()
        self.train_op = self.init_train_op()
        self.saver = self.init_saver()

    def save(self, sess, global_step):
        print("Save model at {}".format(self.config.checkpoint_dir))
        self.saver.save(sess, self.config.checkpoint_dir, global_step)

    def load(self, sess):
        print("Loading model checkpoint from {}".format(self.config.checkpoint_dir))
        latest_checkpoint = tf.train.latest_checkpoint(self.config.checkpoint_dir)
        if latest_checkpoint:
            self.saver.restore(sess, latest_checkpoint)
        else:
            raise ValueError("Checkpoint not find")

    def build_model(self, X):
        raise NotImplementedError

    def init_saver(self):
        return tf.train.Saver(max_to_keep=self.config.max_to_keep)

    def init_global_step(self):
        with tf.variable_scope('global_step'):
            return tf.Variable(0, trainable=False, name='global_step')

    def init_train_op(self):
        if self.config.optimizer == 'adam':
            return tf.train.AdamOptimizer(self.config.learning_rate).minimize(self.loss, global_step=self.global_step)
        else:
            raise ValueError(self.config.optimizer)
