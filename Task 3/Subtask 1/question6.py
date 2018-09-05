import pandas as pd 

train_df = pd.read_csv('train.csv') 
test_df = pd.read_csv('test.csv')
combine = train_df.append(test_df) 

list_datatypes = combine.dtypes
print(list_datatypes)
