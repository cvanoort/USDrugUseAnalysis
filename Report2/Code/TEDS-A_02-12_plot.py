import matplotlib.pyplot as plt
import csv


# Read that data set into a python object
listDataLists = []
with open("TEDS-A_data.tsv", 'r') as tsvFile:
    tsvReader = csv.reader(tsvFile,delimiter='\t')
    for row in tsvReader:
        listDataLists.append(row)

# Plot the data for 1992-2012
xdata = listDataLists[0]
alcData = listDataLists[1]
mjData = listDataLists[2]
cocData = listDataLists[3]
heroinData = listDataLists[4]
halData = listDataLists[5]
inhData = listDataLists[6]
prData = listDataLists[7]
tranqData = listDataLists[8]
stimData = listDataLists[9]
sedData = listDataLists[10]

plt.plot(xdata, alcData, '-sk', xdata, mjData, '-sm', xdata, cocData, '-xr', xdata, heroinData, '-og', 
         xdata, halData, '-sb', xdata, inhData, '-xk', xdata, prData, '-ok', xdata, tranqData, '-sr',
         xdata, stimData, '-xg', xdata, sedData, '-sb')

plt.title("Recovery Service Useage 1992-2012 By Drug")
plt.xlabel("Year")
plt.ylabel("Frequency of Recovery Service Usage")
plt.legend(["Alcohol", "Marijuana", "Cocaine", "Heroin", "Hallucinogens", "Inhalants", "Pain Relievers", "Tranquilizers", "Stimulants", "Sedatives"])
plt.xlim(1990, 2025)

plt.tight_layout()
plt.show()