import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sb

train_df = pd.read_csv('train.csv') 
test_df = pd.read_csv('test.csv')
combine = train_df.append(test_df)

for i,fare in enumerate(combine.Fare):                            #Converting the Fare feature to ordinal values based on the FareBand.
    if fare <= 7.91: combine.Fare[i] = 0
    elif fare > 7.91 and fare <= 14.454: combine.Fare[i] = 1
    elif fare > 14.454 and fare <= 31: combine.Fare[i] = 2
    elif fare > 31: combine.Fare[i] = 3
