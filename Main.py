import matplotlib.pyplot as plt

monthly_sales = df.resample('ME', on='Order_Date')['Revenue'].sum()
monthly_sales.plot(title='Monthly Sales Trend')
plt.xlabel('Month')
plt.ylabel('Revenue')
plt.show()
