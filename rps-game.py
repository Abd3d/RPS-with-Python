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
    if(value == "inputRPS"):
        while playerChooice == "":
            playerChooice = input(
                "Choose one: R for Rock, P for Paper, S for Sciessors, Q to Quit : ")
            playerChooice = playerChooice.lower()
            if(playerChooice != 'r' and playerChooice != 'p' and playerChooice != 's' and playerChooice != 'q'):
                playerChooice = ""


validation('inputRounds')
playerLives = numberOfRounds
computerLives = numberOfRounds
# =========== Step 4: Comparing Player and Computer Chooices ===========
# printResult function: print the result after comparing process


def printResult(win):
    if (win == 'w'):
        print(Fore.GREEN + playerName.upper() +
              " Wins," + Fore.RED + " Computer Loses")
    else:
        print(Fore.RED + playerName.upper() +
              " Loses, " + Fore.GREEN + "Computer Wins")

# =============Step 4:Comparing function: applay the game rules between user and computer choices


def comparing(pChooice, cChooice):
    global computerLives
    global playerLives

    if pChooice == cChooice:
        print(Fore.YELLOW + "Draw")
    elif pChooice == "Rock":
        if(cChooice != "Paper"):
            printResult('w')
            computerLives -= 1
        else:
            printResult('l')
            playerLives -= 1

    elif pChooice == "Paper":
        if(cChooice != "Scissors"):
            printResult('w')
            computerLives -= 1
        else:
            printResult('l')
            playerLives -= 1

    elif pChooice == "Scissors":
        if(cChooice != "Rock"):
            printResult('w')
            computerLives -= 1
        else:
            printResult('l')
            playerLives -= 1


# =========== Steps 3:Player chooices ===========
counter = 1
totalRounds = numberOfRounds
while numberOfRounds > 0:
    print(Back.LIGHTBLUE_EX + "Round " +
          str(counter) + " of " + str(totalRounds))

    validation("inputRPS")
    if playerChooice.lower() == 'q':
        quit = input("Press Y if you want to quit? ")
        if quit.lower() == 'y':
            exit()
        else:
            playerChooice = input(
                "Choose one: R for Rock, P for Paper, S for Sciessors, Q to Quit : ")
    computerChooice = rps[randint(0, 2)]
    if playerChooice.lower() == 'r':
        playerChooice = "Rock"
    elif playerChooice.lower() == 'p':
        playerChooice = "Paper"
    else:
        playerChooice = "Scissors"
    print(playerChooice + "   " + computerChooice)
    comparing(playerChooice, computerChooice)  # step 4
    numberOfRounds -= 1
    counter += 1
    playerChooice = ""
