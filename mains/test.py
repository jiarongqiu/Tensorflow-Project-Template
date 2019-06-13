from utils import utils
from runners import example_runner

args = utils.get_args()
config = utils.import_module(args.config).Config(args.is_training)
dataset = utils.import_module(args.dataset).Dataset(config)
model = utils.import_module(args.model).Model(config)

runner = example_runner.ExampleRunner(model, dataset, config)
runner.evaluate(dataset.test)
