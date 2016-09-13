import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Set matplotlib rc params
rc = {'lines.linewidth' : 2, 'axes.labelsize' : 18, 'axes.titlesize' : 18}
sns.set(rc=rc)

# Load the food data.
xa_high = np.loadtxt('data/xa_high_food.csv', comments='#')
xa_low = np.loadtxt('data/xa_low_food.csv', comments='#')

# Make the bin boundaries.
bins = np.arange(1700, 2500, 50)

# Plot data as a histogram.
_= plt.hist(xa_low, bins=bins)
plt.xlabel('Cross-sectional area(µm$^2$)')
plt.ylabel('Count')
plt.show()
