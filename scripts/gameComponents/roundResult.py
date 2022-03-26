import colorama
from colorama import Fore
from gameComponents import setting, validationFunc

# printResult function: print the result after comparing process

validationFunc.validation('inputRounds')


def printResult(win):
    if (win == 'w'):
        print(Fore.GREEN + "\t" + setting.playerName.upper() +
              " Wins," + Fore.RED + " Computer Loses")
    else:
        print(Fore.RED + "\t" + setting.playerName.upper() +
              " Loses, " + Fore.GREEN + "Computer Wins")


setting.playerLives = setting.numberOfRounds
setting.computerLives = setting.numberOfRounds
# =========== Step 4: Comparing Player and Computer Chooices ===========


def comparing(pChooice, cChooice):

    if pChooice == cChooice:
        print(Fore.YELLOW + "\t" + "Draw")
    elif pChooice == "Rock":
        if(cChooice != "Paper"):
            printResult('w')
            setting.computerLives -= 1
        else:
            printResult('l')
            setting.playerLives -= 1

    elif pChooice == "Paper":
        if(cChooice != "Scissors"):
            printResult('w')
            setting.computerLives -= 1
        else:
            printResult('l')
            setting.playerLives -= 1

    elif pChooice == "Scissors":
        if(cChooice != "Rock"):
            printResult('w')
            setting.computerLives -= 1
        else:
            printResult('l')
            setting.playerLives -= 1
