import random
from random import randint
import time
#To create deck of the cards
class Card:
    def __init__(self, name, health, power):
        self.name = name
        self.health = health
        self.power = power

decks = []
decks.append(Card("Jon", 100, 1000))
decks.append(Card("Arya", 200, 700))
decks.append(Card("Bran", 500, 750))
decks.append(Card("Sansa", 400, 800))
decks.append(Card("Sandor", 350,600))
decks.append(Card("Ramsay", 650, 300))
decks.append(Card("Khal", 800, 550))
decks.append(Card("Lord", 900, 600))
random.shuffle(decks)

# Creating deck for the players
Deck_player = []
Deck_system = []
Deck_outdated = []

while len(decks) > 0:
    Deck_player.append(decks.pop(0))
    Deck_system.append(decks.pop(0))
#Roll the dice to pick up the card from the deck


print(" Character CARDS GAME: Player1 vs Player2!")
def dice_roll():
    global rotationplayer
    print("Player 1 it's your turn.   Type 'roll' to roll the dice  ")
    userOneInput = input(">>>")
    if userOneInput == "roll":
        valueOne = randint(1,6)
        print("Player 1 rolled ", valueOne)
        print(" Player 2 it's your turn.         Type 'roll' to roll the dice  ")
        userTwoInput = input("")
    if userTwoInput == "roll":
        valueTwo = randint(1,6)
        print("Player 2 rolled ",  valueTwo)
        if valueOne > valueTwo:
                print("Player 1 wins and he will pick up the First card from the deck! ")
                rotationplayer  = True
        elif valueOne < valueTwo:
                print("Player 2 wins and he will pick up the First card from the deck! ")
                rotationplayer  = False
        else:
            print("It's a draw!")
            dice_roll()
dice_roll()
#start the game
#rotationplayer = True

# Response for the strenghth of the character x stand for Health and y stand for Power
player_inputs = ["x", "y"]

# Intial ponit of the player1 and player2
player1 = 0
player2 = 0
Godspellctp = 0
Godspellctc = 0
Respellctp = 0
Respellctc = 0

