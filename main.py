"""
-This is a Banking Application with OOPS Concepts

Thanks To: Geeks for Geeks
            Techno Geek

            ^ I watched the tutorials and the code link to get an understanding of how they did the code. 
"""

# Notes:
# Add an actual parameter
# Add colors to texts
# Maybe try adding a picture
# Work on the login section



# NECESSARY ITEMS IN PROGRAM: 
# -----Input/Output
#------Abstract Data in a Collection
#-----A procedure with a parameter
#------Sequence, Selection, iteration
#----2 Calls to your procedure w/different arguments

import pyfiglet
import random
from colorama import init, Fore, Back, Style

# This is an import statement to generate Ascii art for any word title

result = pyfiglet.figlet_format("Welcome to my Python ATM machine")

print(result)
print("\n Please Open an Account first. Create a Pin for you to use.")
# ADD MORE FEATURES Give the option to choose deposit, withdrawal, etc....

# This is the class where the money is stored
class Banking_Account:

  def __init__(self):
    self.b_balance = 0

# Creating account
  def create(self):
    self.pin = random.randint(1000,9999)
    print(self.pin, "This is your pin")
    self.name = input("Enter your full name: ")
    self.gender = input("Enter [M] or [F] or [prefer not to say]: ")

# Adds money to the balance
  def deposit(self):
    amount = float(input("\nAmount of Money to be Deposited: "))
    times = int(input("How many times do you want to deposit that amount: "))
    finale = amount * times
    self.b_balance += finale 
    print(f"\n Amount deposited {finale} ")

# Removes money from the balance
  def withdrawal(self):
    removal = float(input("\n Amount you want to remove: "))
    if self.b_balance <= removal:
      print("\n Insufficient balance")
      print(Fore.BLUE + "Please deposit first. Switching to DEPOSIT.")
      print(Style.RESET_ALL)
      ba.deposit()
    else:
      self.b_balance -= removal
      print(f"\n Amount you withdrew: {removal}")

# Creating Account

# Closing Account
  def close(self):
    pin_enter3 = int(input("Please enter your pin: "))
    if pin_enter3 != self.pin:
      print(" Sorry wrong pin")
      exit()
    else:
      ending_list = ["Account Officially Closed", "See you later", "Thats all", "Account removed", "Account Deleted", "Account ended"]
      Close_Endingb = random.choice(ending_list)
      Close_Ending = pyfiglet.figlet_format(Close_Endingb)
      print(Close_Ending)
      exit()

# Shows the balance
  def show(self):
    print(f"\n YOUR TOTAL BALANCE IS: ", self.b_balance)

# Lottery number chooser
# MATH ALGORTITHM SITUATION
# LOTTERY TICKET SELECTOR
# IF, ELIF, ELSE STATEMENTS
  def lottery(self):
    lotterynumbers = []
    for i in range(0,6):
      number = random.randint(1,110)
      while number in lotterynumbers:
        number = random.randint(1,110)
      lotterynumbers.append(number)
    lotterynumbers.sort()
    print(f"Todays lottery numbers are: {lotterynumbers}")
    for x in lotterynumbers:
      #print(x)
      winner  = random.randint(1,110)
      if winner in lotterynumbers:
        print("The number ", winner, " - Winner")
      else: 
        print("The number",x, "     ->>>    Loser")

# MAKES BANKING ACCOUNT CLASS BECOME VARIABLE
# EASES ACCESS
ba = Banking_Account()


choice = " "

# OUTSIDE OF THE CLASS
# Main MENU Choose Option Server
# PARAMETER
def main_menu(choice):
  while choice != 6:
    print(Fore.GREEN + "\t1. DEPOSIT AMOUNT")
    print("\t2. WITHDRAW AMOUNT")
    print("\t3. LOGIN / REGISTER")
    print("\t4. CLOSE AN ACCOUNT")
    print("\t5. CHECK BALANCE")
    print("\t6. SET UP A LOTTERY TICKET")
    print(Style.RESET_ALL)

    choice = input("Enter your decision: ")

    if choice == "1":
      ba.deposit()
  
    elif choice == "2":
      ba.withdrawal()

    elif choice == "3":
      ba.create()

    elif choice == '4':
      ba.close()

    elif choice == "5":
      ba.show()

    elif choice == "6":
      ba.lottery()

main_menu(choice)

















