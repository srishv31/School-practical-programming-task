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
        if adopter.Adopter.HasReservedPet():
            confirm = input("Would you like to cancel your current reservation?(y/n) ") == "y"
            if confirm:
                ado


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
        print("View all pets")
    
    def DisplayViewStatisticsPage(self):
        print("View Statistics")
    
    def DisplayRemovePetPage(self):
        print("Remove a Pet")

if __name__ == "__main__":
    ui = UI()