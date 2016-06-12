import pandas as pd
import numpy as np

df = pd.read_csv('/home/sophie/projects/Titanic/data/test.csv', header=0)

# Change Sex column to 1/0 in Gender
df['Gender'] = df['Sex'].map({'female': 0, 'male': 1}).astype(float)

#Drop columns
df = df.drop(['Name','Cabin','Ticket','Sex'], axis=1)

# Remove any rows which have a nan in the Embarked or Fare column
df = df.dropna(subset = ['Embarked','Fare'])

# Turn Embarked into float numbers
df['Embarked'] = df['Embarked'].map({'C': 1 ,'Q': 2 ,'S': 3}).astype(float)


###Make guesses for Age. Use the medians for each class
#Make a table filled with zeros
median_ages = np.zeros((2,3)) # male/female for each class

# Loop over the table to fill in the values
for i in range(0, 2):
    for j in range(0, 3):
        median_ages[i,j] = df[(df['Gender'] == i) & (df['Pclass'] == j + 
        1)]['Age'].dropna().median()
	
# Make a copy of Age 
df['AgeFill'] = df['Age']


# Fill the new column with the correct values.
for i in range(0, 2):
    for j in range(0, 3):
        # we need df.loc here to specify the row AND the column. 
        # only where age is null, gender is 1/0 and class is 1-3, that AgeFill 
        # will be set to the median age.
        df.loc[(df.Age.isnull()) & (df.Gender == i) & (df.Pclass == j + 1), 
        'AgeFill'] = median_ages[i,j]

# We can drop the Age column now we have AgeFill
df = df.drop(['Age'], axis=1)

# Transform the whole dataframe into floats. 
df= df.astype(float)

#Output this to csv to be read in for predicting values.
df.to_csv('/home/sophie/projects/Titanic/data/clean_test.csv', sep = " ", index 
= False) 





