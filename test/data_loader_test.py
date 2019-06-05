from utils import utils
from configs import configs
from data_loader import data_loader

args = utils.get_args()
config = configs.ConfigsHelper.process_config(args.config)

dataset = data_loader.DataLoaderHelper.load_dataset(config)
print("Training data {} test data {}".format(len(dataset.train), len(dataset.test)))

for i in range(5):
    X, y = dataset.train.next_batch(batch_size=1)
    print(X, y)

