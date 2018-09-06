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
         
combine.rename(columns={'Sex': 'Gender'})                  #Renaming the column to 'Gender'.

"""
OUTPUT:
0      0
1      1
2      1
3      1
4      0
5      0
6      0
7      0
8      1
9      1
10     1
11     1
12     0
13     0
      ..
401    0
402    1
403    0
404    1
405    0
406    0
407    0
408    0
409    1
410    0
411    0
412    1
413    0
414    0
415    1
416    1
417    1
Name: Gender, Length: 1309, dtype: object
"""
