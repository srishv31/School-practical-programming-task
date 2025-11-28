import pandas as pd

import pets

class Adopter:
    adopters = pd.DataFrame()

    @classmethod
    def AddAdoptersFromCSV(self, fileName):
        self.adopters = pd.read_csv(fileName, index_col = "Adopter ID")
    
    @classmethod
    def CreateID(self):
       num = self.adopters.shape[0]
       return "A" + "0" * (3 - len(str(num))) + str(num)

    @classmethod
    def ValidateAdopterID(self, adopterID):
        return (self.adopters["Adopter ID"] == adopterID).any()

    @staticmethod
    def ValidateAdopterRegistrationInputs(fullName, homeType, experienceLevel, preferredPetSize, preferredEnergyLevel):
        if len(fullName.split(" ")) < 2: return False
        if homeType not in ("Flat", "House", "Farm"): return False
        if experienceLevel not in ("None", "Some", "Expert"): return False
        if preferredPetSize not in ("Small", "Medium", "Large", "Any"): return False
        if preferredEnergyLevel not in ("Low", "Medium", "High", "Any"): return False
        return True

    @classmethod
    def RegisterNewAdopter(self, fullName, homeType, experienceLevel, preferredPetSize, preferredEnergyLevel):
        # newAdopter = pd.DataFrame({"Adopter ID" : [self.CreateID()],
        #                         "Name" : [fullName],
        #                         "Home Type" : [homeType],
        #                         "Experience" : [experienceLevel],
        #                         "Preferred Size" : [preferredPetSize],
        #                         "Preferred Energy" : [preferredEnergyLevel],
        #                         "Adopted Pets" : ["None"]})
        # newAdopter.set_index("Adopter ID")
        # self.adopters = pd.concat([self.adopters, newAdopter])

        self.adopters.loc[self.adopters.shape[0]] = []

        newAdopter = pd.DataFrame({"Adopter ID" : [self.CreateID()],
                                "Name" : [fullName],
                                "Home Type" : [homeType],
                                "Experience" : [experienceLevel],
                                "Preferred Size" : [preferredPetSize],
                                "Preferred Energy" : [preferredEnergyLevel],
                                "Adopted Pets" : ["None"]})
        newAdopter.set_index("Adopter ID")
        self.adopters = pd.concat([self.adopters, newAdopter])
        print(self.adopters)
        input()

    # @classmethod
    # def GetCompatibilityScore(self, adopterID, petID):
    #     adopter = 

ADOPTERS_FILE_NAME = "adopters.csv"
Adopter.AddAdoptersFromCSV(ADOPTERS_FILE_NAME)