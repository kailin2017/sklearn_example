from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn import preprocessing

from com.kailin.api_file import api_file
from com.kailin.api_image import api_image

import numpy


def dealwithX(dataX, day):
    tempA = []
    for i in range(day, len(dataX) - 1):
        tempB = []
        for j in range(day):
            tempB.append(dataX[i - day - 1 + j])
        tempA.append(tempB)
    return numpy.array(tempA)


def deakwithY(dataY, day):
    tempA = []
    for i in range(len(dataY) - 1 - day):
        tempB = []
        for j in range(day):
            tempB.append(dataY[i + j - 1])
        tempA.append(tempB)
    return tempA


closX = ['開盤', '最高', '最低', '成交量', '成交金額']
closY = ['收盤']

trainDay = 120
predictDay = 10

stockcode = '2330'
pathXlsx = api_file.dataPath + stockcode + '.xlsx'
stock = api_file.readExcel(pathXlsx)
stockNum = int(len(stock) * 0.8)
trainStock = stock[trainDay:stockNum - 1 - predictDay]
testStock = stock[stockNum - 1:len(stock) - 1 - predictDay]

trainX = dealwithX(trainStock[closX].values, trainDay)
trainY = deakwithY(trainStock[closY].values, predictDay)

testX = dealwithX(testStock[closX].values, trainDay)
testY = deakwithY(testStock[closY].values, predictDay)

print(testX)

model = LinearRegression()
model.fit(trainX, trainY)

print(model.score(testX, testY))

result = model.predict(testX)

for i in range(len(result)):
    print(result[i], testY[i])
