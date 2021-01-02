##Series
import numpy as np
import pandas as pd

#Instantiation of a list
labels = ['a','b','c']

my_data = [10,20,30]
#Instantiation of an array
arr = np.array(my_data)
#Instantiation of dictionary
d = {'a':10, 'b':20, 'c':30}

#Setting data with our instantiated array (Line:8)
pd.Series(data = my_data)
#0  10
#1  20
#2  30


#Setting data with our instantiated array and list values as the key for each data
pd.Series(data = my_data, index = labels)
#Alternate way:
pd.Series(my_data,labels) #Note: We don't really need to specify "data" and "index"
                          #      inside the code, as long as we put them in order
#or
pd.Series(arr, labels)

#Setting data using a dictionary
pd.Series(d)#Automatically inserts key as index and data as value

#Passing built-in functions
pd.Series(data = [sum,print,len])

#Note: The key of using a series is understanding index(es)

#Setting keys and values using one line
ser1 = pd.Series([1,2,3,4], ['Canada', 'USA', 'USSR', 'China'])# Note, first parameter is going to be the data while the other is the key

ser2 = pd.Series([1,2,4,3], ['Canada', 'USA', 'USSR', 'Cuba'])

#Retrieving index value
ser1['USA']#Note: If label is unindentified, we have to use the default index given, which starts at 0...size

#Adding two series
ser1 + ser2 # Will return a sum of both matching index keys and returns NaN if either Series has a unique key
            # Note: Performing operation on Pandas will automatically convert it to float, in-order not to lose information due to any equation(s).