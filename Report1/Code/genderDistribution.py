import csv
import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as stats

def countKey(key,listDataDicts):
    outDict = {}
    for row in listDataDicts:
        try:
            outDict[row[key]] += 1

        except KeyError:
            outDict[row[key]] = 1

    return outDict

listDataDicts = []
with open('34933-0001-Data.tsv', 'r') as tsvFile:
	tsvReader = csv.DictReader(tsvFile,delimiter='\t')
	for row in tsvReader:
		listDataDicts.append(row)

# First lets look at the gender distribution of the data
genders = countKey('IRSEX',listDataDicts)

print genders["1"], genders["2"]

ydata = genders.values()
xLabels = ["Male", "Female"]


zipped = zip(ydata,xLabels)
zipped.sort(reverse=True)
ydata,xLabels = zip(*zipped)


plt.bar(range(len(ydata)) ,ydata)
plt.title("Gender Distribution")
plt.xlabel("Gender")
plt.ylabel("Frequency")
plt.xticks( [x + .4 for x in range(len(xLabels))], xLabels )
plt.tight_layout()
plt.show()