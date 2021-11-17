# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
import random

#define classes

class Card:
    def __init__(self, name, value, suit):
        self.name = name
        self.value = value
        self.suit = suit
    def __repr__(self):
        return self.name
    #__repr__ is the "represent" function. it allows us to display the name when printing an instance of a card.

class Deck:
    def __init__(self):
        self.cards =[
            #Spades
            Card("2♠", 2, "♠"),
            Card("3♠", 3, "♠"),
            Card("4♠", 4, "♠"),
            Card("5♠", 5, "♠"),
            Card("6♠", 6, "♠"),
            Card("7♠", 7, "♠"),
            Card("8♠", 8, "♠"),
            Card("9♠", 9, "♠"),
            Card("10♠", 10,"♠"),
            Card("J♠", 10, "♠"),
            Card("Q♠", 10, "♠"),
            Card("K♠", 10, "♠"),
            Card("A♠", 1, "♠"),
            #Hearts
            Card("2♥", 2, "♥"),
            Card("3♥", 3, "♥"),
            Card("4♥", 4, "♥"),
            Card("5♥", 5, "♥"),
            Card("6♥", 6, "♥"),
            Card("7♥", 7, "♥"),
            Card("8♥", 8, "♥"),
            Card("9♥", 9, "♥"),
            Card("10♥",10, "♥"),
            Card("J♥", 10, "♥"),
            Card("Q♥", 10, "♥"),
            Card("K♥", 10, "♥"),
            Card("A♥", 1, "♥"),
            #Diamonds
            Card("2♦", 2, "♦"),
            Card("3♦", 3, "♦"),
            Card("4♦", 4, "♦"),
            Card("5♦", 5, "♦"),
            Card("6♦", 6, "♦"),
            Card("7♦", 7, "♦"),
            Card("8♦", 8, "♦"),
            Card("9♦", 9, "♦"),
            Card("10♦",10, "♦"),
            Card("J♦", 10, "♦"),
            Card("Q♦", 10, "♦"),
            Card("K♦", 10, "♦"),
            Card("A♦", 1, "♦"),
            #Clubs
            Card("2♣", 2, "♣"),
            Card("3♣", 3, "♣"),
            Card("4♣", 4, "♣"),
            Card("5♣", 5, "♣"),
            Card("6♣", 6, "♣"),
            Card("7♣", 7, "♣"),
            Card("8♣", 8, "♣"),
            Card("9♣", 9, "♣"),
            Card("10♣", 10,"♣"),
            Card("J♣", 10, "♣"),
            Card("Q♣", 10, "♣"),
            Card("K♣", 10, "♣"),
            Card("A♣", 1, "♣")
        ]
        self.shuffle()
    def shuffle(self):
        random.shuffle(self.cards)
    def remove_card(self):
        return self.cards.pop(-1)

class Hand:
    def __init__(self):
        self.cards = []
    def add_card(self, card):
        self.cards.append(card)
    def get_score(self):
        score = 0
        has_ace = False
        for card in self.cards:
            score =(score + card.value)
            if card.value == 1:
                has_ace = True
        if has_ace == True and score <=11:
            score = (score + 10)
        return score


class Person:
    def __init__(self):
        self.hand = Hand()
        self.score = 0

class Player(Person):
    def __init__(self):
        super().__init__()
    #"super().__init__" will initiate the superclass, which is in this case person.

class Dealer(Person):
    def __init__(self):
        super().__init__()


#functions

def deal(person,deck):
    card = deck.remove_card()
    person.hand.add_card(card)
    #This function defines "card" as the card removed from the deck, then runs the "add_card" function associated with the class Hand.


#Running the game
#This is where I instantiate a deck called deck1, a player, and a dealer

player1 = Player()
dealer1 = Dealer()
deck1= Deck()

deal(player1,deck1)
deal(player1,deck1)
deal(dealer1,deck1)
deal(dealer1,deck1)

print("Welcome to Blackjack.")

#print("Deck:",str(deck1.cards)[1:-1])
print("Player's Hand:", str(player1.hand.cards)[1:-1])
print("Player's score:", player1.hand.get_score())
print("Dealer's Hand:",dealer1.hand.cards[0],"[]")
print(" ")

player_score = player1.hand.get_score()
dealer_score = dealer1.hand.get_score()

if player_score == 21:
    print("Blackjack! Player wins")
    exit(0)

move = input("(h)it or (s)tay?")

#hit
while move == "h" and player_score < 21:
    deal(player1,deck1)
    player_score = player1.hand.get_score()
    print("Player's Hand:", str(player1.hand.cards)[1:-1])
    print("Player's score:", player1.hand.get_score())
    print("Dealer's Hand:", dealer1.hand.cards[0], "[]")
    print(" ")
    if player_score == 21:
        print("21! Player wins!")
        exit(0)
    if player_score > 21:
        print("Bust! Player loses!")
        exit(0)
    move = input("(h)it or (s)tay?")

#stay
if move == "s":
    print("Player's Hand:", str(player1.hand.cards)[1:-1])
    print("Player's score:", player1.hand.get_score())
    print("Dealer's Hand:", str(dealer1.hand.cards)[1:-1])
    print("Dealer's Score:", str(dealer_score))
    print(" ")
    while dealer_score < 17:
        print("Dealer hits:")
        deal(dealer1,deck1)
        dealer_score = dealer1.hand.get_score()
        print("Player's Hand:", str(player1.hand.cards)[1:-1])
        print("Player's score:", player1.hand.get_score())
        print("Dealer's Hand:", str(dealer1.hand.cards)[1:-1])
        print("Dealer's Score:", str(dealer_score))
        print(" ")

if dealer_score > 21:
    print("Dealer Busts! Player wins!")
    exit(0)



#troubleshooter

#deck1 = Deck()
#hand1 = Hand()
#card = deck1.remove_card()
#hand1.add_card(card)
#print("Deck:",deck1.cards)
#print("Hand:",hand1.cards)


