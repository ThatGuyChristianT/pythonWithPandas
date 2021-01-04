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
df.loc[['A', 'B'],['W', 'Y']] #Returns a sub-set of the dataframe

##Conditional Selection and multi-index parts of Dataframe

#Re-creation of a simple excel sheet
df = pd.DataFrame(randn(5,4), ['A','B','C','D','E'], ['W','X','Y','Z'])

#Retrieving table that is greater than 0
df > 0
#Visual Representation
'''
       W      X      Y      Z
A   True   True  False  False
B  False   True   True   True
C   True   True   True   True
D  False  False  False   True
E  False   True   True   True
'''

#Retrieving table values that is greater than 0
df[df>0] #Returns all number values that meets the criteria, otherwise returns NaN.
#Visual Representation
'''
          W         X         Y         Z
A  0.302665  1.693723       NaN       NaN
B       NaN  0.390528  0.166905  0.184502
C  0.807706  0.072960  0.638787  0.329646
D       NaN       NaN       NaN  0.484752
E       NaN  1.901755  0.238127  1.996652
'''

#Asserting specific column value if each index is great than 0
[df['W'] > 0] #Note: Returns a Series value

#List table row values if first column index is greater than 0
df[df['W']> 0]
#Visual Representation
'''
          W         X         Y         Z
A  0.302665  1.693723 -1.706086 -1.159119
C  0.807706  0.072960  0.638787  0.329646
'''

#Multiple Condition
df[(df['W'] > 0) & (df['Y']>1)]

#Resetting index
df.reset_index()
#Visual Representation
'''
  index         W         X         Y         Z
0     A  0.302665  1.693723 -1.706086 -1.159119
1     B -0.134841  0.390528  0.166905  0.184502
2     C  0.807706  0.072960  0.638787  0.329646
3     D -0.497104 -0.754070 -0.943406  0.484752
4     E -0.116773  1.901755  0.238127  1.996652
'''

#Creation of a new index
newindex = 'JU ST AH RA CO'.split()
df['States'] = newindex

#Assiging a new index
df.set_index('States') #Overwrites existing index

##Multi-index and index hierarchy

# Index Levels
outside = ['G1','G1','G1','G2','G2','G2']
inside = [1,2,3,1,2,3]
#Creates a list of tuple pair
hier_index = list(zip(outside,inside))

hier_index = pd.MultiIndex.from_tuples(hier_index)

#Construction of a MultiIndex
df = pd.DataFrame(randn(6,2), hier_index,['A', 'B'])
#Visual Representation
'''
             A         B
G1 1 -0.993263  0.196800
   2 -1.136645  0.000366
   3  1.025984 -0.156598
G2 1 -0.031579  0.649826
   2  2.154846 -0.610259
   3 -0.755325 -0.346419
'''
#Retrieving G2's row 2 values
df.loc['G2'].loc[2] #Returns series
#Visual Representation
'''
A    2.154846
B   -0.610259
Name: 2, dtype: float64
'''
#Setting index value for both G1+ and indexes
df.index.names = ['Groups', 'ID']
df
#Visual Representation
'''
                  A         B
Groups ID                    
G1     1  -0.993263  0.196800
       2  -1.136645  0.000366
       3   1.025984 -0.156598
G2     1  -0.031579  0.649826
       2   2.154846 -0.610259
       3  -0.755325 -0.346419
'''

##Missing Data: Dealing with Missing Data
#Note: If there are going to be any missing value(s), Pandas will automatically fill with a null or NaN value

#Instantiation of Dictionary
d = {'A': [1,2,np.nan], 'B':[5,np.nan,np.nan], 'C': [1,2,3]}

df = pd.DataFrame(d)
#Visual Representation
'''
     A    B  C
0  1.0  5.0  1
1  2.0  NaN  2
2  NaN  NaN  3
'''

#Drops any row by dafault that has any null/NaN value
df.dropna()
#Visual Representation
'''
     A    B  C
0  1.0  5.0  1
'''

#Drops any columns that has any null/NaN value
df.dropna(axis = 1)
#Visual Representation
'''
   C
0  1
1  2
2  3
'''

