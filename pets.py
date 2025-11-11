import sys

class Pet:
	petCount = 0
	pets = {}

	def __init__(self, name, petType, age, size, energy, fee, status, daysInCentre, petID = None):
		if petID == None:
			petID = str(self.petCount + 1)
			petID = "P" + "0" * (3 - len(petID)) + petID
		self.petID = petID
		self.name = name
		self.petType = petType
		self.age = age
		self.size = size
		self.energy = energy
		self.fee = fee
		self.status = status
		self.daysInCentre = daysInCentre
	
	@classmethod
	def AddPetsFromCSV(self, fileName):
		lines = []
		with open(fileName) as file:
			lines = file.readlines()
		for line in lines:
			petData = line.split(",")
			self.pets[petData[0]] = Pet(
				petData[1],
				petData[2],
				int(petData[3]),
				petData[4],
				petData[5],
				int(petData[6]),
				petData[7],
				int(petData[8]),
				petData[0])
	@classmethod
	def ViewAvailabelPets

if __name__ == "__main__":
	PETS_FILE_NAME = "pets.csv"
	Pet.AddPetsFromCSV(PETS_FILE_NAME)