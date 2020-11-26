# Name: Jamar Hill
# Date: 11/25/2020
# Description: Assignment 9


"""Write a class that allows two players to play a game where they choose numbers 1-9 in trying to select a secret value"""

print("Hello! This game is called the Add Three Game.")
print("This game allows players to alternately choose numbers from 1-9.")
print("The goal is to have the sum of their guesses equal a secret value.")
print("If at any point exactly three of the player's numbers sum to exactly the secret value, then that player has won.")
print("If all numbers form 1-9 are chosen, but neither player has won, then the game ends in a draw")

class AddThreeGame:

    # Initialize the files
    def __init__(self): #Create private data members

        self.__ply1 = 0
        self.__ply2 = 0
        self.__guesses = []
        self.__gamepos = "UNFINISHED"

    # Defines current state of the game
    def get_current_state(self):

        return self.__gamepos

    # Defines Action created by player moves
    def make_move(self, ply, x):

        if x in self.__guesses:
            return False #Returns false if input has been played

        if x > 9 or x < 1: #Sets parameter of X being greater than 1 and less than 9
            return False #Returns false if input is outside of the parameter

        if ply == "first":
            self.__ply1 = self.__ply1 + x
            self.__guesses.append(x)#Removes selection

        elif ply == "second":
            self.__ply2 = self.__ply2 + x
            self.__guesses.append(x)#Removes selection

        if len(self.__guesses) > 4  and  self.__ply1 == 15:
            self.__gamepos = "FIRST_WON" #ply1==15 establishes player 1 as the winner after 3 guesses

        elif len(self.__guesses) > 4 and self.__ply2 == 15:
            self.__gamepos = "SECOND_WON"#ply2==15 establishes player 2 as the winner after 3 guesses

        if len(self.__guesses) == 9:#Establishes that is the len of guess == 9 the game will end in a draw
            self.__gamepos = "DRAW"

        return True


#initialize class as follows
game = AddThreeGame()

# The game will loop until it concludes
while True:

    x = int(input("Player 1 please enter a number: "))
    while True:
        if (game.make_move("first", x) == True):
            break
        else:
            x = int(input("Player 1's selection is outside of the game parameters. please try another selection: "))

    # plyrscore checks the current status of the game
    plyrscore = game.get_current_state()

    if plyrscore == "FIRST_WON": #Establishes player 1 as the winner if parameter is met.
        print("Player 1 is the winner!!!\n")
        break

    elif plyrscore == "SECOND_WON": #Establishes player 2 as the winner if parameter is met.
        print("Player 2 is the winner!!!\n")
        break

    elif plyrscore == "DRAW": #Establishes draw if len == 9.
        print("Neither Player 1 or Player 2 successfully guessed the secret number. Game ends in draw.\n")
        break

    x = int(input("Player 2 please enter a number:"))
    # Loop a prompt to enter a guess if the parameter is not met. Exits loop if true.
    while True:
        if (game.make_move("second", x) == True):
            break
        else:
            #informs user that guess is outside of the parameters
            x = int(input("Player 2's selection is outside of the game parameters. please try another selection: "))
    # plyrscore checks the current status of the game
    plyrscore = game.get_current_state()

    if plyrscore == "UNFINISHED": #Informs user that parameter has not been met. Initiates the next round.
        print("Neither player has successfully reached the secret value. Please try again.\n")

    elif plyrscore == "FIRST_WON": # Indentifies player one as the winner
        print("Player 1 is the winner!!!\n")
        break

    elif plyrscore == "SECOND_WON": #identifies player two as the winner
        print("Player 2 is the winner!!!\n")
        break

    elif plyrscore == "DRAW": #Informs user that neither player has entered the secret value and ends game.
        print("Neither Player 1 or Player 2 successfully guessed the secret value. Game ends in draw\n")
        break