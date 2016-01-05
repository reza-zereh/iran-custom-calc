import math

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

def formatOutput(number):
        """ formatOutput(number) --> str
        Recieve a number and format it with thousand seprator then return it."""
        lenght = len(str(number))
        number = int(number)
        if lenght>= 3:
                return format(number, "03,d")
        return number

def ceilOrFloor(number):
	""" ceilOrFloor(number) --> float
	return ceiled number if >=0.5 and floored number if <0.5 """
	number = float(number)
	if math.modf(number)[0] >= 0.5:
		return math.ceil(number)
	else:
		return math.floor(number)
	
# Value
nerkhArz = getNumInput("Nerkhe Arz? ")
amount = getNumInput("Arzeshe kala? ")
arzesh = nerkhArz * amount
arzesh = ceilOrFloor(arzesh)

# Freight
hasFreight = raw_input("Aya keraye haml darad?(Y/N) ")
if hasFreight.lower() == 'y':
    nerkheArzeFrieght = getNumInput("Nerkhe arze keraye haml? ")
    freight = getNumInput("Keraye haml? ")
    freight = freight * nerkheArzeFrieght
    freight = ceilOrFloor(freight)
else:
        freight = 1.0

# Insurance
hasInsurance = raw_input("Aya kala bimeh nameh darad?(Y/N) ")
if hasInsurance.lower() == 'y':
    insurance = getNumInput("Bimeh? ")
else:
    insurance = math.ceil((arzesh + freight) * 0.5 / 100)


arzeshGomroki = arzesh + freight + insurance
rate = getNumInput("Maakhaz gomroki? ")
hoghoogh = arzeshGomroki * rate / 100
hoghoogh = ceilOrFloor(hoghoogh)

nimDarsad = hoghoogh * 0.5 / 100
nimDarsad = ceilOrFloor(nimDarsad)

maliat6Darsad = (arzeshGomroki + hoghoogh) * 6 / 100
maliat6Darsad = ceilOrFloor(maliat6Darsad)

maliat3Darsad = (arzeshGomroki + hoghoogh) * 3 / 100
maliat3Darsad = ceilOrFloor(maliat3Darsad)

total = hoghoogh + nimDarsad + maliat6Darsad + maliat3Darsad

print ''
print '#' * 35
print 'Arzesh: %s' %formatOutput(arzesh)
print 'Keraye haml: %s' %formatOutput(freight)
print 'Bimeh: %s' %formatOutput(insurance)
print 'Jame CIF: %s' %formatOutput(arzeshGomroki)
print ''
print '*' * 35
print 'Hoghoogh voroodi: %s ' %formatOutput(hoghoogh)
print 'Nimdarsad: %s ' %formatOutput(nimDarsad)
print 'Maliat 6 darsad: %s ' %formatOutput(maliat6Darsad)
print 'Maliat 3 darsad: %s ' %formatOutput(maliat3Darsad)
print '_' * 35
print 'Jame kol: %s RIAL' %formatOutput(total)

raw_input("\nPress enter to exit...")
exit()