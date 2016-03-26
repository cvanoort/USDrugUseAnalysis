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

alcData = [0,0,0,0,0,0,0,0]
nonAlcIllicitData = [0,0,0,0,0,0,0,0]
nonMedPharmaData = [0,0,0,0,0,0,0,0]


filePath1 = "data/DAWN_20"
filePath2 = [ "04", "05", "06", "07", "08", "09", "10", "11" ]
filePath3 = "/DS0001/"
filePath4 = ["33041","33042","33221","32861","31264","31921","34083","34565"]
filePath5 = "-0001-Data.tsv"

for i in range(8):
    # Simple progress tracking
    print "Beginning loop iteration %d \n" %(i)

    # Create a path to a data set
    path = filePath1 + filePath2[i] + filePath3 + filePath4[i] + filePath5

    # Read that data set into a python object
    listDataDicts = []
    with open(path, 'r') as tsvFile:
        tsvReader = csv.DictReader(tsvFile,delimiter='\t')
        for row in tsvReader:
            if (row['ALCOHOL'] == "1"):
                    alcData[i] += 1     

            if (row['NONALCILL'] == "1"):
                    nonAlcIllicitData[i] += 1 

            if (row['NONMEDPHARMA'] == "1"):
                    nonMedPharmaData[i] += 1 

    # Clean up the data objects from the prvious iteration in order to decrease memory usage
    gc.collect()


    # Simple progress tracking
    print "Loop iteration %d complete! \n" %(i)

print alcData, "\n", nonAlcIllicitData, "\n", nonMedPharmaData, "\n"

# Write the data to a smaller tsv file for later use
with open("DAWN_data.tsv", 'w') as outFile:
    csvWriter = csv.writer(outFile, delimiter='\t')

    years = [x for x in range(2004, 2012)]

    drugData = [alcData, nonAlcIllicitData, nonMedPharmaData]

    csvWriter.writerow( years )

    for i in drugData:
        csvWriter.writerow( i )