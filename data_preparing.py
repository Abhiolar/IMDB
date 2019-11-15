import pandas as pd 
import numpy as np 

""" Getting decades from years date"""

def get_decade(x):
    if x == 5:
        return '50s'
    elif x == 6:
        return '60s'
    elif x == 7:
        return '70s'
    elif x == 8:
        return '80s'
    elif x == 9:
        return '90s'
    elif x == 0:
        return '00s'
    elif x == 1:
        return '10s'
    
    
"""Get inflation index for years from 2014 to 2019"""
def get_last_years_inflation(x):
    if x == int(2015):
        return 237
    elif x == 2016:
        return 240
    elif x == 2017:
        return 245
    elif x == 2018:
        return 251
    elif x == 2019:
        return 256