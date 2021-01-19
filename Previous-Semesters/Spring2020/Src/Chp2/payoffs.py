import numpy as np
import matplotlib.pyplot as plt

## Basic set-up
S0 = 1000.0
ST = 1050.0
F0 = 1020.0
spot = np.arange(start=0, stop=2000, step=1.0)
longPO = spot - F0
shortPO = F0 - spot


## Long & short forward payoffs
fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
ax.grid()
ax.set_ylabel("Payoff ($)")
ax.set_xlabel("Spot Price at Maturity ($)")
ax.set_title("Long & Short Forward Payoffs")
ax.plot(spot, longPO, 'orange', spot, shortPO, 'purple')
plt.savefig("Long-Short-Forward-Payoffs.png", orientation="landscape")


