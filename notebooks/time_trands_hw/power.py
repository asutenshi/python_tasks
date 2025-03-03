# %%
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import seaborn as sns

data = pd.read_csv('household_power_consumption.csv')
data['Date'] = pd.to_datetime(data['Date'])
data = data[data['Global_active_power'] != '?']
data['Global_active_power'] = pd.to_numeric(data['Global_active_power'])
data = data.groupby('Date')['Global_active_power'].sum().reset_index()

plt.figure(figsize=(15, 7))
plt.grid()

locator = mdates.MonthLocator()
X = plt.gca().xaxis
X.set_major_locator(locator)

sns.lineplot(x = data['Date'],
             y = data['Global_active_power'])
plt.xticks(rotation=45, ha='right')
plt.show()

train = data.loc[data['Date'] < '2024-12-20']
test = data.loc[data['Date'] >= '2024-12-20']

train.shape, test.shape

train_0 = train.groupby(['Date'])['Global_active_power'].sum().reset_index()
test_0 = test.groupby(['Date'])['Global_active_power'].sum().reset_index()

train_0.head()

from prophet import Prophet

model = Prophet(
    changepoint_prior_scale=0.05,  # Регулирует гибкость тренда
    seasonality_prior_scale=10,    # Усиливает сезонный компонент
    daily_seasonality=False,       # Биржевые данные обычно не имеют дневной сезонности
    weekly_seasonality=True,       # Учитывает недельную сезонность
    yearly_seasonality=True        # Учитывает годовую сезонность
)

train_0.columns = ['ds', 'y']
test_0.columns = ['ds', 'y']

model.fit(train_0)
future = model.make_future_dataframe(periods=30)
future.tail(30)

forecast = model.predict(future)
forecast.head()
forecast[['ds', 'yhat', 'yhat_lower', 'yhat_upper']].tail()

#model.plot(forecast)
#model.plot_components(forecast)

from sklearn.metrics import mean_absolute_error
import numpy as np

mape = np.mean(np.abs((test_0['y'] - forecast['yhat'].tail(len(test_0)).values) / test_0['y'])) * 100
print(f"MAPE: {mape:.2f}%")

# %%
