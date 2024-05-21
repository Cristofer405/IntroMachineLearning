import pandas as pd

def datos_columna(df):
    column_list = df.columns.values.tolist()
    for column_name in column_list:
        print(column_name, len(df[column_name].unique()),df[column_name].unique(), '\n')

def modificar_bool(df, valor):
    for col in valor:
        df[col] = df[col].map({True: 1, False: 0})
    
    return df

def modificar_texto(df, col, valor):
    df[col] = df[col].map(valor).fillna(0)
    return df

def divir_columna(df, col, valor):
    df_div = df[col].str.split('/', expand = True)
    df_div.columns = valor
    return df_div