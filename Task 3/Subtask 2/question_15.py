import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sb

train_df = pd.read_csv('train.csv') 
test_df = pd.read_csv('test.csv')
combine = train_df.append(test_df) 

combine['Cabin'].isnull().sum()         # As 'Cabin' has many number of nan values, it will be dropped.
