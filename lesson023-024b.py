import numpy as np
import scipy.special
import matplotlib.pyplot as plt
import seaborn as sns
rc = {'lines.linewidth' : 2, 'axes.labelsize' : 18, 'axes.titlesize' : 18}
sns.set(rc=rc)

def ecdf(data):
    """
    Coputer x, y values for an empirical distribution function
    """

    x = np.sort(data)
    y = np.arange(1, 1+len(x)) / len(x)

    return x, y

#Load data
xa_high = np.loadtxt('data/xa_high_food.csv', comments='#')
xa_low = np.loadtxt('data/xa_low_food.csv', comments='#')

x_high, y_high = ecdf(xa_high)
x_low, y_low = ecdf(xa_low)

plt.plot(x_high, y_high, marker='.', linestyle='none', markersize='20', alpha=0.5)
plt.plot(x_low, y_low, marker='.', linestyle='none', markersize='20', alpha=0.5)
plt.xlabel('Cross-sectional area (um)')
plt.ylabel('eCDF')
plt.legend(('x high', 'x low'), loc='upper right')
plt.show()
