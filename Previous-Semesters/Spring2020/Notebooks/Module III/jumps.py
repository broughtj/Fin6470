import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

## main
spot = 41.0
a = 0.09
aj = -0.02
v = 0.30
vj = 0.05
h = 3.0
k = np.exp(aj) - 1.0
tau = 1.0
q = 0.0
M = 3
N = 252

path = np.empty(N)
pathj = np.empty(N)
dt = tau / N 

mudt = (a - q - 0.5 * v * v) * dt
sigmadt = v * np.sqrt(dt)
path[0] = spot
pathj[0] = spot

z1 = np.random.normal(size=N)
z2 = np.random.normal(size=N)

for t in range(1, N):
    m = np.random.poisson(lam=h*dt, size=1)
    w = np.random.normal(size=m)
    path[t] = path[t-1] * np.exp(mudt + sigmadt * z1[t])
    theta1 = (a - q - h * k -0.5 * v * v)* dt + v * np.sqrt(dt) * z1[t]
    theta2 = m * (aj - 0.5 * vj * vj) + vj * np.sum(w)
    pathj[t] = pathj[t-1] * np.exp(theta1) * np.exp(theta2)

df = pd.DataFrame({'GBM' : path, 'Jumps' : pathj})
    
                
