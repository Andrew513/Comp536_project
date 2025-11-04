import numpy as np
import matplotlib.pyplot as plt

def load(path): return np.loadtxt(path)

def cdf(series):
    x = np.sort(series)
    y = np.arange(1, len(x)+1) / len(x)
    return x, y

# Load
v1_user, v1_sys = load("v1_user.txt"), load("v1_sys.txt")
v2_user, v2_sys = load("v2_user.txt"), load("v2_sys.txt")

# CDF: USER TIME
x1, y1 = cdf(v1_user)
x2, y2 = cdf(v2_user)

plt.figure()
plt.plot(x1, y1, label="version1 (fprintf) — user")
plt.plot(x2, y2, label="version2 (write) — user")
plt.xlabel("User (CPU) time [s]")
plt.ylabel("CDF")
plt.title("CDF of User Time (1000 runs)")
plt.grid(True)
plt.legend()
plt.show()

# CDF: SYSTEM TIME
x1s, y1s = cdf(v1_sys)
x2s, y2s = cdf(v2_sys)

plt.figure()
plt.plot(x1s, y1s, label="version1 (fprintf) — sys")
plt.plot(x2s, y2s, label="version2 (write) — sys")
plt.xlabel("System (kernel) time [s]")
plt.ylabel("CDF")
plt.title("CDF of System Time (1000 runs)")
plt.grid(True)
plt.legend()
plt.show()
