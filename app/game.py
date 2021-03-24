
from random import choice



valid_options = ["rock", "paper", "scissors"]

def my_func(choice1, choice2):
    """
    Params:
        choice1 and choice 2 are both strings (either 'rock', 'paper' or 'scissors')
    """
    winners = {
        "rock": {
            "rock": None,
            "paper" : "paper",
            "scissors" : "scissors",
        },
        "paper" : {
            "rock" : "paper",
            "paper" : None,
            "scissors" : "scissors",
        }
        "scissors" : {
            "rock":
            "paper":
            "scissors"
        }
    }


if __name__ == '__main__':
    
    #
    # USER SELECTION
    #

    u = input("Please choose one of 'Rock', 'Paper', or 'Scissors': ").lower()
    print("USER CHOICE:", u)
    if u not in valid_options:
        print("OOPS, TRY AGAIN")
        exit()

    #
    # COMPUTER SELECTION
    #

    c = choice(valid_options)
    print("COMPUTER CHOICE:", c)

    #
    # DETERMINATION OF WINNER
    #

    winner = determine_winner()

    if winner == u:
        print("YOU WON!")
    elif winner == c:
        print("COMPUTER WON!")
    elif winner == None:
        print("TIE")

    #if u == "rock":
    #    if c == "rock":
    #        print("It's a tie!")
    #    elif c == "paper":
    #        print("The computer wins")
    #    elif c == "scissors":
    #        print("The user wins")
    #elif u == "paper":
    #    if c == "rock":
            

    #elif u == "scissors":


    #use a single dictionary




