# =========== Step1 : INTILIZATION ===========
# Main variables settings
import os
import colorama
from colorama import Fore
os.system('CLS')
rps = ["Rock", "Paper", "Scissors"]
print(Fore.LIGHTCYAN_EX + '\t**********************************')
print(Fore.LIGHTMAGENTA_EX + '\t*    ROCK PAPER SCISSORS GAME    *')
print(Fore.LIGHTMAGENTA_EX + '\t*            Version 1.0         *')
print(Fore.LIGHTCYAN_EX + '\t**********************************')
colorama.init(autoreset=True)
playerName = input("\n\n\tEnter Your Name Please: ")
playerChooice = ""
computerChooice = ""
numberOfRounds = 0
playerChooice = ""
computerLives = 0
playerLives = 0
# =========== Step 1: Game Rules ===========

print(Fore.CYAN + '\t***********************************')
print("\tWelcom " + playerName.upper() +
      " \n\tThere are three possible outcomes:\n \tDRAW, WIN or LOSS\n")
print("\tGame rules:")
print("\t----------")
print("\t" f'{Fore.GREEN}Rock    {Fore.YELLOW}Beats {Fore.RED}Scissors')
print("\t"f'{Fore.GREEN}Scissors {Fore.YELLOW}Beats {Fore.RED}Paper')
print("\t"f'{Fore.GREEN}Paper    {Fore.YELLOW}Beats {Fore.RED}Rock')
print(Fore.CYAN + '\t***********************************')
