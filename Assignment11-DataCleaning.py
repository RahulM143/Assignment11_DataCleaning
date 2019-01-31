import pandas as pd
import numpy as np

df = pd.DataFrame({'From_To': ['LoNDon_paris', 'MAdrid_miLAN', 'londON_StockhOlm',
'Budapest_PaRis', 'Brussels_londOn'],
'FlightNumber': [10045, np.nan, 10065, np.nan, 10085],
'RecentDelays': [[23, 47], [], [24, 43, 87], [13], [67, 32]],
'Airline': ['KLM(!)', '<Air France> (12)', '(British Airways. )',
'12. Air France', '"Swiss Air"']})
df.head()

#1. Some values in the the FlightNumber column are missing. These numbers are meant
#to increase by 10 with each row so 10055 and 10075 need to be put in place. Fill in
#these missing numbers and make the column an integer column (instead of a float
#column).
print ('Dataframe with missing values \n', df.head())
df['FlightNumber'].fillna (value = 10055, limit = 1, downcast = 'int64', inplace = True)
df['FlightNumber'].fillna (10075, inplace = True, downcast ='int64')
print ('\n\nDataframe after missing values treatment \n', df.head())

#2. The From_To column would be better as two separate columns! Split each string on
#the underscore delimiter _ to give a new temporary DataFrame with the correct values.
#Assign the correct column names to this temporary DataFrame.
tf = df['From_To']
tf = tf.to_frame()
tf ['From'] = tf['From_To'].apply (lambda x: x.split('_')[0])
tf['To'] = df['From_To'].apply (lambda x: x.split('_')[1])
del tf['From_To']
print('Temporary DataFrame after splitting From_To column \n',tf.head())

#3. Notice how the capitalisation of the city names is all mixed up in this temporary
#DataFrame. Standardise the strings so that only the first letter is uppercase (e.g.
#"londON" should become "London".)
tran = lambda x: x[0].upper() + x[1:].lower()
tf['From'] = tf['From'].map(tran)
tf['To'] = tf['To'].map(tran)
print('Temporary dataframe with stadardized strings in from to columns \n',tf)
#4. Delete the From_To column from df and attach the temporary DataFrame from the
#previous questions.
df = pd.merge(df,tf,left_index = True, right_index=True)
del df['From_To']
print ('Original dataframe after merging with temporary dataframe \n',df)

#5. In the RecentDelays column, the values have been entered into the DataFrame as a
#list. We would like each first value in its own column, each second value in its own
#column, and so on. If there isn't an Nth value, the value should be NaN.
#Expand the Series of lists into a DataFrame named delays, rename the columns delay_1,
#delay_2, etc. and replace the unwanted RecentDelays column in df with delays.
df.head()
d1 = df['RecentDelays']
d1
d2 = (pd.DataFrame(d1.values.tolist())).rename(columns = lambda x: 'Delay_{}'.format(x+1))
d2
dff = df.merge (d2,left_index = True, right_index=True, how ='inner')
print ('Joined Dataframes: \n', dff ) 
del dff ['RecentDelays']  
print ('\n\nFinal Dataframe: \n', dff )

         
        







