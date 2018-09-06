import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sb

train_df = pd.read_csv('train.csv') 
test_df = pd.read_csv('test.csv')
combine = train_df.append(test_df) 

g = sb.FacetGrid(combine, col = "Survived")
g.map(plt.hist, "Age")
plt.show()
