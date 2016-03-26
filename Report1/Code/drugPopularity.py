import csv
import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as stats


def countKey(key,listDataDicts):
    outDict = {}
    for row in listDataDicts:
        try:
            outDict[row[key]] += 1

        except KeyError:
            outDict[row[key]] = 1

    return outDict

listDataDicts = []
with open('34933-0001-Data.tsv', 'r') as tsvFile:
    tsvReader = csv.DictReader(tsvFile,delimiter='\t')
    for row in tsvReader:
        listDataDicts.append(row)

# Drug popularity by number of people who have ever used it
drugUseEver = []
xLabels = []

# Cigarettes
cigEver = countKey("CIGEVER", listDataDicts)

drugUseEver.append(cigEver["1"])
xLabels.append("Cigarette")

# Snuff
snuffEver = countKey("SNFEVER", listDataDicts)

drugUseEver.append(snuffEver["1"])
xLabels.append("Snuff")

#Cigar
cigarEver = countKey("CIGAREVR", listDataDicts)

drugUseEver.append(cigarEver["1"])
xLabels.append("Cigar")

# Alcohol
alcEver = countKey("ALCEVER", listDataDicts)

drugUseEver.append(alcEver["1"])
xLabels.append("Alcohol")

# Marijuana
mjEver = countKey("MJEVER", listDataDicts)

drugUseEver.append(mjEver["1"])
xLabels.append("Marijuana")

# Cocaine
cocEver = countKey("COCEVER", listDataDicts)

drugUseEver.append(cocEver["1"])
xLabels.append("Cocaine")

# Heroin
heroinEver = countKey("HEREVER", listDataDicts)

drugUseEver.append(heroinEver["1"])
xLabels.append("Heroin")

#Hallucinogens
lsdEver = countKey("LSD", listDataDicts)
pcpEver = countKey("PCP", listDataDicts)
peyoteEver = countKey("PEYOTE", listDataDicts)
mescalineEver = countKey("MESC", listDataDicts)
shroomsEver = countKey("PSILCY", listDataDicts)
ecstasyEver = countKey("ECSTASY", listDataDicts)
otherHalEver = countKey("HALNOLST", listDataDicts)

halTot = lsdEver["1"]+pcpEver["1"]+peyoteEver["1"]+mescalineEver["1"]+shroomsEver["1"]+ecstasyEver["1"]+otherHalEver["1"]
drugUseEver.append(halTot)
xLabels.append("Hallucinogens")

#Inhalants
etherEver = countKey("ETHER", listDataDicts)
solventEver = countKey("SOLVENT", listDataDicts)
lighterGasEver = countKey("LGAS", listDataDicts)
nitOxEver = countKey("NITOXID", listDataDicts)
sPaintEver = countKey("SPPAINT", listDataDicts)
aeroEver = countKey("AEROS", listDataDicts)
otherInhEver = countKey("INHNOLST", listDataDicts)

inhTot = etherEver["1"]+solventEver["1"]+lighterGasEver["1"]+nitOxEver["1"]+sPaintEver["1"]+aeroEver["1"]+otherInhEver["1"]
drugUseEver.append(inhTot)
xLabels.append("Inhalants")

# Pain Relievers
darvosetEver = countKey("DARVTYLC", listDataDicts)
percocetEver = countKey("PERCTYLX", listDataDicts)
vicodinEver = countKey("VICOLOR", listDataDicts)
painRAssortEver = countKey("ANLCARD", listDataDicts)
painROtherEver = countKey("ANLNOLST", listDataDicts)

prTot = darvosetEver["1"]+percocetEver["1"]+vicodinEver["1"]+painRAssortEver["1"]+painROtherEver["1"]
drugUseEver.append(prTot)
xLabels.append("Pain Relievers")

# Tranquilizers
klonopinEver = countKey("KLONOPIN", listDataDicts)
xanaxEver = countKey("XNAXATVN", listDataDicts)
valiumEver = countKey("VALMDIAZ", listDataDicts)
tranqAssorEver = countKey("TRNCARD", listDataDicts)
tranqOtherEver = countKey("TRNOLST", listDataDicts)

tranqTot = klonopinEver["1"]+xanaxEver["1"]+valiumEver["1"]+tranqAssorEver["1"]+tranqOtherEver["1"]
drugUseEver.append(tranqTot)
xLabels.append("Tranquilizers")

# Stimulants
methEver = countKey("METHDES", listDataDicts)
amphEver = countKey("DIETPILS", listDataDicts)
ritalinEver = countKey("RITMPHEN", listDataDicts)
stimAssortEver = countKey("STMCARD", listDataDicts)
stimOtherEver = countKey("STMNOLST", listDataDicts)

stimTot = methEver["1"]+amphEver["1"]+ritalinEver["1"]+stimAssortEver["1"]+stimOtherEver["1"]
drugUseEver.append(stimTot)
xLabels.append("Stimulants")

# Sedatives
quaaludeEver = countKey("METHAQ", listDataDicts)
barbEver = countKey("NEMBBARB", listDataDicts)
restorilEver = countKey("RESTTMAZ", listDataDicts)
sedAssortEver = countKey("SEDCARD", listDataDicts)
sedOtherEver = countKey("SEDNOLST", listDataDicts)

sedTot = quaaludeEver["1"]+barbEver["1"]+restorilEver["1"]+sedAssortEver["1"]+sedOtherEver["1"]
drugUseEver.append(sedTot)
xLabels.append("Sedatives")

# Now lets make a bar chart to conveniently display this
zipped = zip(drugUseEver,xLabels)
zipped.sort(reverse=True)
drugUseEver,xLabels = zip(*zipped)


plt.bar(range(len(drugUseEver)), drugUseEver)
plt.title("Drug Popularity")
plt.xlabel("Drug")
plt.ylabel("Number of Users")
plt.xticks([x+.4 for x in range(len(xLabels))], xLabels)
plt.xticks(rotation=70)
plt.tight_layout()
plt.show()