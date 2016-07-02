# This script will clean up the test data for the Titanic competition using a 
# similar method to the notebook https://www.kaggle.com/creepykoala/
# titanic/study-of-tree-and-forest-algorithms which I have already applied to 
# the training data

# Import libraries

import numpy as np
from numpy.random import random_integers
import pandas as pd
import matplotlib.pyplot as plt
import sklearn
from sklearn.cross_validation import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier
from scipy.stats import pointbiserialr, spearmanr

# Load the test data
df = pd.read_csv('/home/sophie/projects/Titanic/data/test.csv', header=0)

# People with stronger titles tend to have more help on board. Hence, we will 
# categorize passengers based on titles.
Title_Dictionary = {
                    "Capt":       "Officer",
                    "Col":        "Officer",
                    "Major":      "Officer",
                    "Jonkheer":   "Royalty",
                    "Don":        "Royalty",
                    "Sir" :       "Royalty",
                    "Dr":         "Officer",
                    "Rev":        "Officer",
                    "the Countess":"Royalty",
                    "Dona":       "Royalty",
                    "Mme":        "Mrs",
                    "Mlle":       "Miss",
                    "Ms":         "Mrs",
                    "Mr" :        "Mr",
                    "Mrs" :       "Mrs",
                    "Miss" :      "Miss",
                    "Master" :    "Master",
                    "Lady" :      "Royalty"
                    }
df['Title'] = df['Name'].apply(lambda x: 
Title_Dictionary[x.split(',')[1].split('.')[0].strip()])

# Extract the letters from the beginning of each element of 'Ticket'
def Ticket_Prefix(s):
    s=s.split()[0] # if you don't include anything in split()
    if s.isdigit():
        return 'NoClue'
    else:
        return s
    
df['TicketPrefix'] = df['Ticket'].apply(lambda x: Ticket_Prefix(x))

# Make an array where null values are False.
mask_Age = df.Age.notnull()

# New dataframe where all rows have a value for age. 
Age_Sex_Title_Pclass = df.loc[mask_Age, ["Age", "Title", "Sex", "Pclass"]]

# Groupby object to group by Title, Pclass and Sex
Filler_Ages_1 = Age_Sex_Title_Pclass.groupby(by = ["Title", "Pclass", 
"Sex"]).median()

# This moves both Sex and Pclass into column headers and does so in that order. 
Filler_Ages = Filler_Ages_1.Age.unstack(level = -1).unstack(level = -1)

mask_Age = df.Age.isnull()  # A mask where null values are True

# New DataFrame with missing values for age
Age_Sex_Title_Pclass_missing = df.loc[mask_Age, ["Title", "Sex", "Pclass"]]

# Look-up function for the calculated median ages. 
def Age_filler(row):
    if row.Sex == "female":
        age = Filler_Ages.female.loc[row["Title"], row["Pclass"]]
        return age
    elif row.Sex == "male":
        age = Filler_Ages.male.loc[row["Title"], row["Pclass"]]
        return age
    
# Make a new column on "missing" dataframe and add the median value to each 
# row. 
Age_Sex_Title_Pclass_missing["Age"]=Age_Sex_Title_Pclass_missing.apply(
  Age_filler, axis =1                                                  ) 
          

# reform the 'Age' column.
df["Age"] = pd.concat([Age_Sex_Title_Pclass["Age"], 
Age_Sex_Title_Pclass_missing["Age"]])

# Filling in with the mean of all fares.
df['Fare'] = df['Fare'].fillna(value=df.Fare.mean())

df['FamilySize'] = df['SibSp'] + df['Parch']
df = df.drop(['Ticket', 'Cabin'], axis=1)

# get_dummies splits up a column into two seperate columns of 1 and 0, where 
# they are true or false. 
dummies_Sex = pd.get_dummies(df['Sex'], prefix='Sex')

# Making dummies for the other categorical features
dummies_Embarked = pd.get_dummies(df['Embarked'], prefix = 'Embarked')
dummies_Pclass = pd.get_dummies(df['Pclass'], prefix = 'Pclass')
dummies_Titles = pd.get_dummies(df['Title'], prefix= 'Title')
dummies_TicketPrefix = pd.get_dummies(df['TicketPrefix'], prefix='TicketPrefix')

# Make new dataframes which have the dummies added on to the end
df = pd.concat([df,dummies_Sex, dummies_Embarked, dummies_Pclass, 
dummies_Titles, dummies_TicketPrefix], axis = 1)

# Drop the categorical data
df = df.drop(['Sex', 'Embarked','Pclass','Title','Name','TicketPrefix'], axis=1)

# Set PassengerId as the index:
df = df.set_index(['PassengerId'])

# FEATURE SELECTION
# To select features we correlate each feature against Survived in the 
# training data. We need # to use different algorithms for the different data 
# types:
# - Spearman-Rank correlation for nominal vs nominal data
# - Point-Biserial correlation for nominal vs continuous data

best_features = df[['Title_Mr', 'Sex_male', 'Sex_female', 'Title_Mrs', 
'Title_Miss', 'Pclass_3', 'Pclass_1', 'Fare', 'Embarked_C', 
'Embarked_S']]

#Output this to csv to be read in for making a prediction
best_features.to_csv('/home/sophie/projects/Titanic/data/clean_test_53.csv', 
sep = " ")

