import math
from lib.calculator import Calculator

costs=[]
freights=[]
insurances=[]
rates=[]
shares=[]
finalSums={
	'hoghoogh':0,
	'nimDarsad':0,
	'maliat6Darsad':0,
	'maliat3Darsad':0,
	'total':0}
	
# Get input from user
def getNumInput(message=""):
        """ getNumInput([message]) --> int
        Keep getting input from user while its a coorect input and return the number. """
	while True:
		try:
			_num = float(raw_input(message).strip())
			break
		except ValueError:
			print "ERROR!! Lotfan meghdare addadi vared konid..."			
	return _num
	

# Build freights[] and insurances[] based on shares of products
def buildArrays(freight, insurance):
	for share in shares:
		if freight > 1:
			freights.append(round(share * freight / 100))
		else:
			freights.append(1)
		
		insurances.append(round(share * insurance / 100))
		
	diffInsurance = insurance - sum(insurances)
	insurances[-1] += diffInsurance
		
	if freight > 1:
		diffFreight = freight - sum(freights)
		freights[-1] += diffFreight		
		
# Format the number
def formatOutput(number):
        """ formatOutput(number) --> str
        Recieve a number and format it with thousand seprator then return it."""
        lenght = len(str(number))
        number = int(number)
        if lenght>= 3:
                return format(number, "03,d")
        return number

# Print the result in an agile way so end-user can read it easily
def printResult(table):
	print 'Hoghoogh voroodi: %s ' % formatOutput(table['hoghoogh'])
	print 'Nimdarsad: %s ' % formatOutput(table['nimDarsad'])
	print 'Maliat 6 darsad: %s ' % formatOutput(table['maliat6Darsad'])
	print 'Maliat 3 darsad: %s ' % formatOutput(table['maliat3Darsad'])
	print 'Jame kol: %s RIAL' % formatOutput(table['total'])


# Gather basic data from user
itemsCount = int(getNumInput("Tedade aghlame ezharname? "))
invoiceTotal = getNumInput("Arzeshe Faktor? ")
nerkhArz = getNumInput("Nerkhe Arz? ")

# Based on the itemsCount, get costs and rates then build the shares[]
for i in range(itemsCount):
	if itemsCount > 1:
		tempCost = getNumInput("\nArzeshe ghalame " + str(i+1) + "? ")
	else:
		tempCost = invoiceTotal
	costs.append(tempCost)
	
	tempRate = getNumInput("Makhaze ghalame " + str(i+1) + "? ")
	rates.append(tempRate)
	
	tempShare = round(tempCost * 100 / invoiceTotal)
	shares.append(tempShare)

# Deleting temp variables to free up memory
del(tempCost)
del(tempRate)
del(tempShare)	

# Freight
hasFreight = raw_input("Aya keraye haml darad?(Y/N) ")
if hasFreight.lower() == 'y':
	freight = getNumInput("Keraye haml? ")
	nerkheArzeFrieght = getNumInput("Nerkhe arze keraye haml? ")    
	freight = freight * nerkheArzeFrieght
	freight = round(freight)
else:
	freight = 1.0
	
# Insurance
hasInsurance = raw_input("Aya kala bimeh nameh darad?(Y/N) ")
if hasInsurance.lower() == 'y':
    insurance = getNumInput("Bimeh? ")
else:
    insurance = round((invoiceTotal * nerkhArz + freight) * 0.5 / 100)


buildArrays(freight, insurance)

print '@' * 85

for i in range(itemsCount):
	# Calculator.__init__(self, arzesh=0, freight=1, insurance=0, rate=1, nerkhArz=1):
	pd = Calculator(costs[i], freights[i], insurances[i], rates[i], nerkhArz)
	res = pd.calcGomroki()
	print "\nMOHASEBATE GHALAME " + str(i+1)
	print '#' * 35
	print 'Arzesh: %s' % formatOutput(pd.arzesh)
	print 'Keraye haml: %s' % formatOutput(freights[i])
	print 'Bimeh: %s' % formatOutput(insurances[i])
	arzeshGomroki = pd.arzesh + freights[i] + insurances[i]
	print 'Jame CIF: %s' % formatOutput(arzeshGomroki)
	print '_' * 35
	printResult(res)
	
	finalSums['hoghoogh'] += pd.table['hoghoogh']
	finalSums['nimDarsad'] += pd.table['nimDarsad']
	finalSums['maliat6Darsad'] += pd.table['maliat6Darsad']
	finalSums['maliat3Darsad'] += pd.table['maliat3Darsad']
	finalSums['total'] += pd.table['total']
	
if itemsCount > 1:
	print "\nJAME TAMAME AGHLAM"
	print '#' * 35
	printResult(finalSums)
	