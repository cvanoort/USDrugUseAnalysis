import matplotlib.pyplot as plt
import csv


listDataLists = []

with open("QDU_data.tsv", 'r') as tsvFile:
        tsvReader = csv.reader(tsvFile,delimiter='\t')
        for row in tsvReader:
            listDataLists.append(row)

cigData = [int(x) for x in listDataLists[1]]
snuffData = [int(x) for x in listDataLists[2]]
cigarData = [int(x) for x in listDataLists[3]]
alcData = [int(x) for x in listDataLists[4]]
mjData = [int(x) for x in listDataLists[5]]
cocData = [int(x) for x in listDataLists[6]]
heroinData = [int(x) for x in listDataLists[7]]
halData = [int(x) for x in listDataLists[8]]
inhData = [int(x) for x in listDataLists[9]]
prData = [int(x) for x in listDataLists[10]]
tranqData = [int(x) for x in listDataLists[11]]
stimData = [int(x) for x in listDataLists[12]]
sedData = [int(x) for x in listDataLists[13]]


# Plot the data for 2002-2013
xdata = [x for x in range(2002,2014)]

plt.plot(xdata, cigData, '-or', xdata, snuffData, '-sg', xdata, cigarData, '-xb', xdata, alcData, '-ok',
         xdata, mjData, '-sm', xdata, cocData, '-xr', xdata, heroinData, '-og', xdata, halData, '-sb',
         xdata, inhData, '-xk', xdata, prData, '-om', xdata, tranqData, '-sr', xdata, stimData, '-xg',
         xdata, sedData, '-sb')

plt.title("Quantity of Drug Users From 2002-2013 By Drug")
plt.xlabel("Year")
plt.ylabel("Frequency of Drug Use Inception")
plt.legend(["Cigarette", "Snuff", "Cigar", "Alcohol", "Marijuana", "Cocaine", "Heroin", "Hallucinogens", "Inhalants", "Pain Relievers", "Tranquilizers", "Stimulants", "Sedatives"])
plt.xlim(2001, 2019)

plt.tight_layout()
plt.show()