import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

M = 10000
N = 52 * 5
betaHat = np.empty(M)
Rsqrd = np.empty(M)

for i in range(M):
    y = np.cumsum(np.random.normal(size=N))
    x = np.cumsum(np.random.normal(size=N))
    reg = stats.linregress(x,y)
    betaHat[i] = reg.slope
    Rsqrd[i] = reg.rvalue ** 2

plt.hist(betaHat, bins=100);
plt.title('Sampling Distribution of Beta')
plt.xlabel("Value")
plt.ylabel("Frequency")
plt.savefig("images/Spurious-Beta-Histogram.png")
plt.clf()

plt.hist(Rsqrd, bins=100);
plt.title('Sampling Distribution of R-Squared')
plt.xlabel("Value")
plt.ylabel("Frequency")
plt.savefig("images/Spurious-Rsqrd-Histogram.png")
