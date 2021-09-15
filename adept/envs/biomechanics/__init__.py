from gym.envs.registration import register
import os
import numpy as np


curr_dir = os.path.dirname(os.path.abspath(__file__))

print("RS:> Registering adept-Biomechanics Envs")

# Finger-tip reaching ==============================
register(id='FingerReachMotorFixed-v0',
        entry_point='adept.envs.biomechanics.reach_v0:ReachEnvV0',
        max_episode_steps=200,
        kwargs={
            'model_path': curr_dir+'/assets/finger/tendon_finger_motorAct_v0.mjb',
            'target_reach_range': {'IFtip': ((0.2, 0.05, 0.20), (0.2, 0.05, 0.20)),},
            'normalize_act': True,
            'frame_skip': 5,
        }
    )
register(id='FingerReachMotorRandom-v0',
        entry_point='adept.envs.biomechanics.reach_v0:ReachEnvV0',
        max_episode_steps=200,
        kwargs={
            'model_path': curr_dir+'/assets/finger/tendon_finger_motorAct_v0.mjb',
            'target_reach_range': {'IFtip': ((0.27, .1, .3), (.1, -.1, .1)),},
            'normalize_act': True,
            'frame_skip': 5,
        }
    )
register(id='FingerReachMuscleFixed-v0',
        entry_point='adept.envs.biomechanics.reach_v0:ReachEnvV0',
        max_episode_steps=100,
        kwargs={
            'model_path': curr_dir+'/assets/finger/tendon_finger_muscleAct_v0.mjb',
            'target_reach_range': {'IFtip': ((0.2, 0.05, 0.20), (0.2, 0.05, 0.20)),},
            'normalize_act': True,
        }
    )

register(id='FingerReachMuscleRandom-v0',
        entry_point='adept.envs.biomechanics.reach_v0:ReachEnvV0',
        max_episode_steps=100,
        kwargs={
            'model_path': curr_dir+'/assets/finger/tendon_finger_muscleAct_v0.mjb',
            'target_reach_range': {'IFtip': ((0.27, .1, .3), (.1, -.1, .1)),},
            'normalize_act': True,
        }
    )

# Elbow posing ==============================
register(id='ElbowPose1D1MRandom-v0',
        entry_point='adept.envs.biomechanics.pose_v0:PoseEnvV0',
        max_episode_steps=100,
        kwargs={
            'model_path': curr_dir+'/assets/arm/elbow_1dof1muscle.mjb',
            'target_jnt_range': {'r_elbow_flex':(0, 2.27),},
            'viz_site_targets': ('wrist',),
            'normalize_act': True,
            'pose_thd': .175,
            'reset_type': 'random'
        }
    )
register(id='ElbowPose1D6MRandom-v0',
        entry_point='adept.envs.biomechanics.pose_v0:PoseEnvV0',
        max_episode_steps=100,
        kwargs={
            'model_path': curr_dir+'/assets/arm/elbow_1dof6muscles.mjb',
            'target_jnt_range': {'r_elbow_flex':(0, 2.27),},
            'viz_site_targets': ('wrist',),
            'normalize_act': True,
            'pose_thd': .175,
            'reset_type': 'random'
        }
    )
register(id='ElbowPose1D6MExoRandom-v0',
        entry_point='adept.envs.biomechanics.pose_v0:PoseEnvV0',
        max_episode_steps=100,
        kwargs={
            'model_path': curr_dir+'/assets/arm/elbow_1dof6muscles_1dofexo.mjb',
            'target_jnt_range': {'r_elbow_flex':(0, 2.27),},
            'viz_site_targets': ('wrist',),
            'normalize_act': True,
            'pose_thd': .175,
            'reset_type': 'random',
            'weighted_reward_keys':{
                                "pose": 1.0,
                                "bonus": 4.0,
                                "act_reg": 5.0,
                                "penalty": 50,
            }
        }
    )
register(id='ElbowPose1D6M_SoftExo_Random-v0',
        entry_point='adept.envs.biomechanics.pose_v0:PoseEnvV0',
        max_episode_steps=100,
        kwargs={
            'model_path': curr_dir+'/assets/arm/elbow_1dof6muscles_1dofsoftexo.mjb',
            'target_jnt_range': {'r_elbow_flex':(0, 2.27),},
            'viz_site_targets': ('wrist',),
            'normalize_act': True,
            'pose_thd': .175,
            'reset_type': 'random',
            'weighted_reward_keys':{
                                "pose": 1.0,
                                "bonus": 4.0,
                                "act_reg": 5.0,
                                "penalty": 50,
            }
        }
    )
