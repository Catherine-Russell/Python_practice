square_dict = {}
for num in range(1, 11):
    square_dict[num] = num*num
print(square_dict)

friends = ["cat", "kate", "kerri", "Beth"]
card_suit = ["hearts", "spades", "diamonds", "clubs"]

MISTAKE = {friend : card_suit for friend in friends} ## This just assigns the entire list to each friend name

import random   
friend_card_assignment = {friend : random.choice(card_suit) for friend in friends}

card_as_key = {card : random.choice(friends) for card in card_suit}
print(MISTAKE)
print(friend_card_assignment)
print(card_as_key)

## nb these ones sometimes double up on card/friend. To make sure there's only one of each do this:

from random import shuffle
shuffle(card_suit)
card_friends = {friend : card for (friend, card) in zip(friends, card_suit)}
print(card_friends)

## Another practice with zip and dictionary comprehension
print("\n \n Using zip and dictionary comprehension:\n")

pupils = ["Arav", "Yasmin", "Osman", "Ahadu", "Yanni"]
team_roles = ["leader", "scribe", "observer", "illustrator", "summariser"]

without_zip = {pupil : random.choice(team_roles) for pupil in pupils}
print("Randomised but without zip function: " + str(without_zip))

from random import shuffle
shuffle(team_roles)
with_zip = {pupil : role for (pupil, role) in zip(pupils, team_roles)}
print("Randomised and with zip: " + str(with_zip))

###
print("\n \n Using update")

