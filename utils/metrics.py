class Meter(object):

    def __init__(self, max_size=50, smooth=0.9):
        self.records = []
        self.max_size = max_size
        self.smooth = smooth
        self._smooth_value = None

    def put(self, v):
        if len(self.records) >= self.max_size:
            self.records.pop(0)
        self.records.append(v)
        assert len(self.records) <= self.max_size
        if not self._smooth_value:
            self._smooth_value = v
        else:
            self._smooth_value = self.smooth * self._smooth_value + (1 - self.smooth) * v

    @property
    def avg(self):
        return sum(self.records) / len(self.records)

    @property
    def value(self):
        return self.records[-1]

    @property
    def smooth_value(self):
        return self._smooth_value


if __name__ == '__main__':
    acc = Meter()
    acc.put(1)
    acc.put(2)
    acc.put(3)
    print(acc.avg, acc.value, acc.smooth_value)
