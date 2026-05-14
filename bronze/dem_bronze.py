import pandas as pd

df_bronze = pd.read_excel('RNGWHHDm.xls',sheet_name='Data 1', engine="xlrd")

index_header=0
for i in range(len(df_bronze)):
    value=df_bronze.iloc[i,0]
    if value =='Date':
        index_header+=i
        break

df_bronze.columns=list(df_bronze.iloc[index_header])
df_bronze=df_bronze.iloc[index_header+1:]