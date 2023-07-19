class Stamina:

	def __init__(self, co2_max, o2_max, o2_increase, co2_decrease, glucose_max, atp_max):

		self.co2_max = co2_max
		self.o2_max = o2_max
		self.o2_increase = o2_increase
		self.co2_decrease = co2_decrease
		self.atp_max = atp_max
		self.glucose_max = glucose_max
		self.co2_level = 0
		self.o2_level = o2_max
		self.glucose_level = glucose_max
		self.atp_level = atp_max
		self.la_level = 0

	def reset(self):
		self.co2_level = 0
		self.o2_level = self.o2_max
		self.glucose_level = self.glucose_max
		self.atp_level = self.atp_max
		self.la_level = 0

	def aerobicRespiration(self):
		if (self.glucose_level - 1 >= 0):
			if (self.o2_level - 6 >= 0 and self.co2_level + 6 <= self.co2_max):
				self.o2_level -= 6
				self.co2_level += 6
				self.glucose_level -= 1
				if (self.atp_level + 36 < self.atp_max):
					self.atp_level += 36
				else:
					self.atp_level = self.atp_max
		
	def anaerobicRespiration(self):
		if (self.glucose_level - 1 >= 0):
			self.glucose_level -= 1
			if (self.atp_level + 2 <= self.atp_max):
				self.atp_level += 2
				self.la_level +=2
			else:
				self.atp_level = self.atp_max
				self.la_level += 2

	def useEnergy(self, rate):

		if self.o2_level - amount > 0 and self.energy_level - amount > 0:

			self.energy_level -= amount
			self.o2_level -= amount
			self.co2_level += amount
		
		else:

			self.anaerobic_energy_level -= amount
			self.energy_level -= amount

	def inhale(self, amount):
		
		self.useEnergy(amount)

		if self.o2_level + self.o2_increase < self.o2_max:
			
			self.o2_level += self.o2_increase

		else:
		
			self.o2_level = self.o2_max
	
	def exhale(self, amount):

		self.useEnergy(amount)

		if self.co2_level - self.co2_decrease > 0:
			
			self.co2_level -= self.co2_decrease

		else:
	
			self.co2_level = 0
		

sdeplete = input('How much depletion?')
sreplenish = input('How much replenishing?')
deplete = float(sdeplete)
replenish = float(sreplenish)









				