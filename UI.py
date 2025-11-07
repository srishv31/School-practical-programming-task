import os
import abc
import UIText

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
            case "4":
                self.display_current_menu = self.DisplayStaffMenu
    

    def DisplayStaffMenu(self):
        PASSWORD = "password123"

        print("""Enter your password""")
        entered_password = input()
        if entered_password == PASSWORD: input("Correct Password. Press enter to continue...")

        self.display_current_menu = self.DisplayStaffOptionsMenu
    

    def DisplayStaffOptionsMenu(self):
        print(UIText.STAFF_OPTIONS_MENU)
        option = input()

class Menu:
    

        
UI()