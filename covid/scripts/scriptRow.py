import csv
from matplotlib import pyplot as plt
import numpy as np
import random

f = open('../COVID-19/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_deaths_global.csv')
csv_f = csv.reader(f)

dataX = []
dataY = []

dataY_scaleFactor = []
dataX_scaleFactor = []

# add some multiple of one array to another (append natural numbers)
def arrayLength(length):
    array = []
    j = 0
    for i in range (0, length):
        if (i%4 == 0):
            array.append(i)
  
    array.pop()
    return array

#add some multiple of one array to another (append the array number equivalent to multiple)
def brokeTenStrings(array):
    brokenArray = []
    for i in range(0, len(array)):
        if (i) % 4 == 0:
            brokenArray.append(array[i])
    return brokenArray


def getCovidDataScale():

    brokenTenStringsA = []

    for row in csv_f:
        if (row[1] == 'Italy'):
            brokenTenStringsA = brokeTenStrings(row[4:len(row)])
            dataY_scaleFactor.append(brokenTenStringsA)
            dataX_scaleFactor.append(arrayLength(len(row)))

def getCovidData():
    for row in csv_f:
        if (row[1] == 'Brazil'):
            dataY.append(row[4:len(row)])
            dataX.append(arrayLength(len(row)-4))

def arrayToExp(array):
    dataX_exp = []
    for i in range(0, len(array)):
        dataX_exp.append(np.exp(int(array[i])))

    return dataX_exp



#getCovidData()
getCovidDataScale()

print(dataX_scaleFactor)
print(dataY_scaleFactor)

plt.plot(dataX_scaleFactor[0], dataY_scaleFactor[0])


plt.show()
