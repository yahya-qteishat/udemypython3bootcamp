''' we are coding the simple card game called war.

players draw cards, if one player draws a higher card, they get 
both cards passes back into their deck.

if both cards are equal, then players pull out an extra set of cards
whoever has the higher card wins all cards in the war back into their dekc

game keeps going till someone runs out of cards.

we will create card, deck, player classes and game logic '''


# card class holds suit, rank, value.


import random

values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7,
'Eight':8, 'Nine':9, 'Ten':10, 'Jack':11, 'Queen':12, 'King':13, 'Ace':14}

suits = ('Hearts','Diamonds','Spades','Clubs')

ranks = ('Two','Three','Four','Five','Six','Seven','Eight','Nine','Ten','Jack',
	'Queen','King','Ace')

class Card:

	def __init__(self,suit,rank):
		self.suit = suit
		self.rank = rank
		self.value = values[rank]

	def __str__(self):
		return self.rank + " of " + self.suit


two_hearts = Card("Hearts","Two")
three_of_clubs = Card("Clubs","Three")

# deck class will
# instantiate a new deck aka create all 52 card objects and holds a list of 
# cards objects. 

#Shuffle a deck through a method call
#randomly library shuffle function

#deal carsd from deck object using pop method from cards list

class Deck:

	def __init__(self):

		self.all_cards = []

		for suit in suits:
			for rank in ranks:

				# create a card object
				created_card = Card(suit,rank)
				self.all_cards.append(created_card)

	def shuffle(self):
		random.shuffle(self.all_cards)

	def deal_one(self):
		return self.all_cards.pop()


#print(mycard)

''' player class: this class will be used to hold a player's 
current list of cards.

a player should be able to add or remove cards from their hand aka their 
lst of card objecets.

we want player to eb able to add single or multple cards to hand

think ab translating hand of cards with a top and bottom to a python list

u can add somehting to the bottom using append

u can use the extend method to merge lists, it takes in a list

u cant use append becayse the list will become nested

'''

class Player:

	def __init__(self,name):
		self.name = name
		self.all_cards = []

	def remove_one(self):
		return self.all_cards.pop(0)

	def add_cards(self,new_cards):
		if type(new_cards) == type([]):
			self.all_cards.extend(new_cards)
		else:
			self.all_cards.append(new_cards)

	def __str__(self):
		return 'player {} has {} cards.'.format(self.name,len(self.all_cards))


### GAME LOGIC

''' we planned classes around the logic.

#game setup: creating the players '''

player_one = Player("One")
player_two = Player('Two)')

new_deck = Deck()
new_deck.shuffle()

#deal cards
for x in range(26):
	player_one.add_cards(new_deck.deal_one())
	player.two.add_cards(new_deck.deal_one())

game_on = True

round_num = 0

while game_on:
	round_num += 1
	print("round {}".format(round_num))

	if len(player_one.all_cards) == 0:
		print("Player 1 out of cards, player two wins!")
		game_on = False
		break
	if len(player_two.all_cards) == 0:
		print("Player 2 out of cards, player one wins!")
		game_on = False
		break

	# start a new round

	player_one_cardsinplay = []
	player_one_cardsinplay.append(player_one.remove_one())

	player_two_cardsinplay = []
	player_two_cardsinplay.append(player_two.remove_one())


	# check the cards against each other

	at_war = True

	while at_war:
		if player_two_cardsinplay[-1].value > player_two_cardsinplay[-1].value:
			player_one.add_cards(player_one_cardsinplay)
			plauer_one.add_cards(player_two_cardsinplay)
			at_war = False
		elif player_two_cardsinplay[-1].value < player_two_cardsinplay[-1].value:
			player_two.add_cards(player_one_cardsinplay)
			plauer_two.add_cards(player_two_cardsinplay)
			at_war = False
		else:
			print("War")
			if len(player_one.all_cards) < 3:
				print("Player one cant declare war")
				print("Player two wins")
				game_on = False
				break
			elif len(player_two.all_cards) < 3:
				print("Player two cant declare war")
				print("Player one wins")
				game_on = False
				break
			else:
				for num in range(5):
					player_one_cardsinplay.append(player_one.remove_one())
					player_one_cardsinplay.append(player_one.remove_one())

















