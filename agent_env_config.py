
def env_agent_config(env_switch, agent_switch):
    if env_switch == 1:
        env_config = {'env_name': 'LunarLanderContinuous-v2', 'seed': 777, 'render': False, 'max_step': 500, 'max_episode': 2500}
    elif env_switch == 2: # Todo
        env_config = {'env_name': 'pg-drive', 'seed': 777, 'render': False, 'max_step': 1000, 'max_episode': 501}
    elif env_switch == 3: # Todo
        env_config = {'env_name': 'domestic-env', 'seed': 777, 'render': False, 'max_step': 1000, 'max_episode': 501}
    else:
        raise ValueError('Please try to correct env_switch')

    # DDPG
    if agent_switch == 1:
        from agent_config import DDPG_Vanilla_agent_config
        agent_config = DDPG_Vanilla_agent_config
    elif agent_switch == 2:
        from agent_config import DDPG_TQC_agent_config
        agent_config = DDPG_TQC_agent_config
    elif agent_switch == 3:
        from agent_config import DDPG_gSDE_agent_config
        agent_config = DDPG_gSDE_agent_config

    # TD3
    elif agent_switch == 4:
        from agent_config import TD3_Vanilla_agent_config
        agent_config = TD3_Vanilla_agent_config
    elif agent_switch == 5:
        from agent_config import TD3_TQC_agent_config
        agent_config = TD3_TQC_agent_config
    elif agent_switch == 6:
        from agent_config import TD3_gSDE_agent_config
        agent_config = TD3_gSDE_agent_config

    # PPO
    elif agent_switch == 7:
        from agent_config import PPO_Vanilla_agent_config
        agent_config = PPO_Vanilla_agent_config
    elif agent_switch == 8:
        from agent_config import ME_PPO_agent_config
        agent_config = ME_PPO_agent_config
    elif agent_switch == 9:
        from agent_config import PPO_gSDE_agent_config
        agent_config = PPO_gSDE_agent_config

    # SAC
    elif agent_switch == 10:
        from agent_config import SAC_Vanilla_agent_config
        agent_config = SAC_Vanilla_agent_config
    elif agent_switch == 11:
        from agent_config import SAC_TQC_agent_config
        agent_config = SAC_TQC_agent_config
    elif agent_switch == 12:
        from agent_config import SAC_gSDE_agent_config
        agent_config = SAC_gSDE_agent_config

    else:
        raise ValueError('Please try to correct agent_switch')
    
    return env_config, agent_config