import pandas as pd
import numpy as np

d = {'Name':pd.Series(['Tom','James','Ricky',None,'Steve','Minsu','Jack',
   'Lee','David','David','Betina','Andres','James']),
   'Age':pd.Series([25,26,25,23,30,29,None,34,30,30,51,46,26]),
   'Rating':pd.Series([4.23,3.24,3.98,2.56,3.20,None,3.8,3.78,4.8,4.80, None,3.65,3.24])}

df = pd.DataFrame(d)
print(df.head())

print(df.duplicated(keep='first'))
print(df.duplicated(keep='last').sum())
print(df[df.duplicated(keep='first')])

df.drop_duplicates(keep='last',inplace=True)
df.reset_index(inplace=True,drop=True)
print(df)
print(df.describe().T)
print(df[df['Age']>33])


print(df[df["Age"].notnull()])
df["Age"].dropna(inplace=True)

Arr1=pd.DataFrame(data=[[1,2,3,4,5],
                        [6,7,8,9,10],
                        [11,12,13,14,15]],
                  index=['b','a','c'],
                  columns=['p','q','x','y','z'])
print(Arr1)
Arr2=pd.DataFrame(data=[[1,2,3,4,5],
                        [6,7,8,9,10]],
                  columns=['p','q','x','y','z'])
print(Arr2)
Arr3=pd.concat([Arr1,Arr2],axis=0)
print(Arr3)


str="          hello luya  "
str=str.strip()
print(str)


Arr4=pd.Series(['rfGRe4.5分深',
                'rwSe4.8分',
                'rGGRer2.7分',
                'ddGRd8.3分'])
Arr4=Arr4.str.extract('(^[A-Z a-z]+)(\d\.\d分$)',expand=True)
print(Arr4)

s = pd.Series(['a1', 'b2', 'ca25','d5','t6'])
s=s.str.extract(r'([abcd])(\d)')
print(s)