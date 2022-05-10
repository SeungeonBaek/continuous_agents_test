import wandb


class RLLogger():
    def __init__(self, agent_config, rl_config, summary_writer = None, wandb_session = None):
        self.agent_config = agent_config
        self.rl_config = rl_config
        self.summary_writer = summary_writer
        self.wandb_session = wandb_session

    def step_logging(self, Agent):
        if self.rl_config['tensorboard'] == True:
            self.step_logging_tensorboard(Agent)
        if self.rl_config['wandb'] == True:
            self.step_logging_wandb(Agent)

    def episode_logging(self, Agent, episode_score, episode_step, episode_num, episode_rewards):
        if self.rl_config['tensorboard'] == True:
            self.episode_logging_tensorboard(Agent, episode_score, episode_step, episode_num, episode_rewards)
        if self.rl_config['wandb'] == True:
            self.episode_logging_wandb(Agent, episode_score, episode_step, episode_num, episode_rewards)

    def step_logging_tensorboard(self, Agent):
        if self.agent_config['agent_name'] == 'DDPG':
            if self.agent_config['extension']['name'] == 'TQC':
                updated, actor_loss, critic_loss, trgt_q_mean, critic_value= Agent.update()
            elif self.agent_config['extension']['name'] == 'gSDE':
                updated, actor_loss, critic_loss, trgt_q_mean, critic_value= Agent.update()
            else:
                updated, actor_loss, critic_loss, trgt_q_mean, critic_value= Agent.update()

        elif self.agent_config['agent_name'] == 'TD3':
            if self.agent_config['extension']['name'] == 'TQC':
                updated, actor_loss, critic_loss, trgt_q_mean, critic_1_value, critic_2_value = Agent.update()
            elif self.agent_config['extension']['name'] == 'gSDE':
                updated, actor_loss, critic_loss, trgt_q_mean, critic_1_value, critic_2_value = Agent.update()
            else:
                updated, actor_loss, critic_loss, trgt_q_mean, critic_1_value, critic_2_value = Agent.update()

        elif self.agent_config['agent_name'] == 'SAC':
            if self.agent_config['extension']['name'] == 'TQC':
                updated, actor_loss, critic_loss, trgt_q_mean, critic_value, critic_q_value = Agent.update()
            elif self.agent_config['extension']['name'] == 'gSDE':
                updated, actor_loss, critic_loss, trgt_q_mean, critic_value, critic_q_value = Agent.update()
            else:
                updated, actor_loss, critic_loss, trgt_q_mean, critic_value, critic_q_value = Agent.update()

        if self.agent_config['agent_name'] == 'DDPG':
            if updated:
                self.summary_writer.add_scalar('01_Loss/Critic_loss', critic_loss, Agent.update_step)
                self.summary_writer.add_scalar('01_Loss/Actor_loss', actor_loss, Agent.update_step)
                self.summary_writer.add_scalar('02_Critic/Target_Q_mean', trgt_q_mean, Agent.update_step)
                self.summary_writer.add_scalar('02_Critic/Critic_value', critic_value, Agent.update_step)
        elif self.agent_config['agent_name'] == 'TD3':
            if updated:
                self.summary_writer.add_scalar('01_Loss/Critic_loss', critic_loss, Agent.update_step)
                self.summary_writer.add_scalar('01_Loss/Actor_loss', actor_loss, Agent.update_step)
                self.summary_writer.add_scalar('02_Critic/Target_Q_mean', trgt_q_mean, Agent.update_step)
                self.summary_writer.add_scalar('02_Critic/Critic_1_value', critic_1_value, Agent.update_step)
                self.summary_writer.add_scalar('02_Critic/Critic_2_value', critic_2_value, Agent.update_step)
        elif self.agent_config['agent_name'] == 'SAC':
            if updated:
                self.summary_writer.add_scalar('01_Loss/Critic_1_loss', critic_loss, Agent.update_step)
                self.summary_writer.add_scalar('01_Loss/Actor_loss', actor_loss, Agent.update_step)
                self.summary_writer.add_scalar('02_Critic/Target_Q_mean', trgt_q_mean, Agent.update_step)
                self.summary_writer.add_scalar('02_Critic/Critic_1_value', critic_value, Agent.update_step)

    def step_logging_wandb(self, Agent):
        if self.agent_config['agent_name'] == 'DDPG':
            if self.agent_config['extension']['name'] == 'TQC':
                updated, critic_loss, trgt_q_mean, critic_value= Agent.update()
            elif self.agent_config['extension']['name'] == 'gSDE':
                updated, critic_loss, trgt_q_mean, critic_value= Agent.update()
            else:
                updated, critic_loss, trgt_q_mean, critic_value= Agent.update()

        elif self.agent_config['agent_name'] == 'TD3':
            updated, critic_1_loss, critic_2_loss, trgt_q_mean, critic_1_value, critic_2_value = Agent.update()

        elif self.agent_config['agent_name'] == 'PPO':
            updated, critic_1_loss, critic_2_loss, trgt_q_mean, critic_1_value, critic_2_value = Agent.update()

        elif self.agent_config['agent_name'] == 'SAC':
            updated, critic_1_loss, critic_2_loss, trgt_q_mean, critic_1_value, critic_2_value = Agent.update()

        if self.agent_config['agent_name'] == 'DDPG':
            if updated:
                self.wandb_session.log({
                    "01_Loss/Critic_loss": critic_loss,
                    '02_Critic/Target_Q_mean': trgt_q_mean, 
                    '02_Critic/Critic_value': critic_value
                }, step=self.Agent.update_step)
        elif self.agent_config['agent_name'] == 'TD3':
            if updated:
                self.wandb_session.log({
                    "01_Loss/Critic_loss": critic_loss,
                    '02_Critic/Target_Q_mean': trgt_q_mean, 
                    '02_Critic/Critic_value': critic_value
                }, step=self.Agent.update_step)
        elif self.agent_config['agent_name'] == 'PPO':
            if updated:
                self.wandb_session.log({
                    "01_Loss/Critic_loss": critic_loss,
                    '02_Critic/Target_Q_mean': trgt_q_mean, 
                    '02_Critic/Critic_value': critic_value
                }, step=self.Agent.update_step)
        elif self.agent_config['agent_name'] == 'SAC':
            if updated:
                self.wandb_session.log({
                    "01_Loss/Critic_loss": critic_loss,
                    '02_Critic/Target_Q_mean': trgt_q_mean, 
                    '02_Critic/Critic_value': critic_value
                }, step=self.Agent.update_step)

    def episode_logging_tensorboard(self, Agent, episode_score, episode_step, episode_num, episode_rewards):
        if self.agent_config['agent_name'] == 'PPO':
            if self.agent_config['extension']['name'] == 'MEPPO':
                updated, entropy, ratio, actor_loss, advantage, target_val, critic_value, critic_loss = Agent.update()
            elif self.agent_config['extension']['name'] == 'gSDE':
                updated, entropy, ratio, actor_loss, advantage, target_val, critic_value, critic_loss = Agent.update()
            else:
                updated, entropy, ratio, actor_loss, advantage, target_val, critic_value, critic_loss = Agent.update()

            if updated:
                self.summary_writer.add_scalar('01_Loss/Critic_loss', critic_loss, Agent.update_step)
                self.summary_writer.add_scalar('01_Loss/Actor_loss', actor_loss, Agent.update_step)
                self.summary_writer.add_scalar('02_Critic/Advantage', advantage, Agent.update_step)
                self.summary_writer.add_scalar('02_Critic/Target_value', target_val, Agent.update_step)
                self.summary_writer.add_scalar('02_Critic/Critic_value', critic_value, Agent.update_step)
                self.summary_writer.add_scalar('03_Actor/Entropy', entropy, Agent.update_step)
                self.summary_writer.add_scalar('03_Actor/Ratio', ratio, Agent.update_step)

        self.summary_writer.add_scalar('00_Episode/Score', episode_score, episode_num)
        self.summary_writer.add_scalar('00_Episode/Average_reward', episode_score/episode_step, episode_num)
        self.summary_writer.add_scalar('00_Episode/Steps', episode_step, episode_num)

        self.summary_writer.add_histogram('Reward_histogram', episode_rewards, episode_num)

    def episode_logging_wandb(self, Agent, episode_score, episode_step, episode_num, episode_rewards):
        if self.agent_config['agent_name'] == 'PPO':
            if self.agent_config['extension']['name'] == 'MEPPO':
                updated, entropy, ratio, actor_loss, advantage, target_val, critic_value, critic_loss = Agent.update()
            elif self.agent_config['extension']['name'] == 'gSDE':
                updated, entropy, ratio, actor_loss, advantage, target_val, critic_value, critic_loss = Agent.update()
            else:
                updated, entropy, ratio, actor_loss, advantage, target_val, critic_value, critic_loss = Agent.update()

            if updated:
                self.wandb_session.log({
                    '01_Loss/Critic_loss': critic_loss,
                    '01_Loss/Actor_loss': actor_loss, 
                    '02_Critic/Advantage': advantage,
                    '02_Critic/Target_value': target_val,
                    '02_Critic/Critic_value': critic_value,
                    '03_Actor/Entropy': entropy,
                    '03_Actor/Ratio': ratio
                }, step=self.Agent.update_step)

        self.wandb_session.log({
            '00_Episode/Average_reward': episode_score/episode_step,
            "00_Episode/Score": episode_score,
            '00_Episode/Steps': episode_step,
            "episode_num": episode_num
        })

        histogram = wandb.Histogram(episode_rewards)
        self.wandb_session.log({"reward_hist": histogram})