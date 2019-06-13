from base import base_runner


class ExampleRunner(base_runner.BaseRunner):

    def __init__(self, model, dataset, config):
        super(ExampleRunner, self).__init__(model, dataset, config)

    def train(self):
        for epoch in range(self.config.num_epochs + 1):
            if epoch % self.config.evaluate_steps == 0:
                self.evaluate(self.dataset.test)
            if epoch % self.config.save_steps == 0:
                self.model.save(self.sess, self.model.global_step)
            self.dataset.train.init()
            while not self.dataset.train.is_finished:
                self.train_step(epoch)

    def evaluate(self, subset):
        batch_size = self.config.test_batch_size
        global_step = self.model.global_step.eval(self.sess)
        pos = 0
        accs, losses = [], []
        while pos + batch_size < len(subset):
            batch_x = subset.X[pos:pos + batch_size]
            batch_y = subset.Y[pos:pos + batch_size]
            batch_x = batch_x.reshape([-1] + (self.model.X.get_shape().as_list()[1:]))
            pos += batch_size
            feed_dict = {self.model.X: batch_x, self.model.Y: batch_y}
            acc, loss = self.sess.run([self.model.accuracy, self.model.loss], feed_dict)
            accs.append(acc)
            losses.append(loss)
        print("Test Acc {:.3f} Loss {:.3f}".format(sum(accs) / len(accs), sum(losses) / len(losses)))
        summaries_dict = {
            'acc': sum(accs) / len(accs),
            'loss': sum(losses) / len(losses),
        }
        self.logger.summarize(global_step, summaries_dict=summaries_dict, summarizer='test')

    def train_step(self, epoch):
        batch_x, batch_y = self.dataset.train.next_batch(self.config.batch_size)
        batch_x = batch_x.reshape([-1] + (self.model.X.get_shape().as_list()[1:]))
        tensors = [self.model.train_op, self.model.loss, self.model.accuracy]
        feed_dict = {self.model.X: batch_x, self.model.Y: batch_y}
        _, loss, acc = self.sess.run(tensors, feed_dict)
        step = self.model.global_step.eval(self.sess)
        if step % self.config.display_steps == 0 or step == 1:
            print("Epoch {} Step {} Loss {:.3f} Train Acc {:.3f}".format(epoch, step, loss, acc))
            summaries_dict = {
                'loss': loss,
                'acc': acc,
            }
            self.logger.summarize(step, summaries_dict=summaries_dict, summarizer='train')