#Drop rows with row values having 2 or more NaN values
df.dropna(thresh = 2)

#Overwrites all NaN value with "some value"
df.fillna(value = 'some value')

#Overwriting specific index value of missing data
df['A'].fillna(value = df['A'].mean())

##Groupby

# Create dataframe
data = {'Company':['GOOG','GOOG','MSFT','MSFT','FB','FB'],
       'Person':['Sam','Charlie','Amy','Vanessa','Carl','Sarah'],
       'Sales':[200,120,340,124,243,350]}

df = pd.DataFrame(data)

#Grouping by column name
byComp = df.groupby('Company')#Note, if df.groupby(...) printed, it will just return an object.
                              #Call aggregate function of the object to retrieve any value.

#Returns the of overall company's column
byComp.mean()
#Returns sum of overall company's column
byComp.sum() #Note, Methods with arithmetic will only work with numbers.

#Retrieving various information at once
df.groupby('Company').describe()
#Visual Representation
'''
        Sales                                                        
        count   mean         std    min     25%    50%     75%    max
Company                                                              
FB        2.0  296.5   75.660426  243.0  269.75  296.5  323.25  350.0
GOOG      2.0  160.0   56.568542  120.0  140.00  160.0  180.00  200.0
MSFT      2.0  232.0  152.735065  124.0  178.00  232.0  286.00  340.0
'''

#Retrieving specific in-depth information from a row
df.groupby('Company').describe().transpose()['FB']
#Visual Representation
'''
Sales  count      2.000000
       mean     296.500000
       std       75.660426
       min      243.000000
       25%      269.750000
       50%      296.500000
       75%      323.250000
       max      350.000000
Name: FB, dtype: float64
'''

##Merging, Joining, and Concatenating Dataframes

#Instantiation of multiple data-frames
df1 = pd.DataFrame({'A': ['A0', 'A1', 'A2', 'A3'],
                        'B': ['B0', 'B1', 'B2', 'B3'],
                        'C': ['C0', 'C1', 'C2', 'C3'],
                        'D': ['D0', 'D1', 'D2', 'D3']},
                        index=[0, 1, 2, 3])
df2 = pd.DataFrame({'A': ['A4', 'A5', 'A6', 'A7'],
                        'B': ['B4', 'B5', 'B6', 'B7'],
                        'C': ['C4', 'C5', 'C6', 'C7'],
                        'D': ['D4', 'D5', 'D6', 'D7']},
                         index=[4, 5, 6, 7])
df3 = pd.DataFrame({'A': ['A8', 'A9', 'A10', 'A11'],
                        'B': ['B8', 'B9', 'B10', 'B11'],
                        'C': ['C8', 'C9', 'C10', 'C11'],
                        'D': ['D8', 'D9', 'D10', 'D11']},
                        index=[8, 9, 10, 11])

#Concatenating dataframes together by Rows (Default axis is 0)
pd.concat([df1,df2,df3])
#Visual Representation
'''
      A    B    C    D
0    A0   B0   C0   D0
1    A1   B1   C1   D1
2    A2   B2   C2   D2
3    A3   B3   C3   D3
4    A4   B4   C4   D4
5    A5   B5   C5   D5
6    A6   B6   C6   D6
7    A7   B7   C7   D7
8    A8   B8   C8   D8
9    A9   B9   C9   D9
10  A10  B10  C10  D10
11  A11  B11  C11  D11
'''