register(id='ElbowPose1D6MExoRandom_1kg-v0',
        entry_point='adept.envs.biomechanics.pose_v0:PoseEnvV0',
        max_episode_steps=100,
        kwargs={
            'model_path': curr_dir+'/assets/arm/elbow_1dof6muscles_1dofexo_1kg.mjb',
            'target_jnt_range': {'r_elbow_flex':(0, 2.27),},
            'viz_site_targets': ('wrist',),
            'normalize_act': True,
            'pose_thd': .175,
            'reset_type': 'random',
            'weighted_reward_keys':{
                                "pose": 1.0,
                                "bonus": 4.0,
                                "act_reg": 5.0,
                                "penalty": 50,
            }
        }
    )

register(id='ElbowPose1D6MExoRandom_2kg-v0',
        entry_point='adept.envs.biomechanics.pose_v0:PoseEnvV0',
        max_episode_steps=100,
        kwargs={
            'model_path': curr_dir+'/assets/arm/elbow_1dof6muscles_1dofexo_2kg.mjb',
            'target_jnt_range': {'r_elbow_flex':(0, 2.27),},
            'viz_site_targets': ('wrist',),
            'normalize_act': True,
            'pose_thd': .175,
            'reset_type': 'random',
            'weighted_reward_keys':{
                                "pose": 1.0,
                                "bonus": 4.0,
                                "act_reg": 5.0,
                                "penalty": 50,
            }
        }
    )
# Finger-Joint posing ==============================
register(id='FingerPoseMotorFixed-v0',
        entry_point='adept.envs.biomechanics.pose_v0:PoseEnvV0',
        max_episode_steps=200,
        kwargs={
            'model_path': curr_dir+'/assets/finger/tendon_finger_motorAct_v0.mjb',
            'target_jnt_range': {'IFadb':(0, 0),
                                'IFmcp':(0, 0),
                                'IFpip':(.75, .75),
                                'IFdip':(.75, .75)
                                },
            'viz_site_targets': ('IFtip',),
            'normalize_act': True,
            'frame_skip': 5,
        }
)
register(id='FingerPoseMotorRandom-v0',
        entry_point='adept.envs.biomechanics.pose_v0:PoseEnvV0',
        max_episode_steps=200,
        kwargs={
            'model_path': curr_dir+'/assets/finger/tendon_finger_motorAct_v0.mjb',
            'target_jnt_range': {'IFadb':(-.2, .2),
                                'IFmcp':(-.4, 1),
                                'IFpip':(.1, 1),
                                'IFdip':(.1, 1)
                                },
            'viz_site_targets': ('IFtip',),
            'normalize_act': True,
            'frame_skip': 5,
        }
    )
register(id='FingerPoseMuscleFixed-v0',
        entry_point='adept.envs.biomechanics.pose_v0:PoseEnvV0',
        max_episode_steps=100,
        kwargs={
            'model_path': curr_dir+'/assets/finger/tendon_finger_muscleAct_v0.mjb',
            'target_jnt_range': {'IFadb':(0, 0),
                                'IFmcp':(0, 0),
                                'IFpip':(.75, .75),
                                'IFdip':(.75, .75)
                                },
            'viz_site_targets': ('IFtip',),
            'normalize_act': True,
        }
    )
register(id='FingerPoseMuscleRandom-v0',
        entry_point='adept.envs.biomechanics.pose_v0:PoseEnvV0',
        max_episode_steps=100,
        kwargs={
            'model_path': curr_dir+'/assets/finger/tendon_finger_muscleAct_v0.mjb',
            'target_jnt_range': {'IFadb':(-.2, .2),
                                'IFmcp':(-.4, 1),
                                'IFpip':(.1, 1),
                                'IFdip':(.1, 1)
                                },
            'viz_site_targets': ('IFtip',),
            'normalize_act': True,
        }
    )

# Hand-Joint posing ==============================

# Remove this when the ASL envs stablizes
register(id='HandPoseAMuscleFixed-v0',
        entry_point='adept.envs.biomechanics.pose_v0:PoseEnvV0',
        max_episode_steps=100,
        kwargs={
            'model_path': curr_dir+'/assets/hand/2nd_hand_pose.mjb',
            'viz_site_targets': ('THtip','IFtip','MFtip','RFtip','LFtip'),
            'target_jnt_value': np.array([0, 0, 0, -0.0904, 0.0824475, -0.681555, -0.514888, 0, -0.013964, -0.0458132, 0, 0.67553, -0.020944, 0.76979, 0.65982, 0, 0, 0, 0, 0.479155, -0.099484, 0.95831, 0]),
            'normalize_act': True,
            'reset_type': "init",        # none, init, random
            'target_type': 'fixed',      # switch / generate/ fixed
        }
    )

