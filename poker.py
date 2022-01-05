import random
from collections import Counter


card_suits = ['Spades', 'Hearts', 'Diamonds', 'Clubs']
card_dict = {
    14: 'Ace',
    2: 'Two', 
    3: 'Three', 
    4: 'Four', 
    5: 'Five', 
    6: 'Six', 
    7: 'Seven', 
    8: 'Eight', 
    9: 'Nine', 
    10: 'Ten', 
    11: 'Jack', 
    12: 'Queen',
    13: 'King',
}

class Card:
    def getSuit(self):
        return self.suit

    def getValue(self):
        return self.value

    def __init__(self, suit, value):
        self.suit = suit
        self.value = value

    def __str__(self):
     return '[' + card_dict[self.value] + ' of ' + self.suit + ']'

class Deck:
    def getCards(self):
        # return [card.suit[:1] + str(card.value) for card in self.cards]
        return [card.suit[:1] + str(card.value) for card in self.cards]

    def __init__(self):
        cards = []
        for suit in card_suits:
            for value, name in card_dict.items():
                card = Card(suit, value)
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
                    player.handName = "Pocket " + card_dict[player.hand[0].value] + "s"
                # Check for High Card #
                else:
                    player.handValue = player.hand[1].value + player.hand[0].value/100
                    player.handName = card_dict[player.hand[1].value] + " High"
            # Flop #
            elif len(self.board) == 3:
                suits_in_hand = [card.suit for card in player.hand]
                values_in_hand = [card.value for card in player.hand]
                suits_set = set(suits_in_hand)
                values_set = set(values_in_hand)
                value_count = Counter(values_in_hand)
                difference = values_in_hand[-1] - values_in_hand[0]
                # Check for Royal Flush #
                # Check for Straight Flush #
                # Range of Values: (101, 110) #
                if len(suits_set) == 1:
                    if difference == 4 and len(values_set) == 5:
                        player.handValue = 120 + player.hand[4].value
                        if player.hand[4].value == 14:
                            player.handName = "Royal Flush"
                        else:
                            player.handName = card_dict[player.hand[4].value] + " High Straight Flush"
                        continue
                    elif player.hand[0].value == 2 and player.hand[1].value == 3 and player.hand[2].value == 4 and player.hand[3].value == 5 and player.hand[4].value == 14: 
                        player.handValue = 120 + player.hand[3].value
                        player.handName = card_dict[player.hand[3].value] + " High Straight Flush"
                        continue
                # Check for Quads #
                # Check for Full House #
                if len(values_set) == 2:
                    if value_count.most_common(1)[0][1] == 4:
                        # Range of Values: (88, 100) #
                        dominant_value = value_count.most_common(1)[0][0]
                        player.handValue = 105 + dominant_value
                        player.handName = "Quads with " + card_dict[dominant_value] + "s"
                    else:
                        # Range of Values: (75, 88) #
                        dominant_value = value_count.most_common(2)[0][0]
                        player.handValue = 90 + dominant_value + value_count.most_common(2)[1][0]/100
                        player.handName = card_dict[dominant_value] + "s full with " + card_dict[value_count.most_common(2)[1][0]] + "s"
                    continue   
                # Check for Flush #
                # Range of Values: (67, 75) (lowest flush w/o straight flush is 7 high) #
                if len(suits_set) == 1:
                    player.handName = card_dict[player.hand[4].value] + " High Flush"
                    player.handValue = 75 + player.hand[4].value + player.hand[3].value/100 + player.hand[2].value/1000 + player.hand[1].value/10000 + player.hand[0].value/100000
                    continue
                # Check for Straight #
                # Range of Values: (55, 66) #
                if difference == 4 and len(values_set) == 5:
                    player.handValue = 60 + player.hand[4].value
                    player.handName = card_dict[player.hand[4].value] + " High Straight"
                    continue
                if player.hand[0].value == 2 and player.hand[1].value == 3 and player.hand[2].value == 4 and player.hand[3].value == 5 and player.hand[4].value == 14: 
                    player.handValue = 60 + player.hand[3].value 
                    player.handName = card_dict[player.hand[3].value] + " High Straight"
                    continue
                # Check for Trips #
                # Check for Two Pair #
                if len(values_set) == 3:
                    if value_count.most_common(1)[0][1] == 3:
                        # Range of Values: (42, 55) #
                        player.handName = "Trips with " + card_dict[value_count.most_common(1)[0][0]] + "s"
                        player.handValue = 45 + value_count.most_common(3)[0][0] + max([value_count.most_common(3)[1][0], value_count.most_common(3)[2][0]])/100 + min([value_count.most_common(3)[1][0], value_count.most_common(3)[2][0]])/1000
                        continue
                    else:
                        # Range of Values: (29, 41) #
                        player.handName = "Two Pair with " + card_dict[value_count.most_common(2)[0][0]] + "s and " + card_dict[value_count.most_common(2)[1][0]] + "s"
                        player.handValue = 30 + max([value_count.most_common(3)[0][0], value_count.most_common(3)[1][0]]) + min([value_count.most_common(3)[0][0], value_count.most_common(3)[1][0]])/100 + value_count.most_common(3)[2][0]/1000
                        continue
                # Check for Pair #
                # Check for High Card #
                if value_count.most_common(1)[0][1] == 2:
                    other_vals = []
                    for i in range(1, len(value_count.most_common(4))):
                        other_vals.append(value_count.most_common(4)[i][0])
                    other_vals.sort(reverse= True)
                    player.handName = "Pair of " + card_dict[value_count.most_common(1)[0][0]] + "s"
                    player.handValue = 15 + value_count.most_common(1)[0][0] + other_vals[0]/100 + other_vals[1]/1000 + other_vals[2]/10000
                    continue
                else:
                    player.handName = card_dict[player.hand[4].value] + " High"
                    player.handValue = player.hand[4].value + player.hand[3].value/100 + player.hand[2].value/1000 + player.hand[1].value/10000 + player.hand[0].value/100000
                    continue

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
        print("After the flop:", str(self.board[0]), str(self.board[1]), str(self.board[2]), '\n')

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

# ###
# # Setup
# ###
# validPlayers = False
# validBuyIn = False

# # while validPlayers == False:
# #     numPlayersExpected = input("How many players are playing? (2-6) ")
# #     try:
# #         numPlayers = int(numPlayersExpected)
# #         if numPlayers >= 2 and numPlayers <= 6:
# #             validPlayers = True
# #         else:
# #             print('Invalid number of players!')
# #     except:
# #         print('Invalid number of players!')

players = []
for i in range(8):
    # name = input("What is the name of Player " + str(i+1) + '? ')
    player = Player(str(i))
    players.append(player)

playingDeck = Deck()
hand = Hand(playingDeck, .2, .1)

hand.deal(players)
hand.evaluateHands(players)
players.sort(key=lambda x: x.handValue, reverse= True)
for player in players:
    print(player)
hand.flop(players)
hand.evaluateHands(players)
players.sort(key=lambda x: x.handValue, reverse= True)
for player in players:
    print(player)



