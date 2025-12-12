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

    @classmethod
    def HasReservedPet(self, adopterID):
        adopter = self.adopters.loc[adopterID]
        adoptedPets = adopter["Adopted Pets"]

        if adoptedPets == "none": return False

        for petID in adoptedPets.split(";"):
            pet = pets.Pet.pets.loc[petID]
            if pet["Status"] == "Reserved": return petID
        return False

    @classmethod
    def ReservePet(self, adopterID, petID):
        if not pets.Pet.ValidatePetID(petID):
            return False
        pets.Pet.SetPetToReserved(petID)
        adopter = self.adopters.loc[adopterID]
        if adopter["Adopted Pets"] == "none":
            adopter["Adopted Pets"] = petID
        else:
            adopter["Adopted Pets"] += ";" + petID
        return True

    @classmethod
    def DisplayReservedAdoptedPets(self, adopterID):
        adopter = self.adopters.loc[adopterID]
        adoptedPets = adopter["Adopted Pets"]
        if adoptedPets == "none":
            print("You haven't reserved or adopted any pets yet.")
            return False
        for petID in adoptedPets.split(";"):
            petData = pets.Pet.pets.loc[petID]
            print(f"Name: {petData["Name"]}\nType: {petData["Type"]}\nAge: {petData["Age"]}\nStatus: {petData["Status"]}{"\nReady to finalise adoption." if (petData["Status"] == "Reserved") else ""}\n")
        return True

    @classmethod
    def RemoveReservation(self, adopterID, petID):
        adopter = self.adopters.loc[adopterID]
        reserved = adopter["Adopted Pets"]
        reservedList = reserved.split(";")
        reservedList.pop(reservedList.index(petID))
        reserved = ";".join(reservedList)
        adopter["Adopted Pets"] = reserved if len(reservedList) else "none"
        return True

ADOPTERS_FILE_NAME = "adopters.csv"
Adopter.AddAdoptersFromCSV(ADOPTERS_FILE_NAME)