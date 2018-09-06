import pandas as pd 

train_df = pd.read_csv('train.csv') 
test_df = pd.read_csv('test.csv')
combine = train_df.append(test_df) 

combine.columns[combine.isnull().any()].tolist()

"""
OUTPUT:
['Age', 'Cabin', 'Embarked', 'Fare', 'Survived']
"""
