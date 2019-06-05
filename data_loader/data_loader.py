from data_loader import mnist


class DataLoaderHelper:

    @staticmethod
    def load_dataset(config):
        if config.dataset_name == 'mnist':
            return mnist.MNIST(config)
        else:
            raise ValueError("Unknown dataset name")
