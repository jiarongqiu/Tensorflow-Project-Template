from configs import example


class ConfigsHelper:

    @staticmethod
    def process_config(config):
        if config == 'example':
            return example.ExampleConfig()
        else:
            raise ValueError("Unknown config name")
