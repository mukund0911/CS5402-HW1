import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sb

train_df = pd.read_csv('train.csv') 
test_df = pd.read_csv('test.csv')
combine = train_df.append(test_df) 

combine[['Survived', 'Pclass']].groupby('Pclass').mean()

"""
OUTPUT:
Survived
Pclass          
1       0.629630
2       0.472826
3       0.242363


AS SIGNIFICANCE OF PCLASS = 1 >0.5, WHICH IS 0.629, IT MUST BE INCLUDED IN THE MODEL.
"""
