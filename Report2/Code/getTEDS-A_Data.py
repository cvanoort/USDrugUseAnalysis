import csv
import gc

# A small function for grabbing data from a list of dictionaries based on a shared key
def countKey(key,listDataDicts):
    outDict = {}
    for row in listDataDicts:
        try:
            outDict[row[key]] += 1

        except KeyError:
            outDict[row[key]] = 1

    return outDict


filePath1 = "data/TEDS-A_1992-2012/DS000"
filePath2 = [ "1", "2", "3", "4", "5" ]
filePath3 = "/25221-000"
filePath4 = "-Data.tsv"


# Dictionaries to hold data
alcData = {}
mjData = {}
cocData = {}
heroinData = {}
halData = {}
inhData = {}
prData = {}
tranqData = {}
stimData = {}
sedData = {}


for i in range(5):
    # Simple progress tracking
    print "Beginning loop iteration %d \n" %(i)

    # Create a path to a data set
    path = filePath1 + filePath2[i] + filePath3 + filePath2[i] + filePath4

    # Some keys to data of interest
    keys = []

    # Read that data set into a python object
    with open(path, 'r') as tsvFile:
        tsvReader = csv.DictReader(tsvFile,delimiter='\t')
        for row in tsvReader:
            if (int(row['SUB1']) == 2):
                try:
                    alcData[row['YEAR']] += 1

                except:
                    alcData[row['YEAR']] = 1

            if (int(row['SUB1']) == 3):
                try:
                    cocData[row['YEAR']] += 1

                except:
                    cocData[row['YEAR']] = 1

            if (int(row['SUB1']) == 4):
                try:
                    mjData[row['YEAR']] += 1

                except:
                    mjData[row['YEAR']] = 1

            if (int(row['SUB1']) == 5):
                try:
                    heroinData[row['YEAR']] += 1

                except:
                    heroinData[row['YEAR']] = 1

            if (int(row['SUB1']) == 6) or (int(row['SUB1']) == 7):
                try:
                    prData[row['YEAR']] += 1

                except:
                    prData[row['YEAR']] = 1

            if (int(row['SUB1']) == 8) or (int(row['SUB1']) == 9):
                try:
                    halData[row['YEAR']] += 1

                except:
                    halData[row['YEAR']] = 1

            if (int(row['SUB1']) == 10) or (int(row['SUB1']) == 11) or (int(row['SUB1']) == 12):
                try:
                    stimData[row['YEAR']] += 1

                except:
                    stimData[row['YEAR']] = 1

            if (int(row['SUB1']) == 13) or (int(row['SUB1']) == 14):
                try:
                    tranqData[row['YEAR']] += 1

                except:
                    tranqData[row['YEAR']] = 1

            if (int(row['SUB1']) == 15) or (int(row['SUB1']) == 16):
                try:
                    sedData[row['YEAR']] += 1

                except:
                    sedData[row['YEAR']] = 1

            if (int(row['SUB1']) == 17):
                try:
                    inhData[row['YEAR']] += 1

                except:
                    inhData[row['YEAR']] = 1

    # Clean up the data objects from the prvious iteration in order to decrease memory usage
    gc.collect()


    # Simple progress tracking
    print "Loop iteration %d complete! \n" %(i)


# Write the data to a smaller tsv file for later use
with open("TEDS-A_data.tsv", 'w') as outFile:
    csvWriter = csv.writer(outFile, delimiter='\t')

    years = [x for x in range(1992, 2013)]

    drugData = [alcData, mjData, cocData, heroinData, halData, inhData, prData, tranqData, stimData, sedData]

    csvWriter.writerow( years )

    for i in drugData:
        xdata = i.keys()
        xdata = [int(x) for x in xdata]

        ydata = i.values()

        zipped = zip(xdata, ydata)
        zipped.sort()

        xdata, ydata = zip(*zipped)

        csvWriter.writerow( ydata )