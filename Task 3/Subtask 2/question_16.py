import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sb

train_df = pd.read_csv('train.csv') 
test_df = pd.read_csv('test.csv')
combine = train_df.append(test_df)

for i, sex in enumerate(combine.Sex):
     if sex=='male':
         combine.Sex[i]=0
     else:
         combine.Sex[i]=1
         
combine.rename(columns={'Sex': 'Gender'})
