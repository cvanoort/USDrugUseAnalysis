import csv
import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as stats
from scipy.optimize import curve_fit


def countKey(key,listDataDicts):
    outDict = {}
    for row in listDataDicts:
        try:
            outDict[row[key]] += 1

        except KeyError:
            outDict[row[key]] = 1

    return outDict


def avgUse30Days(key, listDataDicts):
    totalDays = 0
    numberUsers = 0
    for person in listDataDicts:
        if int(person[key]) < 31 :
            totalDays += int(person[key])
            numberUsers += 1

    return (1.0*totalDays/numberUsers)


def avgUse30DaysWithZeros(key, listDataDicts):
    totalDays = 0
    numberUsers = 0
    for person in listDataDicts:
        if ( int(person[key]) < 31 ):
            totalDays += int(person[key])
            numberUsers += 1

        elif ( int(person[key]) == 93 ):
            numberUsers += 1

        else:
            pass

    return (1.0*totalDays/numberUsers)

def powerLaw(x,a,b):
	return a*(x**(-b))

def expDecay(x,a,b):
	return a*np.exp(b*x)


listDataDicts = []
with open('34933-0001-Data.tsv', 'rb') as tsvFile:
    tsvReader = csv.DictReader(tsvFile,delimiter='\t')
    for row in tsvReader:
        listDataDicts.append(row)


ageFirstUseKeys = ['CIGTRY', 'SNUFTRY', 'CHEWTRY', 'CIGARTRY', 'ALCTRY', 'MJAGE', 'COCAGE', 'HERAGE', 'HALLAGE', 'INHAGE', 'ANALAGE', 'TRANAGE', 'STIMAGE', 'SEDAGE']
useLast30Keys = ['CIG30USE','SNF30USE','CHW30USE','CGR30USE','ALCDAYS','MJDAY30A','COCUS30A','HER30USE','HAL30USE','INHDY30A','PRDAYPMO','TRDAYPMO','STDAYPMO','SVDAYPMO']
xdata = []
ydata = []

for person in listDataDicts:
    for i in range(len(ageFirstUseKeys)):
        if (int(person[ageFirstUseKeys[i]]) < 900) and (int(person[useLast30Keys[i]]) < 31):
            xdata.append(int(person[ageFirstUseKeys[i]]))
            ydata.append(int(person[useLast30Keys[i]]))

slope,intercept,rValue,pValue,stdErr = stats.linregress(xdata,ydata)

print "Drug First Use Age vs Usage Frequency Linear Regression"
print "Slope: %f, Intercept: %f, RSQ-Value: %f, P-Value: %f, Standard Error: %f,\n 95%% Confidence Interval: %f +- %f\n" %(slope,intercept,rValue*rValue,pValue,stdErr, slope, 1.96*stdErr)


'''# Curve fit with a power law
xfit = range(90)

popt1, pcov1 = curve_fit(powerLaw, xdata, ydata)

print "Power Law Curve fit: ",popt1,np.sqrt(np.diag(pcov1)),"\n"

fitLiney1 = np.zeros(len(xfit))

for i in range(len(xfit)):
	fitLiney1[i] = powerLaw( xfit[i], popt1[0], popt1[1] )
'''

xdata2 = [ x for x in range(89) ]
ydata2 = [ (x*slope + intercept) for x in range(89) ]


plt.plot(xdata,ydata,'b.',xdata2,ydata2,'r-')
plt.title("Age of First Use vs Usage in the Last 30 Days")
plt.xlabel("Age of First Use")
plt.ylabel("Usage in the Past 30 Days)")
plt.legend(["Data","Linear Fit"])
plt.xlim(0,90)
plt.ylim(0,31)
plt.tight_layout()
plt.show()