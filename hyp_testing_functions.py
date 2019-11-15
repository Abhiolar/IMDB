import pandas as pd 
import numpy as np 
import scipy.stats as stats

""" This function get's the pooled variance of 2 samples in order 
to input it for the T-test"""

def pooled_variance(sample1, sample2):
    n1 = len(sample1)
    n2 = len(sample2)
    var1 = np.var(sample1)
    var2 = np.var(sample2)
    num = (n1-1)*var1 + (n2-1)*var2
    den = n1 + n2 - 2
    return num/den


""" T-test function"""
def tstatistic(fifth, now):
    fifth_mean, now_mean = np.mean(fifth), np.mean(now)
    pool_var = pooled_variance(fifth, now)
    n_f, n_n = len(fifth), len(now)
    num = fifth_mean - now_mean
    denom = np.sqrt(pool_var * ((1/n_f)+(1/n_n)))
    return num / denom

"""Welch T-test function"""

def welch_t(a, b):
    
    numerator = np.mean(a) - np.mean(b)
    
    # “ddof = Delta Degrees of Freedom”: the divisor used in the calculation is N - ddof, 
    #  where N represents the number of elements. By default ddof is zero.
    
    denominator = np.sqrt(np.var(a, ddof=1)/np.array(a).size + np.var(b, ddof=1)/np.array(b).size)
    
    return np.abs(numerator/denominator)


"""Getting distribution of means for n samples"""

def samples_means(array, samples_wanted):
    sample_means = []
    for i in range(samples_wanted):
        sample_means.append(np.mean(random.sample(list(array), 30)))
    return sample_means

""" Degrees of freedom for Welch test for two samples"""
def welch_df(a, b):
    
    s1 = np.var(a, ddof=1) 
    s2 = np.var(b, ddof=1)
    n1 = len(a)
    n2 = len(b)
    
    numerator = (s1/n1 + s2/n2)**2
    denominator = (s1/ n1)**2/(n1 - 1) + (s2/ n2)**2/(n2 - 1)
    
    return numerator/denominator


""" Get p-value for one or two sided test"""

def p_value_(a, b, two_sided=False):

    t = welch_t(a, b)
    df = welch_df(a, b)
    
    p = 1-stats.t.cdf(np.abs(t), df)
    
    if two_sided:
        return 2*p
    else:
        return p



