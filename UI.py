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
                break # REMOVE|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
            
                return
        adopter.Adopter.RegisterNewAdopter(fullName, homeType, experienceLevel, preferredPetSize, preferredEnergyLevel)
        print("Registered")
        input("Press enter to return to main menu...")
        self.display_current_menu = self.DisplayMainMenu

    def DisplayAdopterLoginPage(self):
        adopterID = input("Adopter ID: ")
        if not adopter.Adopter.ValidateAdopterID(adopterID):
            print("Adopter ID not found.")
            self.display_current_menu = self.DisplayMainMenu
            input("Press enter to return to main menu...")
            return
        
        self.display_current_menu = self.DisplayAdopterMenu
        print("Login successful.")
        input("Press enter to continue...")
    
    def DisplayAdopterMenu(self):
        print(UIText.STAFF_OPTIONS_MENU)
        
        option = input()
        self.clearscreen()

        match option:
            case "1":
                self.display_current_menu = self.DisplayCompatibilityMatchesPage
            case "2":
                self.display_current_menu = self.DisplayRegisterAsAdopterPage
            case "3":
                self.display_current_menu = self.DisplayAdopterLoginPage
            case "4":
                self.display_current_menu = self.DisplayStaffMenu
            case "5":
                self.running = False

    def DisplayCompatibilityMatchesPage(self):
        print("Compatibility Page")

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


if __name__ == "__main__":
    ui = UI()