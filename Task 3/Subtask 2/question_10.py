import pandas as pd 

train_df = pd.read_csv('train.csv') 
test_df = pd.read_csv('test.csv')
combine = train_df.append(test_df) 

grouped = combine.groupby('Sex')
females = grouped.get_group('female')
males = grouped.get_group('male')

if females['Survived'].sum() > males['Survived'].sum():
    print('Yes, Women are more likely to have survived!')
else:
    print('No')
