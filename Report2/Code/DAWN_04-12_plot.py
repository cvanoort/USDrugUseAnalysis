import matplotlib.pyplot as plt
import csv


# Read that data set into a python object
listDataLists = []
with open("DAWN_data.tsv", 'r') as tsvFile:
    tsvReader = csv.reader(tsvFile,delimiter='\t')
    for row in tsvReader:
        listDataLists.append(row)

# Plot the data for 2004-2012
xdata = listDataLists[0]
alcData = listDataLists[1]
nonAlcIllicitData = listDataLists[2]
nonMedPharmaData = listDataLists[3]

plt.plot(xdata, alcData, '-r', xdata, nonAlcIllicitData, '-g', xdata, nonMedPharmaData, '-b')

plt.title("Emergency Service Useage 2004-2012")
plt.xlabel("Year")
plt.ylabel("Frequency of Emergency Service Usage")
plt.legend(["Alcohol", "Illicit Drugs", "Non-Medical Pharmaceuticals"])
plt.xlim(2003, 2020)

plt.tight_layout()
plt.show()