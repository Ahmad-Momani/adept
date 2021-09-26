# Baselines

## Installation
1. We use [mjrl](https://github.com/aravindr93/mjrl) for our baselines. Please follow mjrl's [install instructions](https://github.com/aravindr93/mjrl/tree/master/setup#installation) before procedding.
2. install hydra `pip install hydra-core --upgrade`
3. install [submitit](https://github.com/facebookincubator/submitit) launcher hydra plugin to launch jobs on cluster/ local `pip install hydra-submitit-launcher --upgrade`


## Launch training
1. Get commands to run
```
./hydra/train_adept_tasks.sh biomechanics          # runs natively
./hydra/train_adept_tasks.sh biomechanics local    # use local launcher
./hydra/train_adept_tasks.sh biomechanics slurm    # use slurm launcher
```
2. Further customize the prompts from the previous step and execute.

