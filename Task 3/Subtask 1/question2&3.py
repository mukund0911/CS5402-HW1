import pandas as pd 

train_df = pd.read_csv('train.csv') 
test_df = pd.read_csv('test.csv')
combine = train_df.append(test_df) 

datatypes = dict(combine.dtypes)
categorical_features = []
numerical_features = []

for i in datatypes:
    if datatypes[i] in ['object']:
        categorical_features.append(i)
    elif datatypes[i] in ['int64', 'float64']:
        numerical_features.append(i)
        
print(numerical_features, categorical_features)

"""
OUTPUT:
['Age', 'Fare', 'Parch', 'PassengerId', 'Pclass', 'SibSp', 'Survived'] 
['Cabin', 'Embarked', 'Name', 'Sex', 'Ticket']
"""
