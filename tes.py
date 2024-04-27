import numpy as np
import seaborn as sns
import math
import matplotlib.pyplot as plt

n = 20  # Number of trials (Sample Size)
p = 0.85  # Probability of success on a trial (Success rate)

simulation_count = 100
data = []

for i in range(simulation_count):
    random_numbers = np.random.rand(n)
    x = (random_numbers <= p).sum()
    data.append(x)
    print(random_numbers, x)

sns.set_theme(style="whitegrid", palette="bright")
sns.histplot(data, kde=True, discrete=True)
