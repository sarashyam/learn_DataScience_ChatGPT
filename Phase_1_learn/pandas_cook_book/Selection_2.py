import pandas as pd
import numpy as np


def ind_Condtion(df):
    df = df.copy()
    df1 = df[ (df.AAA <= 6) & (df.index.isin([0,2,4]))]
    print("Conditions along with the index")
    print(df1)
    
    print("inversing the operation by putting a tilde(~) symbol")
    df2 = df[~( (df.AAA <= 6) & (df.index.isin([0,2,4])))]
    print(df2)

def change_index_access():
    df = pd.DataFrame(
    {"AAA": [4, 5, 6, 7], "BBB": [10, 20, 30, 40], "CCC": [100, 50, -30, -50]},
    index=["foo", "bar", "boo", "kar"],
    )
    print("index changed and accessing value from foo to boo")
    print(df)
    print(df.loc["foo":"boo"])


df = pd.DataFrame(
    {"AAA": [4, 5, 6, 7], "BBB": [10, 20, 30, 40], "CCC": [100, 50, -30, -50]}
)

ind_Condtion(df)
change_index_access()