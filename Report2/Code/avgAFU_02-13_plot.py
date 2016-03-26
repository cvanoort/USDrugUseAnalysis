import csv
import matplotlib.pyplot as plt


def countKey(key,listDataDicts):
    outDict = {}
    for row in listDataDicts:
        try:
            outDict[row[key]] += 1

        except KeyError:
            outDict[row[key]] = 1

    return outDict


listDataLists = []
with open('AFU_data.tsv', 'rb') as tsvFile:
    tsvReader = csv.reader(tsvFile,delimiter='\t')
    for row in tsvReader:
        listDataLists.append(row)

cigData = [float(x) for x in listDataLists[1]]
snuffData = [float(x) for x in listDataLists[2]]
cigarData = [float(x) for x in listDataLists[3]]
alcData = [float(x) for x in listDataLists[4]]
mjData = [float(x) for x in listDataLists[5]]
cocData = [float(x) for x in listDataLists[6]]
heroinData = [float(x) for x in listDataLists[7]]
halData = [float(x) for x in listDataLists[8]]
inhData = [float(x) for x in listDataLists[9]]
prData = [float(x) for x in listDataLists[10]]
tranqData = [float(x) for x in listDataLists[11]]
stimData = [float(x) for x in listDataLists[12]]
sedData = [float(x) for x in listDataLists[13]]


xdata = [x for x in range(2002,2014)]

plt.plot(xdata, cigData, '-or', xdata, snuffData, '-sg', xdata, cigarData, '-xb', xdata, alcData, '-ok',
         xdata, mjData, '-sm', xdata, cocData, '-xr', xdata, heroinData, '-og', xdata, halData, '-vm',
         xdata, inhData, '-xk', xdata, prData, '-om', xdata, tranqData, '-sr', xdata, stimData, '-xg',
         xdata, sedData, '-sb')

plt.title("Age Of First Use By Drug and Year")
plt.xlabel("Year")
plt.ylabel("Average Age Of First Use)")
plt.legend(["Cigarette", "Snuff", "Cigar", "Alcohol", "Marijuana", "Cocaine", "Heroin", "Hallucinogens", "Inhalants", "Pain Relievers", "Tranquilizers", "Stimulants", "Sedatives"])
plt.xlim(2001, 2019)
plt.tight_layout()
plt.show()