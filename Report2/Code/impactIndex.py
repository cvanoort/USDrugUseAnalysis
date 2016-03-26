import matplotlib.pyplot as plt
import csv


# Read data into a python object
listDataLists1 = []
listDataLists2 = []
listDataLists3 = []

with open("QDU_data.tsv", 'r') as tsvFile:
    tsvReader = csv.reader(tsvFile,delimiter='\t')
    for row in tsvReader:
        listDataLists1.append(row)

with open("DAWN_data.tsv", 'r') as tsvFile:
    tsvReader = csv.reader(tsvFile,delimiter='\t')
    for row in tsvReader:
        listDataLists2.append(row)

with open("TEDS-A_data.tsv", 'r') as tsvFile:
    tsvReader = csv.reader(tsvFile,delimiter='\t')
    for row in tsvReader:
        listDataLists3.append(row)

# Divide up the data into plotting groups
alcData = [int(x) for x in listDataLists1[4]]
alcData = alcData[2:-2]

mjData = [int(x) for x in listDataLists1[5]]
mjData =  mjData[2:-2]

cocData = [int(x) for x in listDataLists1[6]]
cocData = cocData[2:-2]

heroinData = [int(x) for x in listDataLists1[7]]
heroinData = heroinData[2:-2]

halData = [int(x) for x in listDataLists1[8]]
halData = halData[2:-2]

inhData = [int(x) for x in listDataLists1[9]]
inhData = inhData[2:-2]

prData = [int(x) for x in listDataLists1[10]]
prData = prData[2:-2]

tranqData = [int(x) for x in listDataLists1[11]]
tranqData = tranqData[2:-2]

stimData = [int(x) for x in listDataLists1[12]]
stimData = stimData[2:-2]

sedData = [int(x) for x in listDataLists1[13]]
sedData = sedData[2:-2]

xdata = listDataLists2[0]
xdata = [int(x) for x in xdata]

eAlcData = listDataLists2[1]
eAlcData = [int(x) for x in eAlcData]

eNonAlcIllicitData = listDataLists2[2]
eNonAlcIllicitData = [int(x) for x in eNonAlcIllicitData]

eNonMedPharmaData = listDataLists2[3]
eNonMedPharmaData = [int(x) for x in eNonMedPharmaData]


recAlcData = listDataLists3[1]
recAlcData = recAlcData[12:-1]
recAlcData = [int(x) for x in recAlcData]

recMjData = listDataLists3[2]
recMjData = recMjData[12:-1]
recMjData = [int(x) for x in recMjData]

recCocData = listDataLists3[3]
recCocData = recCocData[12:-1]
recCocData = [int(x) for x in recCocData]

recHeroinData = listDataLists3[4]
recHeroinData = recHeroinData[12:-1]
recHeroinData = [int(x) for x in recHeroinData]

recHalData = listDataLists3[5]
recHalData = recHalData[12:-1]
recHalData = [int(x) for x in recHalData]

recInhData = listDataLists3[6]
recInhData =recInhData[12:-1]
recInhData = [int(x) for x in recInhData]

recPrData = listDataLists3[7]
recPrData = recPrData[12:-1]
recPrData = [int(x) for x in recPrData]

recTranqData = listDataLists3[8]
recTranqData = recTranqData[12:-1]
recTranqData = [int(x) for x in recTranqData]

recStimData = listDataLists3[9]
recStimData = recStimData[12:-1]
recStimData = [int(x) for x in recStimData]

recSedData = listDataLists3[10]
recSedData = recSedData[12:-1]
recSedData = [int(x) for x in recSedData]

dawnAnnualTotal = [168841, 268128, 269339, 300983, 351697, 380125, 304110, 229211]
tedsAnnualTotal = [1807974, 1895348, 1959942, 1965194, 2054998, 2038465, 1925345, 1928675]

# Calculate impact values for each drug
for i in range(len(xdata)):
	alcData[i] = alcData[i] * (float(recAlcData[i])/tedsAnnualTotal[i]) * (float(eAlcData[i])/dawnAnnualTotal[i])
	
	mjData[i] = mjData[i] * (float(recMjData[i])/tedsAnnualTotal[i]) * (float(eNonAlcIllicitData[i])/dawnAnnualTotal[i])
	
	cocData[i] = cocData[i] * (float(recCocData[i])/tedsAnnualTotal[i]) * (float(eNonAlcIllicitData[i])/dawnAnnualTotal[i])
	
	heroinData[i] = heroinData[i] * (float(recHeroinData[i])/tedsAnnualTotal[i]) * (float(eNonAlcIllicitData[i])/dawnAnnualTotal[i])
	
	halData[i] = halData[i] * (float(recHalData[i])/tedsAnnualTotal[i]) * (float(eNonAlcIllicitData[i])/dawnAnnualTotal[i])

	inhData[i] = inhData[i] * (float(recInhData[i])/tedsAnnualTotal[i]) * (float(eNonAlcIllicitData[i])/dawnAnnualTotal[i])

	prData[i] = prData[i] * (float(recPrData[i])/tedsAnnualTotal[i]) * (float(eNonMedPharmaData[i])/dawnAnnualTotal[i])

	tranqData[i] = tranqData[i] * (float(recTranqData[i])/tedsAnnualTotal[i]) * (float(eNonMedPharmaData[i])/dawnAnnualTotal[i])

	stimData[i] = stimData[i] * (float(recStimData[i])/tedsAnnualTotal[i]) * (float(eNonMedPharmaData[i])/dawnAnnualTotal[i])

	sedData[i] = sedData[i] * (float(recSedData[i])/tedsAnnualTotal[i]) * (float(eNonMedPharmaData[i])/dawnAnnualTotal[i])


plt.plot(xdata, alcData, '-ok', xdata, mjData, '-sm', xdata, cocData, '-xr', xdata, heroinData, '-og',
		 xdata, halData, '-sb', xdata, inhData, '-xk', xdata, prData, '-om', xdata, tranqData, '-sr',
		 xdata, stimData, '-xg', xdata, sedData, '-sb')

plt.title("Drug Impacts In The US From 2004-2011")
plt.xlabel("Year")
plt.ylabel("Impact Index Value")
plt.legend(["Alcohol", "Marijuana", "Cocaine", "Heroin", "Hallucinogens", "Inhalants", "Pain Relievers", "Tranquilizers", "Stimulants", "Sedatives"])
plt.xlim(2003, 2015)

plt.tight_layout()
plt.show()