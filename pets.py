import sys
import pandas as pd

class Pet:
	petCount = 0
	pets = pd.DataFrame()

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
		self.pets = pd.read_csv(fileName)
		self.pets.columns = ["Pet ID", "Name", "Type", "Age", "Size", "Energy", "Fee", "Status", "DaysInCentre"]
		print(self.pets.head)
		
	@classmethod
	def ViewAvailabelPets(self):
		temppets = self.pets
		temppets.sort_values(by="DaysInCentre", ascending=False)
		temppets = temppets[temppets["Status"] == "Available"]
		print(temppets)
			

if __name__ == "__main__":
	PETS_FILE_NAME = "pets.csv"
	Pet.AddPetsFromCSV(PETS_FILE_NAME)
	Pet.ViewAvailabelPets()