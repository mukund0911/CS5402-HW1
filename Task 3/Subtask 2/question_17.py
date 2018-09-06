import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sb
from random import *

m = combine['Age'].mean()                       #Calculating mean of feature 'Age'
std = combine['Age'].std()                      #Calculating standard deviation of 'Age'
s = uniform(m, std)                             #Generating random value between mean and std
combine['Age'] = combine['Age'].fillna(s)       #Replacing nan values with random value.
