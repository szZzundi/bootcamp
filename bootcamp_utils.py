# Bootcamp utils: A collection of statistical functions proved useful to 55 students
import numpy as np
import scipy.special
import matplotlib.pyplot as plt
import seaborn as sns

def ecdf(data):
    """
    Compute x, y values for an empirical distribution function
    """

    x = np.sort(data)
    y = np.arange(1, 1+len(x)) / len(x)

    return x, y
