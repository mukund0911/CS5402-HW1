import pandas as pd 

train_df = pd.read_csv('train.csv') 
test_df = pd.read_csv('test.csv')
combine = train_df.append(test_df) 

combine.describe(include=['O'])

"""
OUTPUT:
Cabin Embarked                  Name   Sex    Ticket
count           295     1307                  1309  1309      1309
unique          186        3                  1307     2       929
top     C23 C25 C27        S  Connolly, Miss. Kate  male  CA. 2343
freq              6      914                     2   843        11
"""
