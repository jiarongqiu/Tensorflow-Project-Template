from models import example_model


class ModelsHelper:

    @staticmethod
    def load_model(config):
        if config.model == 'rnn':
            return example_model.ExampleModel(config)
        else:
            raise ValueError("Unknown dataset name")
