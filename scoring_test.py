import pandas as pd
import numpy as np
import itertools
from collections import Counter

def evaluateHand(hand):
    suits_in_hand = [card[:1] for card in hand]
    values_in_hand = [int(card[1:]) for card in hand]
    values_in_hand.sort()
    suits_set = set(suits_in_hand)
    values_set = set(values_in_hand)
    value_count = Counter(values_in_hand)
    difference = max(values_in_hand) - min(values_in_hand)
    # Check for Royal Flush #
    # Check for Straight Flush #
    # Range of Values: (101, 110) #
    if len(suits_set) == 1:
        if len(values_set) == 5 and difference == 4 :
            score = 120 + values_in_hand[-1]
            if max(values_in_hand) == 14:
                handName = "Royal Flush"
                #print('%s is a %s:, with score: %s' % (hand, handName,score)) 
                return score
            else:
                handName = card_dict[values_in_hand[-1]] + " High Straight Flush"
                #print('%s is a %s:, with score: %s' % (hand, handName,score)) 
                return score
        elif values_in_hand[0] == 2 and values_in_hand[1] == 3 and values_in_hand[2] == 4 and values_in_hand[3] == 5 and values_in_hand[-1] == 14:
            score = 120 + values_in_hand[-2]
            handName = card_dict[values_in_hand[-2]] + " High Straight Flush"
            #print('%s is a %s:, with score: %s' % (hand, handName,score)) 
            return score
    # Check for Quads #
    # Check for Full House #
    if len(values_set) == 2:
        if value_count.most_common(1)[0][1] == 4:
            # Range of Values: (88, 100) #
            dominant_value = value_count.most_common(1)[0][0]
            score = 105 + dominant_value
            handName = "Quads with " + card_dict[dominant_value] + "s"
            #print('%s is a %s:, with score: %s' % (hand, handName,score)) 
            return score
        else:
            # Range of Values: (75, 88) #
            dominant_value = value_count.most_common(2)[0][0]
            score = 90 + dominant_value + value_count.most_common(2)[1][0]/100
            handName = card_dict[dominant_value] + "s full with " + card_dict[value_count.most_common(2)[1][0]] + "s"
            #print('%s is a %s:, with score: %s' % (hand, handName,score))    
            return score
    # Check for Flush #
    # Range of Values: (67, 75) (lowest flush w/o straight flush is 7 high) #
    if len(suits_set) == 1:
        handName = card_dict[values_in_hand[-1]] + " High Flush"
        score = 75 + values_in_hand[-1] + values_in_hand[-2]/100 + values_in_hand[-3]/1000 + values_in_hand[-4]/10000 + values_in_hand[-5]/100000
        #print('%s is a %s:, with score: %s' % (hand, handName,score)) 
        return score
    # Check for Straight #
    # Range of Values: (55, 66) #
    if len(values_set) == 5 and difference == 4:
        score = 60 + values_in_hand[-1]
        handName = card_dict[values_in_hand[-1]] + " High Straight"
        #print('%s is a %s:, with score: %s' % (hand, handName,score)) 
        return score
    if values_in_hand[0] == 2 and values_in_hand[1] == 3 and values_in_hand[2] == 4 and values_in_hand[3] == 5 and values_in_hand[-1] == 14: 
        score = 60 + values_in_hand[3]
        handName = card_dict[values_in_hand[3]] + " High Straight"
        #print('%s is a %s:, with score: %s' % (hand, handName,score)) 
        return score
    # Check for Trips #
    # Check for Two Pair #
    if len(values_set) == 3:
        if value_count.most_common(1)[0][1] == 3:
            # Range of Values: (42, 55) #
            handName = "Trips with " + card_dict[value_count.most_common(1)[0][0]] + "s"
            score = 45 + value_count.most_common(3)[0][0] + max([value_count.most_common(3)[1][0], value_count.most_common(3)[2][0]])/100 + min([value_count.most_common(3)[1][0], value_count.most_common(3)[2][0]])/1000
            #print('%s is a %s:, with score: %s' % (hand, handName,score)) 
            return score
        else:
            # Range of Values: (29, 41) #
            handName = "Two Pair with " + card_dict[value_count.most_common(2)[0][0]] + "s and " + card_dict[value_count.most_common(2)[1][0]] + "s"
            score = 30 + max([value_count.most_common(3)[0][0], value_count.most_common(3)[1][0]]) + min([value_count.most_common(3)[0][0], value_count.most_common(3)[1][0]])/100 + value_count.most_common(3)[2][0]/1000
            #print('%s is a %s:, with score: %s' % (hand, handName,score)) 
            return score
    # Check for Pair #
    # Check for High Card #
    if value_count.most_common(1)[0][1] == 2:
        other_vals = []
        for i in range(1, len(value_count.most_common(4))):
            other_vals.append(value_count.most_common(4)[i][0])
        other_vals.sort(reverse= True)
        handName = "Pair of " + card_dict[value_count.most_common(1)[0][0]] + "s"
        score = 15 + value_count.most_common(1)[0][0] + other_vals[0]/100 + other_vals[1]/1000 + other_vals[2]/10000
        #print('%s is a %s:, with score: %s' % (hand, handName,score)) 
        return score
    else:
        handName = card_dict[values_in_hand[-1]] + " High"
        score = values_in_hand[-1] + values_in_hand[-2]/100 + values_in_hand[-3]/1000 + values_in_hand[-4]/10000 + values_in_hand[-5]/100000
        #print('%s is a %s:, with score: %s' % (hand, handName,score)) 
        return score
     
def combinations(arr, n):
    arr = np.asarray(arr)
    t = np.dtype([('', arr.dtype)]*n)
    print(t)
    result = np.fromiter(itertools.combinations(arr, n), t)
    return result.view(arr.dtype).reshape(-1, n)

def handvalues(combinations):
    scores =[{"hand": i, "value": evaluateHand(i)} for i in combi] # We iterate over all combinations scoring them
    scores = sorted(scores, key = lambda k: k['value']) # We sort hands by score
    return scores

    
deck = Deck().getCards() # We create our deck
combi = combinations(deck,5) # We create an array containing all possible 5 cards combinations
hand_values = handvalues(combi)
x = [i.get("hand","") for i in hand_values] # making a list of hands
y = [i.get("value","") for i in hand_values] #making a list of values

data = {'hands':x, 'value':y} # making a dictionary of hands and values

df = pd.DataFrame(data) # making a pandas dataframe with hands and values
pd.set_option("display.max_rows", None, "display.max_columns", None)

print(df)