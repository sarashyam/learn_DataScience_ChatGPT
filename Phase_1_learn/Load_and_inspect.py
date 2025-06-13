# History
# step 1 - SAS - to load the csv file and then inspect it
# to use 
# read_csv , head , info , describe

# step 2 -SAS
# Clean the data

import pandas  as pd 


# reading the csv file to a dataframe df
df  = pd.read_csv("sales_data.csv")
print(df)


#   Order ID        Date Region     Product         Category  Quantity  Unit Price  Total Sales
# 0      1001  2024-01-05   East    Notebook  Office Supplies         5         2.5         12.5
# 1      1002  2024-01-06   West     Printer       Technology         1       150.0        150.0
# 2      1003  2024-01-07  South         Pen  Office Supplies        10         1.2         12.0
# 3      1004  2024-01-08  North  Desk Chair        Furniture         2        85.0        170.0
# 4      1005  2024-01-09   East      Laptop       Technology         1       950.0        950.0
# 5      1006  2024-01-10  South     Monitor       Technology         2       200.0        400.0
# 6      1007  2024-01-11   West       Paper  Office Supplies        20         0.5         10.0
# 7      1008  2024-01-12  North        Sofa        Furniture         1       400.0        400.0
# 8      1009  2024-01-13   East      Tablet       Technology         3       300.0        900.0
# 9      1010  2024-01-14  South    Bookcase        Furniture         1       120.0        120.0


# this will only print top two rows
print(df.head(2)) 

#    Order ID        Date Region   Product         Category  Quantity  Unit Price  Total Sales
# 0      1001  2024-01-05   East  Notebook  Office Supplies         5         2.5         12.5
# 1      1002  2024-01-06   West   Printer       Technology         1       150.0        150.0



# this will print the detial of  the csv
print(df.info())

# <class 'pandas.core.frame.DataFrame'>
# RangeIndex: 10 entries, 0 to 9
# Data columns (total 8 columns):
#  #   Column       Non-Null Count  Dtype
# ---  ------       --------------  -----
#  0   Order ID     10 non-null     int64
#  1   Date         10 non-null     object
#  2   Region       10 non-null     object
#  3   Product      10 non-null     object
#  4   Category     10 non-null     object
#  5   Quantity     10 non-null     int64
#  6   Unit Price   10 non-null     float64
#  7   Total Sales  10 non-null     float64
# dtypes: float64(2), int64(2), object(4)
# memory usage: 772.0+ bytes
# None


# it will show the basic details of each column
print(df.describe())

#          Order ID   Quantity  Unit Price  Total Sales
# count    10.00000  10.000000   10.000000    10.000000
# mean   1005.50000   4.600000  220.920000   312.450000
# std       3.02765   6.095536  288.401047   353.152505
# min    1001.00000   1.000000    0.500000    10.000000
# 25%    1003.25000   1.000000   23.125000    39.375000
# 50%    1005.50000   2.000000  135.000000   160.000000
# 75%    1007.75000   4.500000  275.000000   400.000000
# max    1010.00000  20.000000  950.000000   950.000000

# to check if any nulls are present
print(df.isnull().sum())

# Order ID       0
# Date           0
# Region         0
# Product        1
# Category       0
# Quantity       0
# Unit Price     0
# Total Sales    0
# dtype: int64




print(df['Quantity'].unique())
print(type(df['Date']))
df["Date"] = pd.to_datetime(df['Date'],errors='coerce')
df.fillna(0)

print(type(df['Date']))

# converting the datatype of a column
df['Quantity'] = df['Quantity'].astype(int)


# used to rename the column or the columns
df = df.rename(columns={'Order ID' : "Order_ID"})

print(df)

print(df.shape)

# total sales amount

print(df["Total Sales"].sum())

# Which product/category sold the most?

print(df.loc[df["Total Sales"].idxmax()])

# which category do we have the most

# ---count occurence
occurance = df['Category'].value_counts()

# --highest value
high_val = occurance.idxmax()
print(high_val)

disp = df[ df['Category'] == high_val ]
print(disp)



