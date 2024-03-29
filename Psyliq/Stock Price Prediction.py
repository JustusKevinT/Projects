
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import yfinance as yf
from sklearn.preprocessing import MinMaxScaler
from keras.layers import Dense, Dropout, LSTM
from keras.models import Sequential

start = input("2012-01-01") 
end = input("2023-12-22") 
stock = input("SBUX") 
data = yf.download(stock,start,end)

data

data.reset_index(inplace = True)
data

ma_100_days = data.Close.rolling(100).mean()

plt.figure(figsize=(10,8))
plt.plot(ma_100_days,"b",label="MA(100)")
plt.plot(data.Close, "g",label="Original Price")
plt.xlabel("Time")
plt.ylabel("Price")
plt.show()

ma_200_days = data.Close.rolling(200).mean()

plt.figure(figsize=(10,8))
plt.plot(ma_100_days,"r",label="MA(100)")
plt.plot(ma_200_days,"b",label="MA(200)")
plt.plot(data.Close, "g",label="Origrinal Price")
plt.xlabel("Time")
plt.ylabel("Price")
plt.show()

data.dropna(inplace=True)

data_train = pd.DataFrame(data.Close[0:int(len(data) * 0.80)])
data_test = pd.DataFrame(data.Close[int(len(data) * 0.80) : len(data)])

data_train.shape[0], data_test.shape[0]

scaler = MinMaxScaler(feature_range=(0,1))
data_train_scale = scaler.fit_transform(data_train)

x,y = [],[]
for i in range(100, data_train_scale.shape[0]):
    x.append(data_train_scale[i-100:i])
    y.append(data_train_scale[i,0])

x,y = np.array(x),np.array(y)
model = Sequential()
model.add(LSTM(units=50,activation="relu", return_sequences = True, input_shape=((x.shape[1],1))))
model.add(Dropout(0.2))
model.add(LSTM(units=60,activation="relu",return_sequences=True))
model.add(Dropout(0.3))
model.add(LSTM(units=80,activation="relu",return_sequences=True))
model.add(Dropout(0.4))
model.add(LSTM(units=120,activation="relu"))
model.add(Dropout(0.5))
model.add(Dense(units=1))

model.compile(optimizer="adam",loss="mean_squared_error")

model.fit(x,y, epochs=50, batch_size=32, verbose=1)

model.summary()

pas_100_days = data_train.tail(100)
data_test = pd.concat([pas_100_days,data_test], ignore_index=True)
data_test

data_test_scale = scaler.fit_transform(data_test)

x,y = [],[]
for i in range(100, data_test_scale.shape[0]):
    x.append(data_test_scale[i-100:i])
    y.append(data_test_scale[i,0])

x,y = np.array(x), np.array(y)
y_predict = model.predict(x)

scale = 1/scaler.scale_

y_predict = y_predict*scale
y = y*scale

plt.figure(figsize=(10,8))
plt.plot(y_predict,"r",label="Predicted Price")
plt.plot(y,"g",label="Original Price")
plt.xlabel("Time")
plt.ylabel("Price")
plt.legend()
plt.show()








