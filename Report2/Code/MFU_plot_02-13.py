import matplotlib.pyplot as plt
import csv

listDataLists = []

with open("MFU_data.tsv", 'r') as tsvFile:
        tsvReader = csv.reader(tsvFile,delimiter='\t')
        for row in tsvReader:
            listDataLists.append(row)

janData = [int(x) for x in listDataLists[1]]
febData = [int(x) for x in listDataLists[2]]
marData = [int(x) for x in listDataLists[3]]
aprData = [int(x) for x in listDataLists[4]]
mayData = [int(x) for x in listDataLists[5]]
junData = [int(x) for x in listDataLists[6]]
julData = [int(x) for x in listDataLists[7]]
augData = [int(x) for x in listDataLists[8]]
septData = [int(x) for x in listDataLists[9]]
octData = [int(x) for x in listDataLists[10]]
novData = [int(x) for x in listDataLists[11]]
decData = [int(x) for x in listDataLists[12]]


# Plot the data for 2002-2013
xdata = [x for x in range(2002,2014)]

plt.plot(xdata, janData, '-r', xdata, febData, '-b', xdata, marData, '-b', xdata, aprData, '-b',
         xdata, mayData, '-b', xdata, junData, '-xr', xdata, julData, '-sr', xdata, augData, '-b',
         xdata, septData, '-b', xdata, octData, '-b', xdata, novData, '-b', xdata, decData, '-b')

plt.title("Monthly Drug Use Inception From 2002-2013")
plt.xlabel("Year")
plt.ylabel("Frequency of Drug Use Inception")
plt.legend(['January', 'February', 'March' , 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'])
plt.xlim(2001, 2019)

plt.tight_layout()
plt.show()