#============================================================================
#mean based on group by values
import numpy as np
import pandas as pd
d = {'key':['X','X','Y','Y','Z'], 
     'X':np.arange(5),
     'Y':[3,4,5,6,7]
    }
df = pd.DataFrame(d)
df_1 = df.groupby('key',as_index=False).mean()
df_2 = df_1.set_index(['key'])


#============================================================================
#fill the null values with specific number
import pandas as pd
import numpy as np

df = pd.DataFrame([[1,2,3,np.nan,4],
                  [2,np.nan,5,6,4],
                  [np.nan,7,np.nan,9,6],
                  [1,np.nan,np.nan,6,7]
                  ])
#1st way-
df_nan  =df.fillna(99.0)
#2nd way
df_rep = df.replcae(np.nan,99.0)

#============================================================================
#drop duplicate rows from dataframe

import pandas as pd
df = pd.DataFrame({'col1':['A']*3 +['B']*4+['C','B','A'],
                    'col2':[2,3,4,2,4,2,1,3,4,4]})
df_dup = df.drop_duplicates(keep='first')

#============================================================================
df_1 = df.apply(pd.to_numeric, errors="ignore").applymap(lambda x: isinstance(x, float), na_action='ignore')
for i in range(0,len(df)):
    if df[i].dtypes == 'float':
        df.replace(df[i],1.0)
    elif df[i].dtypes == 'int':
        df[i].replace(df[i],1)
    else:
        df[i].dtypes(df[i], np.nan)
    
df = pd.DataFrame([[1,2,3,np.nan,4],
                  [2,np.nan,5,6,4],
                  [np.nan,7,np.nan,9,6],
                  [1,np.nan,np.nan,6,7]
                  ])
columns=['A','B','C','D','E']

df['column'] = np.where(df['column'].isnull(), 'value_if_true', 'value_if_false')

for i in range(len(df)+1):
    df[i] = np.where(df[i].dtypes == 'float', 1.0, np.nan)


#============================================================================

"""
database: test
============================================================================
SELECT fname 
FROM customer 
JOIN invoice ON customer.cid = invoice.cid 
WHERE total= (select max(total) from invoice);
============================================================================

SELECT p.playlistid, p.pname 
FROM playlist as p 
JOIN playlisttrack as pt on p.playlistid = pt.playlistid 
JOIN track as t on pt.trackid = t.trackid 
JOIN gener as g on t.generid = g.generid 
WHERE g.gname not like '%latin%'
ORDER BY p.playlistid asc;
============================================================================
"""

#operations on dtaframe and series object
info = {'x' : 0., 'y' : 1., 'z' : 2.} 
d_series = pd.Series(info)
print(d_series) 
"""
out: 
>>> d_series
X    0
Y    1
Z    2
"""

d_frame= pd.DataFrame(info,index=['P'])  #note if we not add index fora single valued dict then it will throw an error
"""
out:
>>> d_frame
   X  Y  Z
P  0  1  2

"""
#============================================================================
#to add the new column in dataframe-
info = {'one' : pd.Series([1, 2, 3, 4, 5], index=['a', 'b', 'c', 'd', 'e']),    
        'two' : pd.Series([1, 2, 3, 4, 5, 6], index=['a', 'b', 'c', 'd', 'e', 'f'])}  

df = pd.DataFrame(info)

df['four'] = pd.Series([4,5,6], index=['a','b','c'])

#to add the new row in dataframe
#.iloc and .loc methods

# Python program to convert list of nested 
# dictionary into Pandas dataframe
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++  
# importing pandas
import pandas as pd
  
# List of list of dictionary initialization
list = [
        {
        "Student": [{"Exam": 90, "Grade": "a"},
                    {"Exam": 99, "Grade": "b"},
                    {"Exam": 97, "Grade": "c"},
                   ],
        "Name": "Paras Jain"
        },
        {
        "Student": [{"Exam": 89, "Grade": "a"},
                    {"Exam": 80, "Grade": "b"}
                  ],
        "Name": "Chunky Pandey"
        }
       ]
  
# rows list initialization
rows = []
  
# appending rows
for data in list:
    data_row = data['Student']
    time = data['Name']
      
    for row in data_row:
        row['Name']= time
        rows.append(row)
  
# using data frame
df = pd.DataFrame(rows)
  
# using pivot_table
df = df.pivot_table(index ='Name', columns =['Grade'],
                        values =['Exam']).reset_index()
  
# Defining columns
df.columns =['Name', 'Maths', 'Physics', 'Chemistry']
  
# print dataframe
print(df)

#=============================================================================
a  = [1,2,3,4]
b  = [3,4,5,6]
common = []
notintwo = []
def cnt(a,b):
    c = 0
    for i in a:
        if i not in b:
                notintwo.append(i)
    return notintwo

co= cnt(a,b)
#=============================================================================