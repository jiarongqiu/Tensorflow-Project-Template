import random
import numpy as np


class BaseDataSet(object):
    def __init__(self, X, Y, shuffle=True):
        self.X = np.array(X)
        self.Y = np.array(Y)
        self._pos = 0
        self.shuffle = shuffle
        self.is_finished = False

    def __len__(self):
        return len(self.X)

    def __getitem__(self, idx):
        return self.X[idx], self.Y[idx]

    def _data_shuffle(self):
        ids = list(range(len(self.X)))
        random.shuffle(ids)
        self.X = self.X[ids]
        self.Y = self.Y[ids]

    def init(self):
        if self.shuffle:
            self._data_shuffle()
        self._pos = 0
        self.is_finished = False

    def next_batch(self, batch_size):
        """Return the next `batch_size` examples from this data set."""
        pos = self._pos
        batch_x = self.X[pos:pos + batch_size]
        batch_y = self.Y[pos:pos + batch_size]
        self._pos = pos + batch_size
        if self._pos + batch_size >= len(self.X):
            self.is_finished = True

        return batch_x, batch_y
