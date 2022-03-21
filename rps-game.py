# ROCK PAPER SCISSORS GAME
# =========== IMPORT SECTION ===========
import colorama
from colorama import Fore, Back
from random import randint

# =========== Step1 : INTILIZATION ===========
# To rest color code in command window
colorama.init(autoreset=True)
# Main variables settings
rps = ["Rock", "Paper", "Scissors"]
playerName = input("Enter Your Name Please: ")
playerChooice = ""
computerChooice = ""
numberOfRounds = 0
playerChooice = ""

# =========== Step 1: Game Rules ===========
print(Fore.CYAN + '***********************************')
print("\tWelcom " + playerName.upper() +
      " \nThere are three possible outcomes:\n \tDRAW, WIN or LOSS\n")
print("\tGame rules:")
print("\t----------")
print("\t" f'{Fore.GREEN}Rock     {Fore.YELLOW}Beats {Fore.RED}Scissors')
print("\t"f'{Fore.GREEN}Scissors {Fore.YELLOW}Beats {Fore.RED}Paper')
print("\t"f'{Fore.GREEN}Paper    {Fore.YELLOW}Beats {Fore.RED}Rock')
print(Fore.CYAN + '***********************************')

# ============= Validation Input Function :
# Step2: inputRounds: to check if the input is number and between 1 to 10


def validation(value):
    global numberOfRounds
    global playerChooice
    if(value == 'inputRounds'):
        while numberOfRounds == 0:
            numberOfRounds = input(
                "How many rounds do you want to play? between [1 to 10]: ")
            if (numberOfRounds.isnumeric() is True):
                numberOfRounds = int(numberOfRounds)
                if (numberOfRounds < 1 or numberOfRounds > 10):
                    numberOfRounds = 0
            else:
                numberOfRounds = 0


validation('inputRounds')
playerLives = numberOfRounds
computerLives = numberOfRounds
