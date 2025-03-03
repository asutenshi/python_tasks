# %%
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import seaborn as sns

data = pd.read_csv('coffee_shop_revenue.csv')
data = data['Number_of_Customers_Per_Day'].reset_index()

# присвою даты, иначе prophet откажется работать
date_range = pd.date_range(start='2014-01-01', periods=len(data), freq='D')

data['index'] = date_range
data = data.rename(columns={'index' : 'Date'})
data['Date'] = pd.to_datetime(data['Date'])
c_data = data[:720]

plt.figure(figsize=(15, 7))
plt.grid()
locator = mdates.MonthLocator()
X = plt.gca().xaxis
X.set_major_locator(locator)
sns.lineplot(x = c_data['Date'],
             y = c_data['Number_of_Customers_Per_Day'])
plt.xticks(rotation=45, ha='right')
plt.show()

train = c_data[:649]
test = c_data[648:]
#train = grouped_by_week.loc[grouped_by_week['Date'] < '2019-01-01']
#test = grouped_by_week.loc[grouped_by_week['Date'] >= '2019-01-01']

train.shape, test.shape

from prophet import Prophet

model = Prophet()

train.columns = ['ds', 'y']
test.columns = ['ds', 'y']

model.fit(train)
future = model.make_future_dataframe(periods=len(test), freq='W')
future.tail(len(future))

forecast = model.predict(future)
forecast.head()
forecast[['ds', 'yhat', 'yhat_lower', 'yhat_upper']].tail()

from sklearn.metrics import mean_absolute_error
import numpy as np

mape = np.mean(np.abs((test['y'] - forecast['yhat'].tail(len(test)).values) / test['y'])) * 100
print(f"MAPE: {mape:.2f}%")

plt.figure(figsize=(15, 7))
plt.plot(train['ds'], train['y'], label='Training Data')
plt.plot(test['ds'], test['y'], label='Test Data')
plt.plot(forecast['ds'].tail(len(test)), forecast['yhat'].tail(len(test)), label='Forecast')
plt.xlabel('Date')
plt.ylabel('Customers per week')
plt.title('Customers in coffe shop prediction with Prophet')
locator = mdates.MonthLocator()
X = plt.gca().xaxis
X.set_major_locator(locator)
plt.xticks(rotation=45, ha='right')
plt.legend()
plt.grid(True)
plt.show()
# %%