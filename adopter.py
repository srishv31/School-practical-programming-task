import pandas as pd

import pets

class Adopter:
    adopters = pd.DataFrame()

    @classmethod
    def AddAdoptersFromCSV(self, fileName):
        self.adopters = pd.read_csv(fileName, index_col="Adopter ID")
    
    @classmethod
    def CreateID(self):
       num = self.adopters.shape[0] + 1
       id =  "A" + "0" * (3 - len(str(num))) + str(num)
       return id

    @classmethod
    def ValidateAdopterID(self, adopterID):
        return adopterID in self.adopters.index

    @staticmethod
    def ValidateAdopterRegistrationInputs(fullName, homeType, experienceLevel, preferredPetSize, preferredEnergyLevel):
        if len(fullName.split(" ")) < 2: return False
        if homeType not in ("Flat", "House", "Farm"): return False
        if experienceLevel not in ("none", "Some", "Expert"): return False
        if preferredPetSize not in ("Small", "Medium", "Large", "Any"): return False
        if preferredEnergyLevel not in ("Low", "Medium", "High", "Any"): return False
        return True

    @classmethod
    def RegisterNewAdopter(self, fullName, homeType, experienceLevel, preferredPetSize, preferredEnergyLevel):
        id = self.CreateID()
        self.adopters.loc[id] = {
                                "Name" : fullName,
                                "Home Type" : homeType,
                                "Experience" : experienceLevel,
                                "Preferred Size" : preferredPetSize,
                                "Preferred Energy" : preferredEnergyLevel,
                                "Adopted Pets" : "none"}
        return id

    # @classmethod
    # def GetCompatibilityScore(self, adopterID, petID):
    #     adopter = 

ADOPTERS_FILE_NAME = "adopters.csv"
Adopter.AddAdoptersFromCSV(ADOPTERS_FILE_NAME)