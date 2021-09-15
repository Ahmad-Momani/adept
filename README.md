# Mujoco Environments
`Adept` is a collection of environments/tasks simulated with the [Mujoco](http://www.mujoco.org/) physics engine and wrapped in the OpenAI `gym` API.

## Getting Started
`Adept` uses git submodules to resolve dependencies. Please follow steps exactly as below to install correctly.

1. Clone this repo with pre-populated submodule dependencies
```
$ git clone --recursive https://github.com/vikashplus/adept.git
```
2. Update submodules
```
$ cd adept
$ git submodule update --remote
```
3. Install package using `pip`
```
$ pip install -e .
```
**OR**
Add repo to pythonpath by updating `~/.bashrc` or `~/.bash_profile`
```
export PYTHONPATH="<path/to/adept>:$PYTHONPATH"
```
4. You can visualize the environments with random controls using the below command
```
$ python utils/visualize_env.py --env_name ElbowPose1D1MRandom-v0
```
**NOTE:** If the visualization results in a GLFW error, this is because `mujoco-py` does not see some graphics drivers correctly. This can usually be fixed by explicitly loading the correct drivers before running the python script. See [this page](https://github.com/aravindr93/mjrl/tree/master/setup#known-issues) for details.