Respell = "no"
Respell1 = "no"
while len(Deck_player) > 0 and len(Deck_system) > 0:

    time.sleep(1)
    if rotationplayer  == True:
        #player1 resurrect spell
        ra = 0
        if (Respellctp == 0 and len(Deck_outdated) > 1 and ra == 0):
            Respell = input("Player1, Would you like to play Resurrect Spell? yes or no: ")
            if (Respell == "yes" and Respellctp == 0):
                a1 = random.randint(1,len(Deck_outdated))
                playerCard = Deck_outdated.pop(int(a1)-1)
                Deck_outdated.append(playerCard)
                Respellctp = 1
                ra = 1
            else:
                playerCard = Deck_player.pop(0)
                Deck_outdated.append(playerCard)
        else:
            playerCard = Deck_player.pop(0)
            Deck_outdated.append(playerCard)

        print("PLAYER1 CARD")
        print("Name:", playerCard.name)
        print("x. Health:", playerCard.health)
        print("y. Power:", playerCard.power)
        answer = input("Player1, which strenth would like to challenge? input x for Health or y for Power")

        while player_inputs.count(answer) == 0:
            answer = input("That isn't a valid answer, please try again: ")
        #player1 god spell
        if (Godspellctp == 0  and len(Deck_system) > 1 and ra == 0):
            gspell = input("Player1, do you want to play God Spell? yes or no: ")
            if (gspell == "yes" and Godspellctp == 0):
                Godspellctp = 1
                lec = len(Deck_system)
                print("No of cards in Player2 deck:", lec)
                cardno = input("Which card number from Player2 deck? ")
                if (Respellctc == 0 and len(Deck_outdated) > 1):
                    Respell1 = input("Player2, do you want to play Resurrect Spell? yes or no: ")
                    if (Respell1 == "yes" and Respellctc == 0):
                        z2 = random.randint(1,len(Deck_outdated))
                        mn = Deck_outdated.pop(int(z2)-1)
                        Deck_system.insert(0,mn)
                        choice = input("Player1: a. Select resurrected card or b. Select earlier choice ")
                        if (choice == "a"):
                            computerCard = Deck_system.pop(0)
                            Deck_outdated.append(computerCard)
                            Respellctc = 1
                        else:
                            computerCard = Deck_system.pop(int(cardno)-1)
                            Deck_outdated.append(computerCard)
                            Respellctc = 1
                    else:
                        computerCard = Deck_system.pop(int(cardno)-1)
                        Deck_outdated.append(computerCard)
                else:
                    computerCard = Deck_system.pop(int(cardno)-1)
                    Deck_outdated.append(computerCard)

            else:
                computerCard = Deck_system.pop(0)
                Deck_outdated.append(computerCard)

        else:
            computerCard = Deck_system.pop(0)
            Deck_outdated.append(computerCard)

        print("PLAYER2 CARD")
        print("Name:", computerCard.name)
        print("x. Health:", computerCard.health)
        print("y. Power", computerCard.power)


    else:
        #player2 resurrect spell
        rb = 0
        if (Respellctc == 0 and len(Deck_outdated) > 1 and rb == 0):
            Respell1 = input("Player2, do you want to play Resurrect Spell? yes or no: ")
            if (Respell1 == "yes" and Respellctc == 0):
                z2 = random.randint(1,len(Deck_outdated))
                computerCard = Deck_outdated.pop(int(z2)-1)
                Deck_outdated.append(computerCard)
                Respellctc = 1
                rb = 1
            else:
                computerCard = Deck_system.pop(0)
                Deck_outdated.append(computerCard)
        else:
            computerCard = Deck_system.pop(0)
            Deck_outdated.append(computerCard)


        print("PLAYER2 CARD")
        print("Name:", computerCard.name)
        print("x. Health:", computerCard.health)
        print("y. Power", computerCard.power)

        answer = input("Player2, which Strength do you challenge? ")
        print("Player2 chooses", answer)

         #Player2 god spell
        if (Godspellctc == 0 and len(Deck_player) > 1 and rb == 0):
            Godspell1 = input("Player2, Would  you like to play God Spell? yes or no: ")
            if (Godspell1 == "yes" and Godspellctc == 0):
                Godspellctc = 1
                lep = len(Deck_player)
                print("No of cards in Player1 deck:", lep)
                cardno1 = input("Which card number from Player1 deck? ")
                if (Respellctp == 0 and len(Deck_outdated) > 1):
                    Respell = input("Player1, Would  you like to play Resurrect Spell? yes or no: ")
                    if (Respell == "yes" and Respellctp == 0):
                        a1 = random.randint(1,len(Deck_outdated))
                        nm = Deck_outdated.pop(int(a1)-1)
                        Deck_player.insert(0,nm)
                        choice1 = input("Player2: a. To take resurrected card or b. Take earlier choice ")
                        if (choice1 == "a"):
                            playerCard = Deck_player.pop(0)
                            Deck_outdated.append(playerCard)
                            Respellctp = 1
                        else:
                            playerCard = Deck_player.pop(int(cardno1)-1)
                            Deck_outdated.append(playerCard)
                            Respellctp = 1
                    else:
                        playerCard = Deck_player.pop(int(cardno1)-1)
                        Deck_outdated.append(playerCard)
                else:
                    playerCard = Deck_player.pop(int(cardno1)-1)
                    Deck_outdated.append(playerCard)
            else:
                playerCard = Deck_player.pop(0)
                Deck_outdated.append(playerCard)

        else:
            playerCard = Deck_player.pop(0)
            Deck_outdated.append(playerCard)

        print("PLAYER1 CARD")
        print("Name:", playerCard.name)
        print("a. Health:", playerCard.health)
        print("b. Power:", playerCard.power)


    playerWins = False
    #comparing cards of player1 and player2
    if answer == "x":
        playerWins = (playerCard.health > computerCard.health)
    elif answer == "y":
        playerWins = (playerCard.power > computerCard.power)
        time.sleep(1)

    #who wins the hand?
    if playerWins:
        print("Player1 wins this hand!")
        player1=player1+1
        rotationplayer = True
    else:
        print("Player2 wins this hand!")
        player2=player2+1
        rotationplayer = False
time.sleep(2)
#who wins the Game?
def win_game():
    print("Total point of Player 1 is ",  player1)
    print("Total point of Player 2 is ",  player2)

if player1<player2:
    print("PLAYER2 WINS THE Game!")
    win_game()
elif player1>player2:
    print("PLAYER1 WINS THE Game!")
    win_game()

else:
    print("IT'S A TIE!")
    win_game()

time.sleep(4)
