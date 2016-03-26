import csv
import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as stats


def mean(data):
	total = 0
	count = 0
	for element in data:
		total += element
		count +=1

	return (total/count)


def median(data):
	if len(data)%2 == 1:
		return data[(len(data)-1)/2]

	else:
		return mean([data[(len(data)/2)],data[(len(data)/2)-1]])


def countKey(key,listDataDicts):
	outDict = {}
	for row in listDataDicts:
		try:
			outDict[row[key]] += 1

		except KeyError:
			outDict[row[key]] = 1

	return outDict


def compileKey(key, listDataDicts, outList):
	for row in listDataDicts:
		outList.append(row[key])

	return outList


def combineDicts(dict1, dict2):
	for key in dict1.keys():
		if key in dict2:
			dict2[key] += dict1[key]

		else:
			dict2[key] = dict1[key]

	return dict2


listDataDicts = []
with open('34933-0001-Data.tsv', 'r') as tsvFile:
	tsvReader = csv.DictReader(tsvFile,delimiter='\t')
	for row in tsvReader:
		listDataDicts.append(row)

#An Age of First Use plot for all of the drugs in the study
totalAFU = {}
listAFU = []


# Cigarettes
cigAFU = countKey("CIGTRY", listDataDicts)
totalAFU = combineDicts(cigAFU, totalAFU)
listAFU = compileKey("CIGTRY", listDataDicts, listAFU)

# Snuff
snuffAFU = countKey("SNUFTRY", listDataDicts)
totalAFU = combineDicts(snuffAFU, totalAFU)
listAFU = compileKey("SNUFTRY", listDataDicts, listAFU)


#Chew
chewAFU = countKey("CHEWTRY", listDataDicts)
totalAFU = combineDicts(chewAFU, totalAFU)
listAFU = compileKey("CHEWTRY", listDataDicts, listAFU)


#Cigar
cigarAFU = countKey("CIGARTRY", listDataDicts)
totalAFU = combineDicts(cigarAFU, totalAFU)
listAFU = compileKey("CIGARTRY", listDataDicts, listAFU)


# Alcohol
alcAFU = countKey("ALCTRY", listDataDicts)
totalAFU = combineDicts(alcAFU, totalAFU)
listAFU = compileKey("ALCTRY", listDataDicts, listAFU)


# Marijuana
mjAFU = countKey("MJAGE", listDataDicts)
totalAFU = combineDicts(mjAFU, totalAFU)
listAFU = compileKey("MJAGE", listDataDicts, listAFU)


# Cocaine
cocAFU = countKey("COCAGE", listDataDicts)
totalAFU = combineDicts(cocAFU, totalAFU)
listAFU = compileKey("COCAGE", listDataDicts, listAFU)


# Heroin
heroinAFU = countKey("HERAGE", listDataDicts)
totalAFU = combineDicts(heroinAFU, totalAFU)
listAFU = compileKey("HERAGE", listDataDicts, listAFU)


#Hallucinogens
hallAFU = countKey("HALLAGE", listDataDicts)
totalAFU = combineDicts(hallAFU, totalAFU)
listAFU = compileKey("HALLAGE", listDataDicts, listAFU)


#Inhalants
inhAFU = countKey("INHAGE", listDataDicts)
totalAFU = combineDicts(inhAFU, totalAFU)
listAFU = compileKey("INHAGE", listDataDicts, listAFU)


# Pain Relievers
PRAFU = countKey("ANALAGE", listDataDicts)
totalAFU = combineDicts(PRAFU, totalAFU)
listAFU = compileKey("ANALAGE", listDataDicts, listAFU)


# Tranquilizers
tranqAFU = countKey("TRANAGE", listDataDicts)
totalAFU = combineDicts(tranqAFU, totalAFU)
listAFU = compileKey("TRANAGE", listDataDicts, listAFU)


# Stimulants
stimAFU = countKey("STIMAGE", listDataDicts)
totalAFU = combineDicts(stimAFU, totalAFU)
listAFU = compileKey("STIMAGE", listDataDicts, listAFU)


# Sedatives
sedAFU = countKey("SEDAGE", listDataDicts)
totalAFU = combineDicts(sedAFU, totalAFU)
listAFU = compileKey("SEDAGE", listDataDicts, listAFU)


# prepare the data for graphing
xdata = totalAFU.keys()
xdata = [int(x) for x in xdata]

ydata = totalAFU.values()
ydata = [int(y) for y in ydata]

# Sort the data
zipped = zip(xdata,ydata)
zipped.sort()
xdata,ydata = zip(*zipped)

xdata = list(xdata)
ydata = list(ydata)

# remove the data related to special codes
xdata = xdata[:-6]
ydata = ydata[:-6]

# plot the data
plt.bar(xdata, ydata)
plt.title("Age of First Use Distribution")
plt.xlabel("Age")
plt.ylabel("Frequency")
plt.tight_layout()
plt.show()

#Compute the mean and median
listAFU = [int(x) for x in listAFU if int(x)<100]

listAFU.sort()

print "The mean age of first use for all drugs in the survey is %d and the median is %d." %(mean(listAFU) , median(listAFU))
