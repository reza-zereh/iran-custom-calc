import math

def getNumInput(message):
	while True:
		try:
			_num = input(message)
			break
		except NameError:
			print "ERROR!! Lotfan meghdare addadi vared konid..."
		except SyntaxError:
			print "ERROR!! Lotfan meghdare addadi vared konid..."
			
	return _num

nerkhArz = getNumInput("Nerkhe Arz? ")
amount = getNumInput("Arzeshe kala? ")
arzesh = nerkhArz * amount
if math.modf(arzesh)[0] >= 0.5:
    arzesh = math.ceil(arzesh)
else:
    arzesh = math.floor(arzesh)

hasFreight = raw_input("Aya keraye haml darad?(Y/N) ")
freight = 1.0;
if hasFreight.lower() == 'y':
    nerkheArzeFrieght = getNumInput("Nerkhe arze keraye haml? ")
    freight = getNumInput("Keraye haml? ")
    freight = freight * nerkheArzeFrieght
    if math.modf(freight)[0] >= 0.5:
        freight = math.ceil(freight)
    else:
        freight = math.floor(freight)

insurance = 0;
hasInsurance = raw_input("Aya kala bimeh nameh darad?(Y/N) ")
if hasInsurance.lower() == 'y':
    insurance = getNumInput("Bimeh? ")
else:
    insurance = math.ceil((arzesh + freight) * 0.5 / 100)

arzeshGomroki = arzesh + freight + insurance
rate = getNumInput("Maakhaz gomroki? ")
hoghoogh = arzeshGomroki * rate / 100
if math.modf(hoghoogh)[0] >= 0.5:
    hoghoogh = math.ceil(hoghoogh)
else:
    hoghoogh = math.floor(hoghoogh)

nimDarsad = hoghoogh * 0.5 / 100
if math.modf(nimDarsad)[0] >= 0.5:
    nimDarsad = math.ceil(nimDarsad)
else:
    nimDarsad = math.floor(nimDarsad)

maliat6Darsad = (arzeshGomroki + hoghoogh) * 6 / 100
if math.modf(maliat6Darsad)[0] >= 0.5:
    maliat6Darsad = math.ceil(maliat6Darsad)
else:
    maliat6Darsad = math.floor(maliat6Darsad)

maliat3Darsad = (arzeshGomroki + hoghoogh) * 3 / 100
if math.modf(maliat3Darsad)[0] >= 0.5:
    maliat3Darsad = math.ceil(maliat3Darsad)
else:
    maliat3Darsad = math.floor(maliat3Darsad)

total = hoghoogh + nimDarsad + maliat6Darsad + maliat3Darsad

print ''
print '#' * 35
print 'Arzesh: %d' %arzesh
print 'Keraye haml: %d' %freight
print 'Bimeh: %d' %insurance
print 'Jame CIF: %d' %arzeshGomroki
print ''
print '*' * 35
print 'Hoghoogh voroodi: %d ' % hoghoogh
print 'Nimdarsad: %d ' % nimDarsad
print 'Maliat 6 darsad: %d ' %maliat6Darsad
print 'Maliat 3 darsad: %d ' %maliat3Darsad
print '_' * 35
print 'Jame kol: %d ' %total

raw_input("\nPress enter to exit...")
exit()