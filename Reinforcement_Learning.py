import numpy as np

# Environment setup (simple grid world)
num_states = 10
num_actions = 2
q_table = np.zeros((num_states, num_actions))

# Hyperparameters
alpha = 0.1  # Learning rate
gamma = 0.6  # Discount factor
epsilon = 0.1  # Exploration-exploitation tradeoff

# Example of a reward function
def reward(state, action):
    if state == 9 and action == 1:
        return 100  # Reward for reaching the goal
    return -1  # Penalty for each step taken

# Q-learning algorithm
for episode in range(1000):
    state = np.random.randint(0, num_states)  # Start in a random state
    done = False

    while not done:
        if np.random.uniform(0, 1) < epsilon:
            action = np.random.randint(0, num_actions)  # Explore
        else:
            action = np.argmax(q_table[state])  # Exploit known Q-values
        
        next_state = (state + action) % num_states  # Example transition
        reward_value = reward(state, action)
        
        # Update Q-value
        q_table[state, action] = q_table[state, action] + alpha * (
            reward_value + gamma * np.max(q_table[next_state]) - q_table[state, action])
        
        state = next_state
        if state == 9:
            done = True  # Goal state reached

# Display learned Q-values
print(q_table)
