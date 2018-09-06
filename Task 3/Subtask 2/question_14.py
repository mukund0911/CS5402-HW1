import pandas as pd 

train_df = pd.read_csv('train.csv') 
test_df = pd.read_csv('test.csv')
combine = train_df.append(test_df) 

dupl = combine['Ticket'].duplicated()             #Number of duplicates in column Ticket.
rate = (sum(dupl)/1309)*100                       #Calculating the rate of duplicates.
print(rate)

"""
OUTPUT:
29.02979373567609
"""
