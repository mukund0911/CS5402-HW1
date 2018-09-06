import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sb

g = sb.FacetGrid(combine, col = "Survived")
g.map(plt.hist, "Age")
plt.show()
