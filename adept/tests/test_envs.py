import unittest

import gym
import adept
import numpy as np

class TestEnvs(unittest.TestCase):

    def check_envs(self, module_name, env_names, lite=False, seed=1234):
        print("\nTesting module:: ", module_name)
        for env_name in env_names:
            print("Testing env: ", env_name)
            # test init
            env = gym.make(env_name)
            env.seed(seed)

            # test reset
            env.env.reset()
            # test obs vec
            obs = env.env.get_obs()

            if not lite:
                # test obs dict
                obs_dict = env.env.get_obs_dict(env.env.sim)
                # test rewards
                rwd = env.env.get_reward_dict(obs_dict)

                # test vector => dict upgrade
                # print(env.env.get_obs() - env.env.get_obs_vec())
                # assert (env.env.get_obs() == env.env.get_obs_vec()).all(), "check vectorized computations"

            # test env infos
            infos = env.env.get_env_infos()

            # test step (everything together)
            observation, _reward, done, _info = env.env.step(np.zeros(env.env.sim.model.nu))
            del(env)

    # Biomechanics
    def test_biomechanics(self):
        env_names = [
            'FingerReachMotorFixed-v0', 'FingerReachMotorRandom-v0',
            'FingerReachMuscleFixed-v0', 'FingerReachMuscleRandom-v0',

            'FingerPoseMotorFixed-v0', 'FingerPoseMotorRandom-v0',
            'FingerPoseMuscleFixed-v0', 'FingerPoseMuscleRandom-v0',
            'ElbowPose1D1MRandom-v0', 'ElbowPose1D6MRandom-v0',

            'ElbowPose1D6MExoRandom-v0', 'ElbowPose1D6M_SoftExo_Random-v0',
            'ElbowPose1D6MExoRandom_1kg-v0', 'ElbowPose1D6MExoRandom_2kg-v0',

            'HandKeyTurnFixed-v0', 'HandKeyTurnRandom-v0',

            'HandObjHoldFixed-v0', 'HandObjHoldRandom-v0',

            'HandPenTwirlFixed-v0', 'HandPenTwirlRandom-v0',

            'BaodingFixed-v1', 'BaodingFixed4th-v1', 'BaodingFixed8th-v1',

            'HandPoseAMuscleFixed-v0', 'HandPoseMuscleRandom-v0'
        ]
        for k in range(10): env_names+=['HandPose'+str(k)+'MuscleFixed-v0']

        self.check_envs('Biomechanics', env_names)

if __name__ == '__main__':
    unittest.main()
