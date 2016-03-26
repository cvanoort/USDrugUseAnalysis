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

# Now looking at the drug first use on a per month basis

cigMonths = countKey("CIGMFU", listDataDicts)

snuffMonths = countKey("SNUFMFU", listDataDicts)

chewMonths = countKey("CHEWMFU", listDataDicts)

cigarMonths = countKey("CIGARMFU", listDataDicts)

alcMonths = countKey("ALCMFU", listDataDicts)

mjMonths = countKey("MJMFU", listDataDicts)

cocMonths = countKey("COCMFU", listDataDicts)

heroinMonths = countKey("HERMFU", listDataDicts)

halMonths = countKey("HALMFU", listDataDicts)

inhMonths = countKey("INHMFU", listDataDicts)

prMonths = countKey("ANALMFU", listDataDicts)

tranqMonths = countKey("TRANMFU", listDataDicts)

stimMonths = countKey("STIMMFU", listDataDicts)

sedMonths = countKey("SEDMFU", listDataDicts)

january = cigMonths["1"]+snuffMonths["1"]+chewMonths["1"]+cigarMonths["1"]+alcMonths["1"]+mjMonths["1"]+cocMonths["1"]+heroinMonths["1"]+halMonths["1"]+inhMonths["1"]+prMonths["1"]+tranqMonths["1"]+stimMonths["1"]+sedMonths["1"]
february = cigMonths["2"]+snuffMonths["2"]+chewMonths["2"]+cigarMonths["2"]+alcMonths["2"]+mjMonths["2"]+cocMonths["2"]+heroinMonths["2"]+halMonths["2"]+inhMonths["2"]+prMonths["2"]+tranqMonths["2"]+stimMonths["2"]+sedMonths["2"]
march =  cigMonths["3"]+snuffMonths["3"]+chewMonths["3"]+cigarMonths["3"]+alcMonths["3"]+mjMonths["3"]+cocMonths["3"]+heroinMonths["3"]+halMonths["3"]+inhMonths["3"]+prMonths["3"]+tranqMonths["3"]+stimMonths["3"]+sedMonths["3"]
april = cigMonths["4"]+snuffMonths["4"]+chewMonths["4"]+cigarMonths["4"]+alcMonths["4"]+mjMonths["4"]+cocMonths["4"]+heroinMonths["4"]+halMonths["4"]+inhMonths["4"]+prMonths["4"]+tranqMonths["4"]+stimMonths["4"]+sedMonths["4"]
may = cigMonths["5"]+snuffMonths["5"]+chewMonths["5"]+cigarMonths["5"]+alcMonths["5"]+mjMonths["5"]+cocMonths["5"]+heroinMonths["5"]+halMonths["5"]+inhMonths["5"]+prMonths["5"]+tranqMonths["5"]+stimMonths["5"]+sedMonths["5"]
june = cigMonths["6"]+snuffMonths["6"]+chewMonths["6"]+cigarMonths["6"]+alcMonths["6"]+mjMonths["6"]+cocMonths["6"]+heroinMonths["6"]+halMonths["6"]+inhMonths["6"]+prMonths["6"]+tranqMonths["6"]+stimMonths["6"]+sedMonths["6"]
july = cigMonths["7"]+snuffMonths["7"]+chewMonths["7"]+cigarMonths["7"]+alcMonths["7"]+mjMonths["7"]+cocMonths["7"]+heroinMonths["7"]+halMonths["7"]+inhMonths["7"]+prMonths["7"]+tranqMonths["7"]+stimMonths["7"]+sedMonths["7"]
august = cigMonths["8"]+snuffMonths["8"]+chewMonths["8"]+cigarMonths["8"]+alcMonths["8"]+mjMonths["8"]+cocMonths["8"]+heroinMonths["8"]+halMonths["8"]+inhMonths["8"]+prMonths["8"]+tranqMonths["8"]+stimMonths["8"]+sedMonths["8"]
september = cigMonths["9"]+snuffMonths["9"]+chewMonths["9"]+cigarMonths["9"]+alcMonths["9"]+mjMonths["9"]+cocMonths["9"]+heroinMonths["9"]+halMonths["9"]+inhMonths["9"]+prMonths["9"]+tranqMonths["9"]+stimMonths["9"]+sedMonths["9"]
october = cigMonths["10"]+snuffMonths["10"]+chewMonths["10"]+cigarMonths["10"]+alcMonths["10"]+mjMonths["10"]+cocMonths["10"]+heroinMonths["10"]+halMonths["10"]+inhMonths["10"]+prMonths["10"]+tranqMonths["10"]+stimMonths["10"]+sedMonths["10"]
november = cigMonths["11"]+snuffMonths["11"]+chewMonths["11"]+cigarMonths["11"]+alcMonths["11"]+mjMonths["11"]+cocMonths["11"]+heroinMonths["11"]+halMonths["11"]+inhMonths["11"]+prMonths["11"]+tranqMonths["11"]+stimMonths["11"]+sedMonths["11"]
december = cigMonths["12"]+snuffMonths["12"]+chewMonths["12"]+cigarMonths["12"]+alcMonths["12"]+mjMonths["12"]+cocMonths["12"]+heroinMonths["12"]+halMonths["12"]+inhMonths["12"]+prMonths["12"]+tranqMonths["12"]+stimMonths["12"]+sedMonths["12"]

ydata = [january,february,march,april,may,june,july,august,september,october,november,december]
xLabels = ["January","February", "March","April","May", "June","July","August","September","October","November","December"]


#normalize the data
total = 0
for month in ydata:
	total += month

normed = [x/total for x in ydata]

#KS-Test
D,pVal = stats.kstest(normed, 'uniform')
critVal = .05

if pVal< critVal :
	print "The data is statistically signficant (p < %0.4f) in its variation from the uniform distribution (Two Sided KS-Test, statistic = %f, p-value = %f)" %(critVal,D,pVal)

else:
	print "The data is not statistically signficant (p >= %0.4f) in its variation from the uniform distribution (Two Sided KS-Test, statistic = %f, p-value = %f)" %(critVal,D,pVal)


#Mann-Whitney U-Test
U,pVal2 = stats.mannwhitneyu(normed, stats.uniform.rvs(size=12))

if pVal2< critVal :
	print "\n The data is statistically signficant (p < %0.4f) in its variation from the uniform distribution (Two Sided Mann-Whitney U-Test, statistic = %f, p-value = %f) \n" %(critVal,U,2*pVal2)

else:
	print "The data is not statistically signficant (p >= %0.4f) in its variation from the uniform distribution (Two Sided Mann-Whitney U-Test, statistic = %f, p-value = %f) \n" %(critVal,U,2*pVal2)


plt.bar(range(len(ydata)), ydata)
plt.title("Month Popularity by Drug Use Inception")
plt.xlabel("Month")
plt.ylabel("Frequency of Drug Use Inception")
plt.xticks([x+.4 for x in range(len(xLabels))], xLabels)
plt.xticks(rotation=50)
plt.tight_layout()
plt.show()