##Data-frames
import numpy as np
import pandas as pd

from numpy.random import randn

#Seed makes sure you're getting random numbers between 0~100
np.random.seed(101)

#Creation of a simple excel sheet
df = pd.DataFrame(randn(5,4), ['A','B','C','D','E'], ['W','X','Y','Z']) #First parameter is how many rows and columns.
                                                                        #Second parameter are row identifier(s) while the last are for the column.
#For visualization purpose:
''' 
          W         X         Y         Z
A  2.706850  0.628133  0.907969  0.503826
B  0.651118 -0.319318 -0.848077  0.605965
C -2.018168  0.740122  0.528813 -0.589001
D  0.188695 -0.758872 -0.933237  0.955057
E  0.190794  1.978757  2.605967  0.683509
'''
#Note: Each of the column's a Pandas Series that shares common index

#Retrieving specific column value
df['Z']
#Alternate way:
df.Z#Not really recommended because it'll end up in confusion whether a function is being called or a value

#Finding out what type the column is
type(df['Z']) #Returns pandas.core.series.Series

#Retrieving multiple columns
df[['W','Z']]#Note: For multiple column, we must pass a list of columns
                    #Returns a data-frame if multiple column. If it's single column, it returns a Series

#Creation of new column
df['SumOfXAndY'] = df['X'] + df['Y']#Note: Each column of X and Y are added, resulting in having the new column to hold the sum of both
'''
          W         X         Y         Z  SumOfXAndY
A  2.706850  0.628133  0.907969  0.503826    1.536102
B  0.651118 -0.319318 -0.848077  0.605965   -1.167395
C -2.018168  0.740122  0.528813 -0.589001    1.268936
D  0.188695 -0.758872 -0.933237  0.955057   -1.692109
E  0.190794  1.978757  2.605967  0.683509    4.584725

'''
#Important: axis = 0 refers to as rows while axis = 1 refers to as the column. Or X and Y axis
#Removal of column
df.drop('SumOfXAndY', axis = 1) #Note: if this statement is executed on and printed, operation will be performed on this line only.

df.drop('SumOfXAndY', axis = 1, inplace=True) #Note: inplace has to be set to true "inplace" to save the changes
                                #It's more of a safety net to not accidentally lose data

#Dropping rows
df.drop('E')# axis does not need to be specified because default value is 0.

#Retrieving count of Rows + Columns
df.shape

#Selecting Row
df.loc['A']#Takes in a label

#Selecting Row using a numerical index position
df.iloc[0]

#Selecting sub-sets of rows and columns
df.loc['B', 'Y'] #Retrieves specific index
df.loc[['A', 'B']['W', 'Y']] #Returns a sub-set of the dataframe