import pandas as pd
import quandl, math, datetime
import numpy as np
from sklearn import preprocessing, svm, model_selection
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
from matplotlib import style

dataFrame = quandl.get('WIKI/GOOGL')
print(dataFrame.tail())

# Changing the data frame to only include the columns that we care about
dataFrame = dataFrame[['Adj. Open', 'Adj. High', 'Adj. Low', 'Adj. Close', 'Adj. Volume',]]
# High low percentage
dataFrame['HL_PCT'] = (dataFrame['Adj. High'] - dataFrame['Adj. Close']) / dataFrame['Adj. Close'] * 100
# Percent change
dataFrame['PCT_change'] = (dataFrame['Adj. Close'] - dataFrame['Adj. Open']) / dataFrame['Adj. Open'] * 100

# Define the columns that we care about
dataFrame = dataFrame[['Adj. Close', 'HL_PCT', 'PCT_change', 'Adj. Volume']]


forecastColumn = 'Adj. Close'
dataFrame.fillna(-99999, inplace=True)

forecastOut = int(math.ceil(0.01*len(dataFrame)))


dataFrame['label'] = dataFrame[forecastColumn].shift(-forecastOut)


# features are usually a 'X'
# labels are usually a 'y'
features = np.array(dataFrame.drop(['label'], 1))
features = preprocessing.scale(features)
features = features[:-forecastOut]
featuresLately = features[-forecastOut:]
# print(features.tail())
# print(featuresLately)


dataFrame.dropna(inplace=True)
labels = np.array(dataFrame['label'])

features_train, features_test, labels_train, labels_test = model_selection.train_test_split(features, labels, test_size=0.2)

classifier = LinearRegression(n_jobs=-1)
classifier.fit(features_train, labels_train)
accuracy = classifier.score(features_test, labels_test)

forecastSet = classifier.predict(featuresLately)
print(forecastSet, accuracy, forecastOut)

dataFrame['Forecast'] = np.nan

lastDate = dataFrame.iloc[-1].name
lastUnix = lastDate.timestamp()
oneDay = 86400
nextUnix = lastUnix + oneDay

for i in forecastSet:
    nextDate = datetime.datetime.fromtimestamp(nextUnix)
    nextUnix += oneDay
    dataFrame.loc[nextDate] = [np.nan for _ in range(len(dataFrame.columns)-1)] + [i]


dataFrame['Adj. Close'].plot()
dataFrame['Forecast'].plot()
plt.legend(loc=4)
plt.xlabel('Date')
plt.ylabel('Price')

plt.show()
