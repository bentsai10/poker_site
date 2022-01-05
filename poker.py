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
            player.hand.sort(key=lambda x: x.value)
            # Pre Flop #
            if len(self.board) == 0:
                # Check for Pair #
                if player.hand[0].value == player.hand[1].value:
                    player.handValue = player.hand[0].value * 10 
                    player.handName = "Pocket " + player.hand[0].name + "s"
                # Check for High Card #
                else:
                    player.handValue = player.hand[1].value + player.hand[0].value/100
                    player.handName = player.hand[1].name + " High"
            # Flop #
            elif len(self.board) == 3:
                suits_in_hand = [card.suit for card in player.hand]
                values_in_hand = [card.value for card in player.hand]
                # Check for Royal Flush #
                # Check for Straight Flush #
                if len(set(suits_in_hand)) == 1:
                    if player.hand[0].value == player.hand[1].value - 1 and player.hand[1].value == player.hand[2].value - 1 and player.hand[2].value == player.hand[3].value - 1 and player.hand[3].value == player.hand[4].value - 1:
                        player.handValue = player.hand[4].value * 100000
                        if player.hand[4].value == 14:
                            player.handName = "Royal Flush"
                        else:
                            player.handName = player.hand[4].name + " High Straight Flush"
                        continue
                    elif player.hand[0].value == 2 and player.hand[1].value == 3 and player.hand[2].value == 4 and player.hand[3].value == 5 and player.hand[4].value == 14: 
                        player.handValue = player.hand[3].value * 100000
                        player.handName = player.hand[3].name + " High Straight Flush"
                        continue
                # Check for Quads #
                if len(set(values_in_hand)) == 2:
                    vals_in_hand = []
                    for i in range(len(player.hand)):
                        if player.hand[i].value in vals_in_hand:
                            player.handValue = player.hand[i].value * 1000
                            player.handName = "Quads with " + player.hand[i].name + "s"
                            break
                        else:
                            vals_in_hand.append(player.hand[i].value)
                    continue
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
    
    def flop(self, players):
        self.burn = []
        self.burn.append(str(self.deck.cards.pop()))
        for i in range(3):
            self.board.append(self.deck.cards.pop())
        for player in players:
            player.hand.extend(self.board)
        print("After the flop:", self.board, '\n')

    def turn(self):
        self.burn.append(str(self.deck.cards.pop()))
        self.board.append(self.deck.cards.pop())
        print("After the turn:", self.board, '\n')

    def river(self):
        self.burn.append(str(self.deck.cards.pop()))
        self.board.append(self.deck.cards.pop())
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
        self.handName = ""
        self.currentBet = 0
        
    def __str__(self):
        string = self.name + ' with '
        for i in range(len(self.hand)):
            string += '[ ' + str(self.hand[i]) + ' ] '
        string += "with a hand of " + str(self.handName) + ": " + str(self.handValue)
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
for i in range(5):
    # name = input("What is the name of Player " + str(i+1) + '? ')
    player = Player(str(i))
    players.append(player)

playingDeck = Deck()
hand = Hand(playingDeck, .2, .1)

hand.deal(players)

hand.flop(players)
players[0].hand = [Card('Spades', 14, 'Ace'), Card('Spades', 13, 'King'), Card('Spades', 12, 'Queen'), Card('Spades', 11, 'Jack'), Card('Spades', 10, 'Ten')]
players[1].hand = [Card('Spades', 10, 'Ten'), Card('Spades', 9, 'Nine'), Card('Spades', 8, 'Eight'), Card('Spades', 11, 'Jack'), Card('Spades', 12, 'Queen')]
players[2].hand = [Card('Spades', 10, 'Ten'), Card('Spades', 9, 'Nine'), Card('Spades', 13, 'King'), Card('Spades', 11, 'Jack'), Card('Spades', 12, 'Queen')]
players[3].hand = [Card('Spades', 9, 'Nine'), Card('Spades', 3, 'Three'), Card('Diamonds', 9, 'Nine'), Card('Clubs', 9, 'Nine'), Card('Hearts', 9, 'Nine')]
players[4].hand = [Card('Spades', 10, 'Ten'), Card('Spades', 9, 'Nine'), Card('Diamonds', 10, 'Ten'), Card('Clubs', 10, 'Ten'), Card('Hearts', 10, 'Ten')]


hand.evaluateHands(players)

for i in range(len(players)):
    print('Player ' + str(i + 1) + ' is ' + str(players[i]))
