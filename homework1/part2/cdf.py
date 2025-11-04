import numpy as np
import matplotlib.pyplot as plt

v1 = np.loadtxt("ver1_time.txt")
v2 = np.loadtxt("ver2_time.txt")

def cdf(data):
    data_sorted = np.sort(data)
    n = len(data_sorted)
    y = np.arange(1, n+1) / n
    return data_sorted, y

x1, y1 = cdf(v1)
x2, y2 = cdf(v2)

plt.plot(x1, y1, label="ver1")
plt.plot(x2, y2, label="ver2")
plt.xlabel("Execution time (seconds)")
plt.ylabel("CDF")
plt.title("CDF of Execution Times (1000 runs)")
plt.legend()
plt.grid(True)
plt.show()
