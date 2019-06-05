# Tensorflow Project Template
This repo is forked from [Tensorflow-Project-Template](https://github.com/MrGemy95/Tensorflow-Project-Template).
Based on their setting, I add the following features:

#### Built-in Configuration rather than JSON file
This is to reuse variables. For example, the exp_name could be used in 
constructing model_dir, save_path, model_name or anything. It is inconvenient and obvious to define 
these in the code. But, JSON file can not support this kind of reference. 

Note that we could also use shell to achieve this.

Please inherit base/base_config.py to build configuration file.

#### TODO
-[x] Base config
-[x] Base dataset
-[x] Base model
-[x] Base runner
-[x] A toy example 
-[ ] Doc