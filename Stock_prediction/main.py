import datetime as dt
import matplotlib.pyplot as plt
from matplotlib import style
import pandas as pd
import pandas_datareader.data as web
from matplotlib.finance import candlestick_ohlc
import matplotlib.dates as mdates
style.use('ggplot')

df = pd.read_csv('tsla.csv', parse_dates=True, index_col=0 )
df_ohlc = df['Close'].resample('10D').ohlc()
df_volume = df['Volume'].resample('10D').sum()

#print(df_ohlc.head())
df_ohlc.reset_index(inplace=True)
df_ohlc['Date'] = df_ohlc['Date'].map(mdates.date2num)
#print(df_ohlc.head())

#plt.show()
#df['100ma'] = df['Close'].rolling(window=100, min_periods=0 ).mean()
#df.dropna(inplace=True)

#df[['Close', '100ma']].plot()

ax1 = plt.subplot2grid((6,1), (0,0), rowspan=5, colspan=1)
ax2 = plt.subplot2grid((6,1), (5,0), rowspan=1, colspan=1, sharex=ax1)
ax1.xaxis_date()
candlestick_ohlc(ax1, df_ohlc.values, width=2, colorup='g')
ax2.fill_between(df_volume.index.map(mdates.date2num), df_volume.values, 0)
#ax1.plot(df.index, df['Close'])
#ax1.plot(df.index, df['100ma'])
#ax2.bar(df.index, df['Volume'])
plt.show()

