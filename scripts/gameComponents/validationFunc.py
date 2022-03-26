import colorama
from colorama import Back
from gameComponents import setting
# ============= Validation Input Function :
# Step2: inputRounds: to check if the input is number and between 1 to 10


def validation(value):

    if(value == 'inputRounds'):
        while setting.numberOfRounds == 0:
            setting.numberOfRounds = input(
                "\tHow many rounds do you want to play? between [1 to 10]: ")
            if (setting.numberOfRounds.isnumeric() is True):
                setting.numberOfRounds = int(setting.numberOfRounds)
                if (setting.numberOfRounds < 1 or setting.numberOfRounds > 10):
                    setting.numberOfRounds = 0
            else:
                setting.numberOfRounds = 0
    if(value == "inputRPS"):
        while setting.playerChooice == "":
            setting.playerChooice = input(
                "\tChoose one: R for Rock, P for Paper, S for Sciessors, Q to Quit : ")
            setting.playerChooice = setting.playerChooice.lower()
            if(setting.playerChooice != 'r' and setting.playerChooice != 'p' and setting.playerChooice != 's' and setting.playerChooice != 'q'):
                setting.playerChooice = ""
