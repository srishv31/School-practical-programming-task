import pandas as pd

class Adopter:
    # AdopterID,Name,HomeType,Experience,PreferredSize,PreferredEnergy,AdoptedPets
    adopters = pd.DataFrame()

    @classmethod
    def AddAdoptersFromCSV(self, fileName):
        self.adopters = pd.read_csv(fileName)
        self.adopters.columns = ["Adopter ID", "Name", "Home Type", "Experience", "Preferred Size", "Preferred Energy", "Adopted Pets"]
    
    @classmethod
    def CreateID(self):
       num = self.adopters.shape[0]
       return "A" + "0" * (3 - len(str(num))) + str(num)


    @classmethod
    def RegisterNewAdopter(self, fullName, homeType, experienceLevel, preferredPetSize, preferredEnergyLevel):
        newAdopter = pd.Series({"Adopter ID" : self.CreateID(),
                                "Name" : fullName,
                                "Home Type" : homeType,
                                "Experience" : experienceLevel,
                                "Preferred Size" : preferredPetSize,
                                "Preferred Energy" : preferredEnergyLevel,
                                "Adopted Pets" : ""})
        self.adopters = pd.concat([self.adopters, newAdopter], ignore_index=True)


ADOPTERS_FILE_NAME = "adopters.csv"
Adopter.AddAdoptersFromCSV(ADOPTERS_FILE_NAME)