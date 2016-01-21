class Calculator(object):
    totalCIF = 0
    daysInMonth = [0, 31, 31, 31, 31, 31, 31, 30, 30, 30, 30, 30, 29]
    lifterakPerHour = 820000
    pricePerDayINDOOR = 4000
    pricePerDayOUTDOOR = 2200
    pricePerDay20FOOT_1_60 = 32000
    pricePerDay20FOOT_61 = 27000
    pricePerDay40FOOT_1_60 = 47000
    pricePerDay40FOOT_61 = 40000
    ritch20FOOT = 680000
    ritch40FOOT = 910000
    extraWeightPerTon20FOOT = 57000
    extraWeightPerTon40FOOT = 67000
    limitWeightTon20FOOT = 12
    limitWeightTon40FOOT = 22
    container20FootWeight = 2200
    container40FootWeight = 4200


    def __init__(self, arzesh=0, freight=1, insurance=0, rate=1, nerkhArz=1):
        self.arzesh = arzesh
        self.freight = freight
        self.insurance = insurance
        self.nerkhArz = nerkhArz
        self.rate = rate
        self.arzeshGomroki = 0
        self.hoghoogh = 0
        self.maliat6Darsad = 0
        self.maliat3Darsad = 0
        self.table = {}


    def setArzesh(self, arzesh):
        self.arzesh = arzesh

    def setFreight(self, freight):
        self.freight = freight

    def setInsurance(self, insurance):
        self.insurance = insurance

    def setRate(self, rate):
        self.rate = rate

    def setNerkhArz(self, nerkhArz):
        self.nerkhArz = nerkhArz

    def calcGomroki(self):
        self.arzesh = round(self.nerkhArz * self.arzesh)

        self.arzeshGomroki = self.arzesh + self.freight + self.insurance
        Calculator.totalCIF += self.arzeshGomroki
        self.hoghoogh = round(self.arzeshGomroki * self.rate / 100)
        self.table['hoghoogh'] = self.hoghoogh

        self.nimDarsad = round(self.hoghoogh * 0.5 / 100)
        self.table['nimDarsad'] = self.nimDarsad

        self.maliat6Darsad = round((self.arzeshGomroki + self.hoghoogh) * 6 / 100)
        self.table['maliat6Darsad'] = self.maliat6Darsad

        self.maliat3Darsad = round((self.arzeshGomroki + self.hoghoogh) * 3 / 100)
        self.table['maliat3Darsad'] = self.maliat3Darsad

        self.total = self.hoghoogh + self.nimDarsad + self.maliat6Darsad + self.maliat3Darsad
        self.table['total'] = self.total

        return self.table
    """ end of calcGomroki() """

    def daysInWarehouse(self, enteranceDate, clearanceDate):
        self.eYear, self.eMonth, self.eDay = map(int, enteranceDate.split('/'))
        self.cYear, self.cMonth, self.cDay = map(int, clearanceDate.split('/'))
        self.eDateInDays = 0
        self.cDateInDays = 0

        # Convert the product entrance date to equivalent days
        self.eDateInDays += self.eYear * 365
        self.eDateInDays += self.eDay
        for i in range(1, self.eMonth):
            self.eDateInDays += Calculator.daysInMonth[i]

        # Convert the product clearance date to equivalent days
        self.cDateInDays += self.cYear * 365
        self.cDateInDays += self.cDay
        for i in range(1, self.cMonth):
            self.cDateInDays += Calculator.daysInMonth[i]

        totaldaysinwarehouse = self.cDateInDays - self.eDateInDays + 1
        #print totaldaysinwarehouse
        return totaldaysinwarehouse

    def roundToThousand(self, number):
        diff = number % 1000
        if diff >= 500:
            return number + (1000 - (number % 1000))
        else:
            return number - (number % 1000)
    """ end of roundToThousand() """


    def anbardariPallet(self, totalDaysInWarehouse):

        # warehouseType:1 => Indoor
        # warehouseType:2 => Outdoor
        if self.warehouseType == 1:
            pricePerDay = Calculator.pricePerDayINDOOR
        else:
            pricePerDay = Calculator.pricePerDayOUTDOOR

        if self.grossWeight % 1000 != 0:
            tonaj = int((self.grossWeight / 1000) + 1)
        else:
            tonaj = int(self.grossWeight / 1000)
        print "tonaj: " + str(tonaj)
        anbardari = self.roundToThousand(totalDaysInWarehouse * pricePerDay * tonaj)
        if tonaj > 2:
            takhlieBargiri = Calculator.lifterakPerHour * 2
        else:
            takhlieBargiri = Calculator.lifterakPerHour

        return anbardari, takhlieBargiri
    """ end of anbardariPallet() """

    def setcontainerscount(self, containersCount=1):
        self.containersCount = containersCount

    def anbardari20foot(self, totalDaysInWarehouse):

        if totalDaysInWarehouse <= 60:
            anbardari = self.roundToThousand(totalDaysInWarehouse * Calculator.pricePerDay20FOOT_1_60)
        else:
            anbardari = self.roundToThousand(totalDaysInWarehouse * Calculator.pricePerDay20FOOT_61)

        takhlieBargiri = Calculator.ritch20FOOT * self.containersCount * 2
        containersCountWeight = self.containersCount * Calculator.container20FootWeight
        weightWithContainerInTon = int(((self.grossWeight + containersCountWeight) / 1000) + 1)
        if weightWithContainerInTon > Calculator.limitWeightTon20FOOT * self.containersCount:
            diff = weightWithContainerInTon - (Calculator.limitWeightTon20FOOT * self.containersCount)
            # mult by 2 => one for loading container, one for unloading
            takhlieBargiri += diff * Calculator.extraWeightPerTon20FOOT * 2
        return anbardari, takhlieBargiri

    """ end of anbardari20foot() """

    def anbardari40foot(self, totalDaysInWarehouse):
        if totalDaysInWarehouse <= 60:
            anbardari = self.roundToThousand(totalDaysInWarehouse * Calculator.pricePerDay40FOOT_1_60)
        else:
            anbardari = self.roundToThousand(totalDaysInWarehouse * Calculator.pricePerDay40FOOT_61)

        takhlieBargiri = Calculator.ritch40FOOT * self.containersCount * 2
        containersWeight = self.containersCount * Calculator.container40FootWeight
        weightWithContainerInTon = int(((self.grossWeight + containersWeight) / 1000) + 1)
        if weightWithContainerInTon > Calculator.limitWeightTon40FOOT * self.containersCount:
            diff = weightWithContainerInTon - (Calculator.limitWeightTon40FOOT * self.containersCount)
            # mult by 2 => one for loading container, one for unloading
            takhlieBargiri += diff * Calculator.extraWeightPerTon40FOOT * 2

        return anbardari, takhlieBargiri
    """ end of anbardari40foot """

    def initAnbardari(self, enteranceDate, clearanceDate, grossWeight, warehouseType, packingType, hasInsurance):
        self.enteranceDate = enteranceDate
        self.clearanceDate = clearanceDate
        self.grossWeight = grossWeight
        self.warehouseType = warehouseType
        self.packingType = packingType
        self.hasInsurance = hasInsurance
        self.warehouseTypeDict = {
            1 : self.anbardariPallet,
            2 : self.anbardari20foot,
            3 : self.anbardari40foot
        }


    # this function calculate the price for kepting the product in warehouse
    def calcAnbardari(self):
        totalDaysInWarehouse = self.daysInWarehouse(self.enteranceDate, self.clearanceDate)

        if totalDaysInWarehouse < 150:
            totalMonthsInWarehouse = totalDaysInWarehouse / 30
            if totalDaysInWarehouse % 30 != 0:
                totalMonthsInWarehouse += 1
        else:
            totalMonthsInWarehouse = 5

        #print Calculator.totalCIF
        tejari = self.roundToThousand(Calculator.totalCIF * 2 / 1000)

        if not self.hasInsurance:
            bimeh = self.roundToThousand((Calculator.totalCIF * 55 / 100) / 1000 * totalMonthsInWarehouse)
        else:
            bimeh = 0

        anbardari, takhlieBargiri = self.warehouseTypeDict[self.packingType](totalDaysInWarehouse)
        total = anbardari + takhlieBargiri + tejari + bimeh

        return {
            '01_Anbardari' : anbardari,
            '02_Takhlie-Bargiri' : takhlieBargiri,
            '03_Khadamete Tejari' : tejari,
            '04_Bimeh' : bimeh,
            '05_Jame Kol': total}
