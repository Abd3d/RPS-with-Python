# ROCK PAPER SCISSORS GAME
# =========== IMPORT SECTION ===========
import winsound
import colorama
from colorama import Fore, Back
from random import randint
from gameComponents import setting, validationFunc, roundResult, winner
# To rest color code in command window
colorama.init(autoreset=True)

# =========== Steps 3:Player chooices ===========
counter = 1
totalRounds = setting.numberOfRounds
while setting.numberOfRounds > 0:
    print(Back.LIGHTBLUE_EX + "Round " +
          str(counter) + " of " + str(totalRounds))

    validationFunc.validation("inputRPS")
    if setting.playerChooice.lower() == 'q':
        quit = input("\tPress (y / Y) if you want to quit? ")
        if quit.lower() == 'y':
            print(Fore.GREEN + "\tGood by!!!")
            winsound.PlaySound("SystemExit", winsound.SND_ALIAS)
            exit()
        else:
            setting.playerChooice = input(
                "\tChoose one: R for Rock, P for Paper, S for Sciessors, Q to Quit : ")
    setting.computerChooice = setting.rps[randint(0, 2)]
    if setting.playerChooice.lower() == 'r':
        setting.playerChooice = "Rock"
    elif setting.playerChooice.lower() == 'p':
        setting.playerChooice = "Paper"
    else:
        setting.playerChooice = "Scissors"
    print("\t" + setting.playerChooice + "   " + setting.computerChooice)
    roundResult.comparing(setting.playerChooice,
                          setting.computerChooice)  # step 4
    setting.numberOfRounds -= 1
    counter += 1
    setting.playerChooice = ""

winner.displayResult()
