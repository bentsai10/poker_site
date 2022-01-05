import random

card_suits = ['Spades', 'Hearts', 'Diamonds', 'Clubs']
card_values = [14, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
card_names = ['Ace', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King']

class Card:
    def getSuit(self):
        return self.suit

    def getValue(self):
        return self.value

    def getName(self):
        return self.name

    def __init__(self, suit, value, name):
        self.suit = suit
        self.value = value
        self.name = name

    def __str__(self):
     return '[' + self.name + ' of ' + self.suit + ']'

class Deck:
    def getCards(self):
        return self.cards

    def __init__(self):
        cards = []
        for suit in card_suits:
            for i in range(len(card_values)):
                card = Card(suit, card_values[i], card_names[i])
                cards.append(card)
        for i in range(5):
            random.shuffle(cards)
        self.cards = cards
    
    def __str__(self):
        string = ''
        print(len(self.cards))
        for i in range(len(self.cards)):
            substring = '[' + str(self.cards[i]) + ']\n'
            string += substring
        return string

class Hand: 
    def evaluateHands(self, players):
        for player in players:
            # Pre Flop #
            if len(self.board) == 0:
                # Check for Pair #
                if player.hand[0].value == player.hand[1].value:
                    player.handValue = player.hand[0].value * 2 * 10 / len(player.hand)
                # Check for High Card #
                else:
                    player.handValue = max([player.hand[0].value, player.hand[1].value])
            # Flop #
            elif len(self.board) == 3:
                pass
                # Check for Royal Flush #
                # Check for Straight Flush #
                # Check for Quads #
                # Check for Full House #
                # Check for Flush #
                # Check for Straight #
                # Check for Trips #
                # Check for Two Pair #
                # Check for Pair #
                # Check for High Card #
            # Turn #
            elif len(self.board) == 4:
                pass
                # Check for Royal Flush #
                # Check for Straight Flush #
                # Check for Quads #
                # Check for Full House #
                # Check for Flush #
                # Check for Straight #
                # Check for Trips #
                # Check for Two Pair #
                # Check for Pair #
                # Check for High Card #
            # River #
            else:
                pass
                # Check for Royal Flush #
                # Check for Straight Flush #
                # Check for Quads #
                # Check for Full House #
                # Check for Flush #
                # Check for Straight #
                # Check for Trips #
                # Check for Two Pair #
                # Check for Pair #
                # Check for High Card #
                
            
    def deal(self, players):
        for i in range(2):
            for j in range(len(players)):
                player = players[j]
                player.hand.append(self.deck.cards.pop())
    
    def flop(self):
        self.burn = []
        self.burn.append(str(self.deck.cards.pop()))
        for i in range(3):
            self.board.append(str(self.deck.cards.pop()))
        print("After the flop:", self.board, '\n')

    def turn(self):
        self.burn.append(str(self.deck.cards.pop()))
        self.board.append(str(self.deck.cards.pop()))
        print("After the turn:", self.board, '\n')

    def river(self):
        self.burn.append(str(self.deck.cards.pop()))
        self.board.append(str(self.deck.cards.pop()))
        print("After the river:", self.board, '\n')

    def __init__(self, deck, bigBlind, smallBlind):
        self.deck = deck
        self.board = []
        self.bigBlind = bigBlind
        self.smallBlind = smallBlind
        self.currentAmountToCall = bigBlind
        self.pot = bigBlind + smallBlind
    

class Player:
    def buyIn(self, buyInAmt):
        self.stack = buyInAmt

    def __init__(self, name):
        self.name = name
        self.hand = []
        self.handValue = 0
        self.currentBet = 0
        
    def __str__(self):
        string = self.name + ' with '
        for i in range(len(self.hand)):
            string += '[ ' + str(self.hand[i]) + ' ] '
        string += "with a hand strength of " + str(self.handValue)
        return string + '\n'

###
# Setup
###
validPlayers = False
validBuyIn = False

# while validPlayers == False:
#     numPlayersExpected = input("How many players are playing? (2-6) ")
#     try:
#         numPlayers = int(numPlayersExpected)
#         if numPlayers >= 2 and numPlayers <= 6:
#             validPlayers = True
#         else:
#             print('Invalid number of players!')
#     except:
#         print('Invalid number of players!')

players = []
for i in range(2):
    # name = input("What is the name of Player " + str(i+1) + '? ')
    player = Player(str(i))
    players.append(player)

playingDeck = Deck()
hand = Hand(playingDeck, .2, .1)

hand.deal(players)
hand.evaluateHands(players)

for i in range(len(players)):
    print('Player ' + str(i + 1) + ' is ' + str(players[i]))
