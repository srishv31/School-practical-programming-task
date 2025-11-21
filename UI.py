import os
import abc
import UIText

import pets

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
        input("Press enter to continue...")

    def DisplayRegisterAsAdopterPage(self):
        

    def DisplayAdopterLoginPage(self):
        print("Adopter Login")

    def DisplayStaffMenu(self):
        PASSWORD = "password123"

        print("""Enter your password""")
        entered_password = input()
        if entered_password == PASSWORD: input("Correct Password. Press enter to continue...")

        self.display_current_menu = self.DisplayStaffOptionsMenu
    

    def DisplayStaffOptionsMenu(self):
        print(UIText.STAFF_OPTIONS_MENU)
        option = input()
    

if __name__ == "__main__":
    ui = UI()