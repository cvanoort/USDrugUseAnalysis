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

# Some lists to hold plotting data
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

    # Drug popularity by number of people who have ever used it
    # Cigarettes
    cigEver = countKey("CIGEVER", listDataDicts)
    cigData.append(cigEver["1"])

    # Snuff
    snuffEver = countKey("SNFEVER", listDataDicts)
    snuffData.append(snuffEver["1"])

    #Cigar
    cigarEver = countKey("CIGAREVR", listDataDicts)
    cigarData.append(cigarEver["1"])

    # Alcohol
    alcEver = countKey("ALCEVER", listDataDicts)
    alcData.append(alcEver["1"])

    # Marijuana
    mjEver = countKey("MJEVER", listDataDicts)
    mjData.append(mjEver["1"])

    # Cocaine
    cocEver = countKey("COCEVER", listDataDicts)
    cocData.append(cocEver["1"])

    # Heroin
    heroinEver = countKey("HEREVER", listDataDicts)
    heroinData.append(heroinEver["1"])

    #Hallucinogens
    lsdEver = countKey("LSD", listDataDicts)
    pcpEver = countKey("PCP", listDataDicts)
    peyoteEver = countKey("PEYOTE", listDataDicts)
    mescalineEver = countKey("MESC", listDataDicts)
    shroomsEver = countKey("PSILCY", listDataDicts)
    ecstasyEver = countKey("ECSTASY", listDataDicts)
    otherHalEver = countKey("HALNOLST", listDataDicts)
    
    halTot = lsdEver["1"]+pcpEver["1"]+peyoteEver["1"]+mescalineEver["1"]+shroomsEver["1"]+ecstasyEver["1"]+otherHalEver["1"]
    halData.append(halTot)

    #Inhalants
    etherEver = countKey("ETHER", listDataDicts)
    solventEver = countKey("SOLVENT", listDataDicts)
    lighterGasEver = countKey("LGAS", listDataDicts)
    nitOxEver = countKey("NITOXID", listDataDicts)
    sPaintEver = countKey("SPPAINT", listDataDicts)
    aeroEver = countKey("AEROS", listDataDicts)
    otherInhEver = countKey("INHNOLST", listDataDicts)
    
    inhTot = etherEver["1"]+solventEver["1"]+lighterGasEver["1"]+nitOxEver["1"]+sPaintEver["1"]+aeroEver["1"]+otherInhEver["1"]
    inhData.append(inhTot)

    # Pain Relievers
    darvosetEver = countKey("DARVTYLC", listDataDicts)
    percocetEver = countKey("PERCTYLX", listDataDicts)
    vicodinEver = countKey("VICOLOR", listDataDicts)
    painRAssortEver = countKey("ANLCARD", listDataDicts)
    painROtherEver = countKey("ANLNOLST", listDataDicts)
   
    prTot = darvosetEver["1"]+percocetEver["1"]+vicodinEver["1"]+painRAssortEver["1"]+painROtherEver["1"]
    prData.append(prTot)

    # Tranquilizers
    klonopinEver = countKey("KLONOPIN", listDataDicts)
    xanaxEver = countKey("XNAXATVN", listDataDicts)
    valiumEver = countKey("VALMDIAZ", listDataDicts)
    tranqAssorEver = countKey("TRNCARD", listDataDicts)
    tranqOtherEver = countKey("TRNOLST", listDataDicts)

    tranqTot = klonopinEver["1"]+xanaxEver["1"]+valiumEver["1"]+tranqAssorEver["1"]+tranqOtherEver["1"]
    tranqData.append(tranqTot)
    
    # Stimulants
    methEver = countKey("METHDES", listDataDicts)
    amphEver = countKey("DIETPILS", listDataDicts)
    ritalinEver = countKey("RITMPHEN", listDataDicts)
    stimAssortEver = countKey("STMCARD", listDataDicts)
    stimOtherEver = countKey("STMNOLST", listDataDicts)

    stimTot = methEver["1"]+amphEver["1"]+ritalinEver["1"]+stimAssortEver["1"]+stimOtherEver["1"]
    stimData.append(stimTot)

    # Sedatives
    quaaludeEver = countKey("METHAQ", listDataDicts)
    barbEver = countKey("NEMBBARB", listDataDicts)
    restorilEver = countKey("RESTTMAZ", listDataDicts)
    sedAssortEver = countKey("SEDCARD", listDataDicts)
    sedOtherEver = countKey("SEDNOLST", listDataDicts)

    sedTot = quaaludeEver["1"]+barbEver["1"]+restorilEver["1"]+sedAssortEver["1"]+sedOtherEver["1"]
    sedData.append(sedTot)

    # Forced garbage collection again
    gc.collect()

    # Simple progress tracking
    print "Loop iteration %d complete! \n" %(i)


# Write the data to a smaller tsv file for later use
with open("QDU_data.tsv", 'w') as outFile:
    csvWriter = csv.writer(outFile, delimiter='\t')

    years = [x for x in range(2002, 2014)]

    drugData = [cigData, snuffData, cigarData, alcData, mjData, cocData, heroinData, halData, inhData, prData, tranqData, stimData, sedData]

    csvWriter.writerow( years )

    for i in range(len(drugData)):
        csvWriter.writerow( drugData[i] )