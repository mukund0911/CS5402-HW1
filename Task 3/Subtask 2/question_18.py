import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sb

train_df = pd.read_csv('train.csv') 
test_df = pd.read_csv('test.csv')
combine = train_df.append(test_df) 

cleanedList = [x for x in combine['Embarked'] if x != 'nan']            #Removing nan values from feature 'Embarked'
max_occurences = max(cleanedList,key=cleanedList.count)                 #Finding the letter with maximum occurences.
combine['Embarked'] = combine['Embarked'].fillna(max_occurences)        #Filling nan values with max_occurences.
