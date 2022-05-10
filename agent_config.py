
# DDPG        
DDPG_Vanilla_agent_config = {'agent_name': 'DDPG', 'gamma' : 0.99, 'tau': 0.005, 'update_freq': 2, 'batch_size': 128, 'warm_up': 1024, 
                        'lr_actor': 0.001, 'lr_critic': 0.002, 'buffer_size': 2000000, 'use_PER': True, 'use_ERE': False, 'reward_normalize' : False}
DDPG_Vanilla_agent_config['extension'] = {'name': 'Vanilla', 'gaussian_std': 0.1, 'noise_clip': 0.5, 'noise_reduction_rate': 0.999999}

DDPG_TQC_agent_config = {'agent_name': 'DDPG', 'gamma' : 0.99, 'tau': 0.005, 'update_freq': 2, 'batch_size': 128, 'warm_up': 1024, \
                        'lr_actor': 0.001, 'lr_critic': 0.002, 'buffer_size': 2000000, 'use_PER': True, 'use_ERE': False, 'reward_normalize' : False}
DDPG_TQC_agent_config['extension'] = {'name': 'TQC', 'gaussian_std': 0.1, 'noise_clip': 0.5, 'noise_reduction_rate': 0.999999}

DDPG_gSDE_agent_config = {'agent_name': 'DDPG', 'gamma' : 0.99, 'tau': 0.005, 'update_freq': 2, 'batch_size': 128, 'warm_up': 1024, \
                        'lr_actor': 0.001, 'lr_critic': 0.002, 'buffer_size': 2000000, 'use_PER': True, 'use_ERE': False, 'reward_normalize' : False}
DDPG_gSDE_agent_config['extension'] = {'name': 'gSDE', 'latent_space': 64, 'n_step_reset': 16}

# TD3
TD3_Vanilla_agent_config = {'agent_name': 'TD3', 'gamma' : 0.99, 'tau': 0.005, 'update_freq': 2, 'actor_update_freq': 2, 'batch_size': 128, 'warm_up': 1024, \
                'lr_actor': 0.001, 'lr_critic': 0.002, 'buffer_size': 2000000, 'use_PER': True, 'use_ERE': False, 'reward_normalize' : False}
TD3_Vanilla_agent_config['extension'] = {'name': 'Vanilla', 'gaussian_std': 0.1, 'noise_clip': 0.5, 'noise_reduction_rate': 0.999999}

TD3_TQC_agent_config = {'agent_name': 'TD3', 'gamma' : 0.99, 'tau': 0.005, 'update_freq': 2, 'actor_update_freq': 2, 'batch_size': 128, 'warm_up': 1024, \
                        'lr_actor': 0.001, 'lr_critic': 0.002, 'buffer_size': 2000000, 'use_PER': True, 'use_ERE': False, 'reward_normalize' : False}
TD3_TQC_agent_config['extension'] = {'name': 'TQC', 'gaussian_std': 0.1, 'noise_clip': 0.5, 'noise_reduction_rate': 0.999999}

TD3_gSDE_agent_config = {'agent_name': 'TD3', 'gamma' : 0.99, 'tau': 0.005, 'update_freq': 2, 'actor_update_freq': 2, 'batch_size': 128, 'warm_up': 1024, \
                        'lr_actor': 0.001, 'lr_critic': 0.002, 'buffer_size': 2000000, 'use_PER': True, 'use_ERE': False, 'reward_normalize' : False}
TD3_gSDE_agent_config['extension'] = {'name': 'gSDE', 'latent_space': 64, 'n_step_reset': 16}

# PPO
PPO_Vanilla_agent_config = {'agent_name': 'PPO', 'gamma' : 0.99, 'batch_size': 128, 'epoch_num': 4, 'entropy_coeff': 0.005, 'entropy_reduction_rate': 0.999999, 
		                    'epsilon': 0.2, 'lr_actor': 0.001, 'lr_critic': 0.002, 'buffer_size': 512, 'use_GAE': True, 'lambda': 0.95, 'reward_normalize' : False}
PPO_Vanilla_agent_config['extension'] = {'name': 'Vanilla', 'std_bound': [0.02, 0.3]}

ME_PPO_agent_config = {'agent_name': 'PPO', 'gamma' : 0.99, 'update_freq': 2, 'batch_size': 128, 'epoch_num': 20, 'eps_clip': 0.2, 'eps_reduction_rate': 0.999999, \
                        'lr_actor': 0.001, 'lr_critic': 0.002, 'buffer_size': 2000000, 'use_GAE': True, 'lambda': 0.995, 'reward_normalize' : False}
ME_PPO_agent_config['extension'] = {'name': 'TQC', 'gaussian_std': 0.1, 'noise_clip': 0.5, 'noise_reduction_rate': 0.999999}

PPO_gSDE_agent_config = {'agent_name': 'PPO', 'gamma' : 0.99, 'update_freq': 2, 'batch_size': 128, 'epoch_num': 20, 'eps_clip': 0.2, 'eps_reduction_rate': 0.999999, \
                        'lr_actor': 0.001, 'lr_critic': 0.002, 'buffer_size': 2000000, 'use_GAE': True, 'lambda': 0.995, 'reward_normalize' : False}
PPO_gSDE_agent_config['extension'] = {'name': 'gSDE', 'latent_space': 64, 'n_step_reset': 16}

# SAC
SAC_Vanilla_agent_config = {'agent_name': 'SAC', 'gamma' : 0.99, 'tau': 0.005, 'update_freq': 2, 'actor_update_freq': 2, 'batch_size': 128, 'warm_up': 1024, \
                        'lr_actor': 0.001, 'lr_critic': 0.002, 'buffer_size': 2000000, 'use_PER': True, 'use_ERE': False, 'reward_normalize' : False}
SAC_Vanilla_agent_config['extension'] = {'name': 'Vanilla', 'gaussian_std': 0.1, 'noise_clip': 0.5, 'noise_reduction_rate': 0.999999}

SAC_TQC_agent_config = {'agent_name': 'SAC', 'gamma' : 0.99, 'tau': 0.005, 'update_freq': 2, 'actor_update_freq': 2, 'batch_size': 128, 'warm_up': 1024, \
                        'lr_actor': 0.001, 'lr_critic': 0.002, 'buffer_size': 2000000, 'use_PER': True, 'use_ERE': False, 'reward_normalize' : False}
SAC_TQC_agent_config['extension'] = {'name': 'TQC', 'gaussian_std': 0.1, 'noise_clip': 0.5, 'noise_reduction_rate': 0.999999}

SAC_gSDE_agent_config = {'agent_name': 'SAC', 'gamma' : 0.99, 'tau': 0.005, 'update_freq': 2, 'actor_update_freq': 2, 'batch_size': 128, 'warm_up': 1024, \
                        'lr_actor': 0.001, 'lr_critic': 0.002, 'buffer_size': 2000000, 'use_PER': True, 'use_ERE': False, 'reward_normalize' : False}
SAC_gSDE_agent_config['extension'] = {'name': 'gSDE', 'latent_space': 64, 'n_step_reset': 16}