#Concatenating dataframes by Columns
concatenated_by_columns = pd.concat([df1,df2,df3], axis = 1)
#Visual Representation
'''
      A    B    C    D    A    B    C    D    A    B    C    D
0    A0   B0   C0   D0  NaN  NaN  NaN  NaN  NaN  NaN  NaN  NaN
1    A1   B1   C1   D1  NaN  NaN  NaN  NaN  NaN  NaN  NaN  NaN
2    A2   B2   C2   D2  NaN  NaN  NaN  NaN  NaN  NaN  NaN  NaN
3    A3   B3   C3   D3  NaN  NaN  NaN  NaN  NaN  NaN  NaN  NaN
4   NaN  NaN  NaN  NaN   A4   B4   C4   D4  NaN  NaN  NaN  NaN
5   NaN  NaN  NaN  NaN   A5   B5   C5   D5  NaN  NaN  NaN  NaN
6   NaN  NaN  NaN  NaN   A6   B6   C6   D6  NaN  NaN  NaN  NaN
7   NaN  NaN  NaN  NaN   A7   B7   C7   D7  NaN  NaN  NaN  NaN
8   NaN  NaN  NaN  NaN  NaN  NaN  NaN  NaN   A8   B8   C8   D8
9   NaN  NaN  NaN  NaN  NaN  NaN  NaN  NaN   A9   B9   C9   D9
10  NaN  NaN  NaN  NaN  NaN  NaN  NaN  NaN  A10  B10  C10  D10
11  NaN  NaN  NaN  NaN  NaN  NaN  NaN  NaN  A11  B11  C11  D11

'''

##Operations

df = pd.DataFrame({'col1':[1,2,3,4],
                   'col2':[444,555,666,444],
                   'col3':['abc','def','ghi','xyz']})
df.head()

#Finding unique values on specific column
df['col2'].unique()

#Finding count of unique values on specific columns
df['col2'].nunique()

#Find occurrences for each values
df['col2'].value_counts()

#Returning only data with specific conditions
df[df['col1'] >2]

#Returning only data with multiple specific conditions
df[(df['col1'] >2) & (df['col2']  == 444)]

#Passing column values to a method
def minus2(value):
    return value -2
df['col1'].apply(minus2)

#Passing column values using a lambda expression
df['col1'].apply(lambda x: x-2)

#Dropping specific column(s)
df.drop('col1', axis = 1 ) #change in-place to true if save changes

#Sorting df by specific column
df.sort_values('col2')

data = {'A':    ['foo','foo','foo','bar','bar','bar'],
        'B':    ['one','one','two','two','one','one'],
        'C':    ['x','y','x','y','x','y'],
        'D':    [1,3,2,5,4,1]}

df = pd.DataFrame(data)

#Creating multi-column index
df.pivot_table(values = 'D', index = ['A', 'B'], columns = ['C'])
#Visual Representation
'''
C          x    y
A   B            
bar one  4.0  1.0
    two  NaN  5.0
foo one  1.0  3.0
    two  2.0  NaN
'''

##Data Input and Output
 # - CSV
 # - Excel
 # - HTML
 # - SQL
 
#Reading Csv file
df = pd.read_csv('resources/input_data/example.csv')
#Visual Representation
'''
    a   b   c   d
0   0   1   2   3
1   4   5   6   7
2   8   9  10  11
3  12  13  14  15
'''

#saving data to CSV
df.to_csv('resources/output_data/My_output', index = False)# Setting index to false because I
                                     # don't want the index to be part of the column

#Reading Excel file
pd.read_excel('resources/input_data/Excel_Sample.xlsx', sheet_name= 'Sheet1')#Note: Each sheet is seen as a data-frame.

#Exporting data to excel
df.to_excel('resources/output_data/exportingDataFrame.xlsx',  sheet_name= 'NewSheet')

#Reading HTML data
data = pd.read_html('http://www.fdic.gov/bank/individual/failed/banklist.html')#Keep in-mind, Pandas will try to search for all tables in the HTML.
                                                                             # Therefore returning a list.

#Reading SQL data

#Allows us to create a sql memory in the project
from sqlalchemy import create_engine

#Creates SQL engine in memory.
engine = create_engine('sqlite:///:memory:')#Creates temporary SQL Lite engine that's running in memory

df.to_sql('resources/output_data/my_sql_table', engine)

sqldf = pd.read_sql('resources/output_data/my_sql_table', con = engine)
#Visual Representation
'''
   index   a   b   c   d
0      0   0   1   2   3
1      1   4   5   6   7
2      2   8   9  10  11
3      3  12  13  14  15
'''
#Note: Be sure to search for libraries specifically for the SQL that's being used