
import matplotlib.pyplot as plt
axis1 = plt.subplot2grid((3, 3), (0, 0), colspan = 2)
axis2 = plt.subplot2grid((3, 3), (0, 2), rowspan = 3)
axis3 = plt.subplot2grid((3, 3), (1, 0), rowspan = 2, colspan = 2)


axis1.grid()
axis2.grid()
axis3.grid()

import numpy as np
x = np.arange(1,10)
axis2.plot(x, x * x)
axis2.set_title('square')
axis1.plot(x, np.exp(x))
axis1.set_title('exp')
axis3.plot(x, np.log(x))
axis3.set_title('log')


plt.tight_layout()

plt.show()