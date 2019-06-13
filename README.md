# Tensorflow Project Template
This repo is forked from [Tensorflow-Project-Template](https://github.com/MrGemy95/Tensorflow-Project-Template).
Based on their setting, I add the following features:

## Features
#### Base Config
I use built-in Configuration rather than JSON file to record variables. 
For example, the exp_name could be used in constructing model_dir, 
save_path, model_name or anything. It is inconvenient and obvious to define 
these in the code. But, JSON file can not support this kind of reference. 

Note that we could also use shell to achieve this.

#### Base Dataset
I write a container for small dataset that can fit in memory. Simply,
the dataset instance is built with X,y. Then, we can access its data directly 
or call next batch function.

Remember to add the dataset in data_loader.py.

#### Base Model
I already built saver, global step and other repetitous ops used 
during training. Mostly, we need only define X and Y and 
overwrite build_model function

#### Base Runner
I did the things about sess and variables initialization. We only need 
to specific the training process, including logging and so on.
 
## Run
Train a demo mnist example.
```
python -m mains.train -it -c configs.example -m models.example -d datasets.mnist
```
Test
```
python -m mains.test -c configs.example -m models.example -d datasets.mnist
```
Args:
* -it: is training
* -c: config file
* -m: model file
* -d: data file


#### TODO

- [x] Base config
- [x] Base dataset
- [x] Base model
- [x] Base runner
- [x] A toy example 
- [x] Doc
- [ ] Early Stopping Mechanism
- [ ] Large Dataset Loader
