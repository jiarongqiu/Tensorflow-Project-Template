import tensorflow as tf


class BaseModel:
    def __init__(self, config):
        self.config = config
        with tf.name_scope('model'):
            self.logits = self.build_model()
            with tf.name_scope('metrics'):
                self.compute_loss()
                self.compute_metric()
                self.loss = self.loss + tf.losses.get_regularization_loss()  # add regularization loss

            self.global_step = self.init_global_step()
            with tf.name_scope('optimizer'):
                self.train_op = self.init_train_op(self.loss)
            self.saver = self.init_saver()
            print("Finish building the model")

    def build_model(self):
        raise NotImplementedError

    def compute_loss(self):
        self.loss = tf.losses.sparse_softmax_cross_entropy(logits=self.logits, labels=self.Y)

    def compute_metric(self):
        self.prob = tf.nn.softmax(self.logits)
        self.pred = tf.argmax(self.prob, 1)
        self.accuracy = tf.reduce_mean(tf.cast(tf.equal(tf.cast(self.pred, tf.int32), self.Y), tf.float32))

    def init_train_op(self, loss):
        return tf.train.AdamOptimizer(self.config.learning_rate).minimize(loss, global_step=self.global_step)

    def init_global_step(self):
        with tf.variable_scope('global_step'):
            return tf.Variable(0, trainable=False, name='global_step')

    def init_saver(self):
        return tf.train.Saver(max_to_keep=self.config.max_to_keep)

    def save(self, sess, global_step):
        print("Save model at {}".format(self.config.save_path))
        self.saver.save(sess, self.config.save_path, global_step)

    def load(self, sess):
        print("Loading model checkpoint from {}".format(self.config.model_dir))
        latest_checkpoint = tf.train.latest_checkpoint(self.config.model_dir)
        if latest_checkpoint:
            self.saver.restore(sess, latest_checkpoint)
        else:
            raise ValueError("Checkpoint not find")
