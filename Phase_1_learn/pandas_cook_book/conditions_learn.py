import pandas as pd
import numpy as np

def arg_sort(df):
    df = df.copy()
    # -----------------------argsort()-------------------------
    print("argument sort")
    specific_val = 43
    print(df.loc[(df.CCC - specific_val).abs().argsort()])
    # .argsort() tells you the order of positions to sort values from smallest to largest.
    print(df.loc[(df.CCC).argsort()])
    print(df)


    Crit1 = df.AAA <= 5.5

    Crit2 = df.BBB == 10.0

    Crit3 = df.CCC > -40.0

    print(Crit1)
    print(Crit2)
    print(Crit3)


    AllCrit = Crit1 & Crit2 & Crit3

    print(AllCrit)

    import functools
    crit_lst = [Crit1,Crit2,Crit3]
    AllCrit = functools.reduce(lambda x,y :x & y ,crit_lst)
    print(AllCrit)

    print(df[AllCrit])


def change_col(df):
    
    df = df.copy()
    print("change one column")
    df.loc[df.AAA >= 5,"BBB"] = -1
    # for multiple cols just add the column names in [ ]
    print(df)


def add_col_with_logic(df):
    df = df.copy()
    print("adding column")
    
    df['logic'] = np.where(df["AAA"] >=5, "high","low")
    
    print(df)



def check_and_assign(df):
    df = df.copy()
    print("check and assign value")
    df.loc[(df["BBB"]<25) & (df["CCC"]>=40),"AAA"] = "aa"
    print(df)
    

df = pd.DataFrame(
    {"AAA": [4, 5, 6, 7], "BBB": [10, 20, 30, 40], "CCC": [100, 50, -30, -50]}
)




arg_sort(df)
change_col(df)
add_col_with_logic(df)
check_and_assign(df)