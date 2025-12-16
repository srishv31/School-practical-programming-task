import os
import abc
import UIText

import pets
import adopter

class UI:
    def __init__(self):
        os.system("clear")
        self.display_current_menu = self.DisplayMainMenu
        self.DisplayMainMenu()

        self.signed_in_adopter_id = None

        # Main Loop
        self.running = True
        while self.running:
            self.clearscreen()
            self.display_current_menu()
            

    @staticmethod
    def clearscreen():
        os.system("clear")


    def DisplayMainMenu(self):
        print(UIText.MAIN_MENU)
        
        option = input()
        self.clearscreen()

        match option:
            case "1":
                self.display_current_menu = self.DisplayAvailablePetsPage
            case "2":
                self.display_current_menu = self.DisplayRegisterAsAdopterPage
            case "3":
                self.display_current_menu = self.DisplayAdopterLoginPage
            case "4":
                self.display_current_menu = self.DisplayStaffMenu
            case "5":
                self.running = False
    
    def DisplayAvailablePetsPage(self):
        petstext = pets.Pet.ViewAvailablePets()
        self.display_current_menu = self.DisplayMainMenu
        input("Press enter to return to main menu...")

    def DisplayRegisterAsAdopterPage(self):
        while True:
            fullName = input("Full Name: ")
            homeType = input("Home Type: ")
            experienceLevel = input("Experience Level: ")
            preferredPetSize = input("Preferred Pet Size: ")
            preferredEnergyLevel = input("Preferred Energy Level: ")
            if adopter.Adopter.ValidateAdopterRegistrationInputs(fullName, homeType, experienceLevel, preferredPetSize, preferredEnergyLevel):
                break
            else:
                print("Invalid Input")
                input("Press enter to return to main menu...")
                self.display_current_menu = self.DisplayMainMenu
                return
        id = adopter.Adopter.RegisterNewAdopter(fullName, homeType, experienceLevel, preferredPetSize, preferredEnergyLevel)
        print("Registered. Welcome!")
        print(f"You're adopter ID is {id}")
        input("Press enter to return to main menu...")
        self.display_current_menu = self.DisplayMainMenu

    def DisplayAdopterLoginPage(self):
        adopterID = input("Adopter ID: ")
        if not adopter.Adopter.ValidateAdopterID(adopterID):
            print("Adopter ID not found.")
            self.display_current_menu = self.DisplayMainMenu
            input("Press enter to return to main menu...")
            return
        
        self.signed_in_adopter_id = adopterID
        self.display_current_menu = self.DisplayAdopterMenu
        print("Login successful.")
        input("Press enter to continue...")
    
    def DisplayAdopterMenu(self):
        print(UIText.ADOPTER_OPTIONS_MENU)
        
        option = input()
        self.clearscreen()

        match option:
            case "1":
                self.display_current_menu = self.DisplayCompatibilityMatchesPage
            case "2":
                self.display_current_menu = self.DisplayReservePetPage
            case "3":
                self.display_current_menu = self.DisplayAdoptedReservedPets
            case "4":
                self.display_current_menu = self.DisplayCancelReservationPage
            case "5":
                self.signed_in_adopter_id = None
                self.display_current_menu = self.DisplayMainMenu

    def DisplayCompatibilityMatchesPage(self):
        print("Compatibility Page")

    def DisplayReservePetPage(self):
        print("Reserve A Pet")
        if adopter.Adopter.HasReservedPet(self.signed_in_adopter_id):
            print("You already have a reservation. Please complete or cancel it first.")
            self.display_current_menu = self.DisplayAdopterMenu
            return

        petID = input("Pet ID to reserve: ")
        if not adopter.Adopter.ReservePet(self.signed_in_adopter_id, petID):
            print("Failed to reserve. Invalid Pet ID.")
        else:
            print("Reservation successful.")
        input("Press enter to return to adopter menu...")
        self.display_current_menu = self.DisplayAdopterMenu

    
    def DisplayAdoptedReservedPets(self):
        adopter.Adopter.DisplayReservedAdoptedPets(self.signed_in_adopter_id)
        input("Press enter to return to adopter menu...")
        self.display_current_menu = self.DisplayAdopterMenu
    
    def DisplayCancelReservationPage(self):
        print(f"You have currently reserved pet with ID {adopter.Adopter.HasReservedPet(self.signed_in_adopter_id)}.")
        if adopter.Adopter.HasReservedPet(self.signed_in_adopter_id):
            confirm = input("Would you like to cancel your current reservation?(y/n) ") == "y"
            if confirm:
                adopter.Adopter.RemoveReservation(self.signed_in_adopter_id, adopter.Adopter.HasReservedPet(self.signed_in_adopter_id))
        print("Reservation Cancelled.")
        input("Press enter to return to adopter menu...")
        self.display_current_menu = self.DisplayAdopterMenu


    def DisplayStaffMenu(self):
        PASSWORD = "pawsadopt2024"
        
        for i in range(3, 0, -1):
            entered_password = input(f"Enter Password ({i} tries left): ")
            if entered_password == PASSWORD:
                self.display_current_menu = self.DisplayStaffOptionsMenu
                print("Correct Password.")
                input("Press enter to continue...")
                return
        print("Incorrect Password entered 3 times.")
        input("Press enter to return to main menu...")

    def DisplayStaffOptionsMenu(self):
        print(UIText.STAFF_OPTIONS_MENU)
        option = input()

        match option:
            case "1":
                self.display_current_menu = self.DisplayAddNewPetPage
            case "2":
                self.display_current_menu = self.DisplayCompleteAnAdoptionPage
            case "3":
                self.display_current_menu = self.DisplayViewPetsPage
            case "4":
                self.display_current_menu = self.DisplayViewStatisticsPage
            case "5":
                self.display_current_menu = self.DisplayRemovePetPage
            case "6":
                self.running = False
    
    def DisplayAddNewPetPage(self):
        while True:
            name = input("Pet Name: ")
            type = input("Pet Type: ")
            age = input("Pet Age in years: ")
            size = input("Pet Size: ")
            energy = input("Energy Level: ")
            adoptionFee = input("Adoption Fee: £")
            if pets.Pet.ValidatePetRegistrationInputs(name, type, age, size, energy, adoptionFee):
                break
            else:
                print("Invalid Input")
                input("Press enter to return to main menu...")
                self.display_current_menu = self.DisplayMainMenu
                return

        id = pets.Pet.RegisterNewPet(name, type, age, size, energy, adoptionFee)
        print(f"Pet registered with id {id}.")
        input("Press enter to return to main menu...")
        self.display_current_menu = self.DisplayMainMenu

    def DisplayCompleteAnAdoptionPage(self):
        print("Complete and Adoption")
    
    def DisplayViewPetsPage(self):
        nReserved = 0
        nAdopted = 0
        nAvailable = 0
        nTotal = 0
        for petID, petData in pets.Pet.pets.iterrows():
            nTotal += 1
            match petData["Status"]:
                case "Adopted": nAdopted += 1
                case "Reserved": nReserved += 1
                case "Availabe": nAvailable += 1
            print(f"Name: {petData["Name"]}\nType: {petData["Type"]}\nAge: {petData["Age"]}\nStatus: {petData["Status"]}\n")
        print("Number of pets: {nTotal}")
        print("Number of adopted pets: {nAdopted}")
        print("Number of reserved pets: {nReserved}")
        print("Number of available pets: {nAvailable}")
        return True

    def DisplayViewStatisticsPage(self):
        nDogs = 0
        nCats = 0
        nRabbits = 0
        nHamsters = 0
        nAdopted = 0
        nAvailable = 0
        nAdoptedWait = 0
        longest = 0
        longestName = None
        totalIncome = 0
        for petID, petData in pets.Pet.pets.iterrows():
            match petData["Type"]:
                case "Dog": nDogs += 1
                case "Cat": nCats += 1
                case "Rabbit": nRabbits += 1
                case "Hamster": nHamsters += 1
            if petData["Status"] == "Adopted":
                nAdopted += 1
                nAdoptedWait += int(petData["Days In Centre"])
            elif petData["Status"] == "Available":
                totalIncome += int(petData["Fee"])
                nAvailable += 1
            wait = int(petData["Days In Centre"])
            if wait > longest:
                longest = wait
                longestName = petData["Name"]
        print(f"Number of dogs: {nDogs}")
        print(f"Number of cats: {nCats}")
        print(f"Number of rabbits: {nRabbits}")
        print(f"Number of hamsters: {nHamsters}")
        petTypes = ["dogs", "cats", "rabbits", "hamsters"]
        nPets = [nDogs, nCats, nRabbits, nHamsters]
        print(f"The most common pet type is {petTypes[nPets.index(max(nPets))]}.")
        print()

        print(f"Number of adopted pets : {nAdopted}")
        print(f"Average wait length: {nAdoptedWait / nAdopted}")
        print(f"The longest waiting pet is {longestName} who has been waiting for {longest} days")
        print()

        print(f"Total Fees: {totalIncome}")
        print(f"Average Fee: {totalIncome / nAvailable}")
        print()

        nAdopters = 0
        nAdoptersWithAdoption = 0
        highestLevel = 0
        levels = ["none", "Some", "Expert"]
        for adopterID,  adopterData in adopter.Adopter.adopters.iterrows():
            nAdopters += 1
            if adopterData["Adopted Pets"] != "none":
                nAdoptersWithAdoption += 1
            level = levels.index(adopterData["Experience"])
            highestLevel = max(level, highestLevel)

        print(f"Number of registered adopters: {nAdopters}")
        print(f"Number of adopters with completed adoptions: {nAdoptersWithAdoption}")
        print(f"Highest adopter experience: {levels[highestLevel]}")
        print()

        input("Press enter to return to staff menu...")
        self.display_current_menu = self.DisplayStaffOptionsMenu
        return

    
    def DisplayRemovePetPage(self):
        print("Remove a Pet")

if __name__ == "__main__":
    ui = UI()