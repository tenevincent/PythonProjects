

from matplotlib import pyplot as plt
import numpy as np
import math #needed for definition of pi
x = np.arange(0, math.pi*2, 0.05)
y = np.sin(x)
plt.style.use("seaborn")
plt.grid(color='g',linestyle='-',linewidth=1)
plt.plot(x,y, marker="*", color='r')
plt.xlabel("angle")
plt.ylabel("sine")
plt.title('sine wave')
plt.show()


