from data_loader import mnist


class DataLoaderHelper:

    @staticmethod
    def load_dataset(config):
        if config.dataset == 'mnist':
            return mnist.MNIST(config)
        else:
            raise ValueError("Unknown dataset name")
