Re-implement in Python the results presented in Example 6.6 of the Sutton & Barto book on page 132 
comparing SARSA and Q-learning in the cliff-walking task. Investigate the effect of choosing different values 
for the exploration parameter  for both methods. Present your code and results. In your discussion clearly 
describe the main difference between SARSA and Q-learning in relation to your findings. 
 
Note: For this problem, use α = 0.1 and γ = 1 for both algorithms. The "smoothing" that is mentioned in the 
caption of Figure 6.4 is a result of 1) averaging over 10 runs, and 2) plotting a moving average over the last 
10 episodes.

main.ipynb -- includes results and discussion.
