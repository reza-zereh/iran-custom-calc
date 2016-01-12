class Calculator(object):
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
		

	
		
		
		
		
		
		