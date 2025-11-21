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
		
	@classmethod
	def ViewAvailablePets(self):
		temppets = self.pets

		temppets.sort_values(by="DaysInCentre", ascending=False)
		temppets = temppets[temppets["Status"] == "Available"]

		if len(temppets) == 0:
			print("No Available Pets")
		else:
			print("Available Pets:")
			print(temppets[temppets.columns.difference(["Status"])].to_string(index=False))
			
			avg_days_in_centre = temppets["DaysInCentre"].mean()
			print("\n\nAverage Days In Centre:", avg_days_in_centre, "days\n")

		print()
			

PETS_FILE_NAME = "pets.csv"
Pet.AddPetsFromCSV(PETS_FILE_NAME)