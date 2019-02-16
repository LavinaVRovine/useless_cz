import numpy as np
import random

x = np.random.normal(3, scale=0.5, size=1000000)

hist, edges = np.histogram(x, 1000, normed=True)

hundred_top = np.sort(hist)[-100:]
sample_score = np.random.choice(hundred_top, 1)
index = np.where(hist == sample_score)
x_loc = edges[index]

sample_score = sample_score - random.uniform(0.001, 0.02)
sample_score_perc = '{:.1%}'.format(sample_score[0])
