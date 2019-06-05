from utils import utils
from configs import configs
from models import models

args = utils.get_args()
config = configs.ConfigsHelper.process_config(args.config)

model = models.ModelsHelper.load_model(config)
print(model.logits)
