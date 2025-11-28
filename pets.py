import sys
import pandas as pd

class Pet:
	pets = pd.DataFrame()
	
	@classmethod
	def AddPetsFromCSV(self, fileName):
		self.pets = pd.read_csv(fileName, index_col = "Pet ID")
		
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