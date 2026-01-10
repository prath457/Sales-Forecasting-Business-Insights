import pandas as pd

df = pd.read_csv('sales_data.csv')
df['Order_Date'] = pd.to_datetime(df['Order_Date'])
df.drop_duplicates(inplace=True)
