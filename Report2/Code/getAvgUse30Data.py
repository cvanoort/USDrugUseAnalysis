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

# A small function which calculates the average value of a key shared by multiple dictionaries
def avgUse30Days(key, listDataDicts):
    totalDays = 0
    numberUsers = 0
    for person in listDataDicts:
        if int(person[key]) < 31 :
            totalDays += int(person[key])
            numberUsers += 1

    return (1.0*totalDays/numberUsers)


# Some lists to hold data
cigData = []
snuffData = []
cigarData = []
alcData = []
mjData = []
cocData = []
heroinData = []
halData = []
inhData = []
prData = []
tranqData = []
stimData = []
sedData = []


filePath1 = "data/NSDUH_20"
filePath2 = ["02","03","04","05","06","07","08","09","10","11","12","13"]
filePath3 = "/DS0001/"
filePath4 = ["03903","04138","04373","04596","21240","23782","26701","29621","32722","34481","34933","35509"]
filePath5 = "-0001-Data.tsv"

for i in range(12):
    # Simple progress tracking
    print "Beginning loop iteration %d \n" %(i)

    # Create a path to a data set
    path = filePath1 + filePath2[i] + filePath3 + filePath4[i] + filePath5

    # Read that data set into a python object
    listDataDicts = []
    with open(path, 'r') as tsvFile:
        tsvReader = csv.DictReader(tsvFile,delimiter='\t')
        for row in tsvReader:
            listDataDicts.append(row)

    # Clean up the data objects from the prvious iteration in order to decrease memory usage
    gc.collect()

    cigData.append(avgUse30Days( 'CIG30USE' , listDataDicts ))
    snuffData.append(avgUse30Days( 'SNF30USE' , listDataDicts ))
    cigarData.append(avgUse30Days( 'CGR30USE' , listDataDicts ))
    alcData.append(avgUse30Days( 'ALCDAYS' , listDataDicts ))
    mjData.append(avgUse30Days( 'MJDAY30A' , listDataDicts ))
    cocData.append(avgUse30Days( 'COCUS30A' , listDataDicts ))
    heroinData.append(avgUse30Days( 'HER30USE' , listDataDicts ))
    halData.append(avgUse30Days( 'HAL30USE' , listDataDicts ))
    inhData.append(avgUse30Days( 'INHDY30A' , listDataDicts ))
    prData.append(avgUse30Days( 'PRDAYPMO' , listDataDicts ))
    tranqData.append(avgUse30Days( 'TRDAYPMO' , listDataDicts ))
    stimData.append(avgUse30Days( 'STDAYPMO' , listDataDicts ))
    sedData.append(avgUse30Days( 'SVDAYPMO' , listDataDicts ))

    # Forced garbage collection again
    gc.collect()

    # Simple progress tracking
    print "Loop iteration %d complete! \n" %(i)


# Write the data to a smaller tsv file for later use
with open("avgUse30_data.tsv", 'w') as outFile:
    csvWriter = csv.writer(outFile, delimiter='\t')

    years = [x for x in range(2002, 2014)]

    drugData = [cigData, snuffData, cigarData, alcData, mjData, cocData, heroinData, halData, inhData, prData, tranqData, stimData, sedData]

    csvWriter.writerow( years )

    for i in range(len(drugData)):
        csvWriter.writerow( drugData[i] )