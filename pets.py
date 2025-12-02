import sys
import pandas as pd

class Pet:
	pets = pd.DataFrame()
	
	@classmethod
	def AddPetsFromCSV(self, fileName):
		self.pets = pd.read_csv(fileName, index_col = "Pet ID")
			
	@classmethod
	def CreateID(self):
		num = self.pets.shape[0] + 1
		id =  "P" + "0" * (3 - len(str(num))) + str(num)
		return id

	@staticmethod
	def ValidatePetRegistrationInputs(name, type, age, size, energy, adoptionFee):
		if not name: return False
		if not type in ["Dog", "Cat", "Rabbit", "Hamster"]: return False
		if not (age.isnumeric() and int(age) <= 20): return 20
		if not size in ["Small", "Medium", "Large"]: return False
		if not energy in ["Low", "Medium", "High"]: return False
		if not adoptionFee.isnumeric(): return False
		fee = int(adoptionFee)
		if fee < 20 or fee > 300: return False
		return True

	@classmethod
	def RegisterNewPet(self, name, type, age, size, energy, adoptionFee):
		id = self.CreateID()
		self.pets.loc[id] = {
                                "Name" : name,
                                "Type" : type,
                                "Age" : age,
                                "Size" : size,
                                "Energy" : energy,
                                "Adoption Fee" : adoptionFee,
								"Status": "Available",
								"Days in Centre": "0"}
		return id

	@classmethod
	def ViewAllPets(self):
		print(self.pets)

	@classmethod
	def ViewAvailablePets(self):
		temppets = self.pets

		temppets.sort_values(by="Days In Centre", ascending=False)
		temppets = temppets[temppets["Status"] == "Available"]

		if len(temppets) == 0:
			print("No Available Pets")
		else:
			print("Available Pets:")
			print(temppets[temppets.columns.difference(["Status"])].to_string(index=False))
			
			avg_days_in_centre = temppets["Days In Centre"].mean()
			print(f"\n\nAverage Days In Centre: {avg_days_in_centre:.1f} days\n")

		print()
			

PETS_FILE_NAME = "pets.csv"
Pet.AddPetsFromCSV(PETS_FILE_NAME)