# Create ASL envs ==============================
jnt_namesHand=['pro_sup', 'deviation', 'flexion', 'cmc_abduction', 'cmc_flexion', 'mp_flexion', 'ip_flexion', 'mcp2_flexion', 'mcp2_abduction', 'pm2_flexion', 'md2_flexion', 'mcp3_flexion', 'mcp3_abduction', 'pm3_flexion', 'md3_flexion', 'mcp4_flexion', 'mcp4_abduction', 'pm4_flexion', 'md4_flexion', 'mcp5_flexion', 'mcp5_abduction', 'pm5_flexion', 'md5_flexion']

ASL_qpos={}
ASL_qpos[0]='0 0 0 0.5624 0.28272 -0.75573 -1.309 1.30045 -0.006982 1.45492 0.998897 1.26466 0 1.40604 0.227795 1.07614 -0.020944 1.46103 0.06284 0.83263 -0.14399 1.571 1.38248'.split(' ')
ASL_qpos[1]='0 0 0 0.0248 0.04536 -0.7854 -1.309 0.366605 0.010473 0.269258 0.111722 1.48459 0 1.45318 1.44532 1.44532 -0.204204 1.46103 1.44532 1.48459 -0.2618 1.47674 1.48459'.split(' ')
ASL_qpos[2]='0 0 0 0.0248 0.04536 -0.7854 -1.13447 0.514973 0.010473 0.128305 0.111722 0.510575 0 0.37704 0.117825 1.44532 -0.204204 1.46103 1.44532 1.48459 -0.2618 1.47674 1.48459'.split(' ')
ASL_qpos[3]='0 0 0 0.3384 0.25305 0.01569 -0.0262045 0.645885 0.010473 0.128305 0.111722 0.510575 0 0.37704 0.117825 1.571 -0.036652 1.52387 1.45318 1.40604 -0.068068 1.39033 1.571'.split(' ')
ASL_qpos[4]='0 0 0 0.6392 -0.147495 -0.7854 -1.309 0.637158 0.010473 0.128305 0.111722 0.510575 0 0.37704 0.117825 0.306345 -0.010472 0.400605 0.133535 0.21994 -0.068068 0.274925 0.01571'.split(' ')
ASL_qpos[5]='0 0 0 0.3384 0.25305 0.01569 -0.0262045 0.645885 0.010473 0.128305 0.111722 0.510575 0 0.37704 0.117825 0.306345 -0.010472 0.400605 0.133535 0.21994 -0.068068 0.274925 0.01571'.split(' ')
ASL_qpos[6]='0 0 0 0.6392 -0.147495 -0.7854 -1.309 0.637158 0.010473 0.128305 0.111722 0.510575 0 0.37704 0.117825 0.306345 -0.010472 0.400605 0.133535 1.1861 -0.2618 1.35891 1.48459'.split(' ')
ASL_qpos[7]='0 0 0 0.524 0.01569 -0.7854 -1.309 0.645885 -0.006982 0.128305 0.111722 0.510575 0 0.37704 0.117825 1.28036 -0.115192 1.52387 1.45318 0.432025 -0.068068 0.18852 0.149245'.split(' ')
ASL_qpos[8]='0 0 0 0.428 0.22338 -0.7854 -1.309 0.645885 -0.006982 0.128305 0.194636 1.39033 0 1.08399 0.573415 0.667675 -0.020944 0 0.06284 0.432025 -0.068068 0.18852 0.149245'.split(' ')
ASL_qpos[9]='0 0 0 0.5624 0.28272 -0.75573 -1.309 1.30045 -0.006982 1.45492 0.998897 0.39275 0 0.18852 0.227795 0.667675 -0.020944 0 0.06284 0.432025 -0.068068 0.18852 0.149245'.split(' ')

# ASl Eval envs for each numerals
for k in ASL_qpos.keys():
    register(id='HandPose'+str(k)+'MuscleFixed-v0',
            entry_point='adept.envs.biomechanics.pose_v0:PoseEnvV0',
            max_episode_steps=100,
            kwargs={
                'model_path': curr_dir+'/assets/hand/2nd_hand_pose.mjb',
                'viz_site_targets': ('THtip','IFtip','MFtip','RFtip','LFtip'),
                'target_jnt_value': np.array(ASL_qpos[k],'float'),
                'normalize_act': True,
                'reset_type': "none",        # none, init, random
                'target_type': 'fixed',      # switch / generate/ fixed
            }
    )

