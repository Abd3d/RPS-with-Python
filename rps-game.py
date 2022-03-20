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
playerLives = numberOfRounds
computerLives = numberOfRounds
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
