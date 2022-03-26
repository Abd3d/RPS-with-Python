
import colorama
from colorama import Back, Fore
from gameComponents import setting
# ******************** Step 5: Print the Result *****************


def displayResult():
    if(setting.computerLives == setting.playerLives):
        print(Back.YELLOW + Fore.BLACK +
              "\n\t\t\tThe Result is Draw!!")
    elif (setting.computerLives > setting.playerLives):
        print(Back.RED + "\n\t\t\tGame Over; Try Again!")
    else:
        print(Back.GREEN + "\n\t\t\t" + str(setting.playerName).upper() +
              " Is The Winner!!")
