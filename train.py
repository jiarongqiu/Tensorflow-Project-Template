from utils import utils
from configs import configs
from data_loader import data_loader
from models import models
from trainers import example_runner

args = utils.get_args()
config = configs.ConfigsHelper.process_config(args.config)

dataset = data_loader.DataLoaderHelper.load_dataset(config)
model = models.ModelsHelper.load_model(config)

runner = example_runner.ExampleRunner(model,dataset,config)
runner.train()

