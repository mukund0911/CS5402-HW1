import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sb

train_df = pd.read_csv('train.csv') 
test_df = pd.read_csv('test.csv')
combine = train_df.append(test_df) 

mode = combine['Fare'].mode()                                     #Finding the mode of feature, 'Fare'.
combine['Embarked'] = combine['Embarked'].fillna(mode)            #Replacing nan values with mode.
