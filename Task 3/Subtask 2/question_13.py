import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sb

train_df = pd.read_csv('train.csv') 
test_df = pd.read_csv('test.csv')
combine = train_df.append(test_df) 

g = sb.FacetGrid(combine, row='Embarked', col='Survived')
g.map(sb.barplot, 'Sex', 'Fare', ci=None)
