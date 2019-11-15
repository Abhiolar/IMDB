
import pandas as pd 
from matplotlib import pyplot as plt 

    
"""Visualize the critical t values on a t distribution"""
def visualize_t(t_stat, n_control, n_experimental):
    from matplotlib import pyplot as plt 

    fig = plt.figure(figsize=(8,5))
    ax = fig.gca()

    xs = np.linspace(t_stat+1, t_stat+1, 500)

    # use stats.t.ppf to get critical value. For alpha = 0.05 and two tailed test
    crit = stats.t.ppf(1-0.025, (n_control+n_experimental-2))
    
    # use stats.t.pdf to get values on the probability density function for the t-distribution
    
    ys= stats.t.pdf(xs, (n_control+n_experimental-2), 0, 1)
    ax.plot(xs, ys, linewidth=3, color='darkred')

    ax.axvline(crit, color='black', linestyle='--', lw=5)
    ax.axvline(-crit, color='black', linestyle='--', lw=5)
    ax.axvline(t_stat, color='red', linestyle='--', lw=5)
    
    plt.show()
    return None