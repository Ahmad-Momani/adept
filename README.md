# Mujoco Environments
`Adept` is a collection of environments/tasks simulated with the [Mujoco](http://www.mujoco.org/) physics engine and wrapped in the OpenAI `gym` API.

## Getting Started
`Adept` uses git submodules to resolve dependencies. Please follow steps exactly as below to install correctly.

1. The main package dependencies are `MuJoCo`, `python=3.7`, `gym>=0.13`, `mujoco-py>=2.0`, and `pytorch>=1.0`. See `setup/README.md` ([link](https://github.com/vikashplus/adept/tree/master/setup#installation)) for detailed install instructions.

2. To get started with `Adept`, clone this repo with pre-populated submodule dependencies
```
$ git clone --recursive https://github.com/vikashplus/adept.git
```
3. Update submodules
```
$ cd adept
$ git submodule update --remote
```
4. Install package using `pip`
```
$ pip install -e .
```
**OR**
Add repo to pythonpath by updating `~/.bashrc` or `~/.bash_profile`
```
export PYTHONPATH="<path/to/adept>:$PYTHONPATH"
```
5. You can visualize the environments with random controls using the below command
```
$ python adept/utils/visualize_env.py --env_name ElbowPose1D1MRandom-v0
```
**NOTE:** If the visualization results in a GLFW error, this is because `mujoco-py` does not see some graphics drivers correctly. This can usually be fixed by explicitly loading the correct drivers before running the python script. See [this page](https://github.com/aravindr93/mjrl/tree/master/setup#known-issues) for details.