# ASL Train Env
m = np.array([ASL_qpos[i] for i in range(10)]).astype(float)
Rpos = {}
for i_n, n  in enumerate(jnt_namesHand):
    Rpos[n]=(np.min(m[:,i_n]), np.max(m[:,i_n]))

register(id='HandPoseMuscleRandom-v0',
        entry_point='adept.envs.biomechanics.pose_v0:PoseEnvV0',
        max_episode_steps=100,
        kwargs={
            'model_path': curr_dir+'/assets/hand/2nd_hand_pose.mjb',
            'viz_site_targets': ('THtip','IFtip','MFtip','RFtip','LFtip'),
            'target_jnt_range': Rpos,
            'normalize_act': True,
            'reset_type': "init",        # none, init, random
            'target_type': 'generate',      # switch / generate/ fixed
        }
    )


# Hand-Joint key turn ==============================
register(id='HandKeyTurnFixed-v0',
        entry_point='adept.envs.biomechanics.key_turn_v0:KeyTurnEnvV0',
        max_episode_steps=200,
        kwargs={
            'model_path': curr_dir+'/assets/hand/2nd_hand_Index_Thumb_keyturn.mjb',
            'normalize_act': True
        }
    )

register(id='HandKeyTurnRandom-v0',
        entry_point='adept.envs.biomechanics.key_turn_v0:KeyTurnEnvV0',
        max_episode_steps=200,
        kwargs={
            'model_path': curr_dir+'/assets/hand/2nd_hand_Index_Thumb_keyturn.mjb',
            'normalize_act': True,
            'key_init_range':(-np.pi/2, np.pi/2)
        }
    )


# Hold objects ==============================
register(id='HandObjHoldFixed-v0',
        entry_point='adept.envs.biomechanics.obj_hold_v0:ObjHoldFixedEnvV0',
        max_episode_steps=75,
        kwargs={
            'model_path': curr_dir+'/assets/hand/2nd_hand_hold.mjb',
            'normalize_act': True
        }
    )

register(id='HandObjHoldRandom-v0',
        entry_point='adept.envs.biomechanics.obj_hold_v0:ObjHoldRandomEnvV0',
        max_episode_steps=75,
        kwargs={
            'model_path': curr_dir+'/assets/hand/2nd_hand_hold.mjb',
            'normalize_act': True
        }
    )


# Pen twirl ==============================
register(id='HandPenTwirlFixed-v0',
            entry_point='adept.envs.biomechanics.pen_v0:PenTwirlFixedEnvV0',
            max_episode_steps=50,
            kwargs={
                'model_path': curr_dir+'/assets/hand/2nd_hand_pen.mjb',
                'normalize_act': True,
                'frame_skip': 5,
            }
    )

register(id='HandPenTwirlRandom-v0',
        entry_point='adept.envs.biomechanics.pen_v0:PenTwirlRandomEnvV0',
        max_episode_steps=50,
        kwargs={
            'model_path': curr_dir+'/assets/hand/2nd_hand_pen.mjb',
            'normalize_act': True,
            'frame_skip': 5,
        }
    )

# Baoding ==============================
register(id='BaodingFixed-v1',
        entry_point='adept.envs.biomechanics.baoding_v1:BaodingFixedEnvV1',
        max_episode_steps=200,
        kwargs={
            'model_path': curr_dir+'/assets/hand/2nd_hand_baoding.mjb',
            'normalize_act': True,
            'reward_option': 0,
        }
    )
register(id='BaodingFixed4th-v1',
        entry_point='adept.envs.biomechanics.baoding_v1:BaodingFixedEnvV1',
        max_episode_steps=200,
        kwargs={
            'model_path': curr_dir+'/assets/hand/2nd_hand_baoding.mjb',
            'normalize_act': True,
            'reward_option':1
        }
    )
register(id='BaodingFixed8th-v1',
        entry_point='adept.envs.biomechanics.baoding_v1:BaodingFixedEnvV1',
        max_episode_steps=200,
        kwargs={
            'model_path': curr_dir+'/assets/hand/2nd_hand_baoding.mjb',
            'normalize_act': True,
            'reward_option': 2,
        }
    )
