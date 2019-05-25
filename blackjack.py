#!/usr/bin/env python3

import random

SUITS = ('SPADE', 'HEART', 'DIAMOND', 'CLUB')
RANKS = ('A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K')

class MainGame:

	def _draw_card(self, who, is_face_up):
		print("_draw_card " + who + " " + str(is_face_up))

	def player_draw(self):
		print("Player draw")

	def dealer_draw(self):
		print("Dealer draw")

#	def get_num_of_card(self):
#		return MainGame.num_of_card

	def judge(self):
		print("You win.")

class Card:
	def __init__(self, suit, rank):
		if (suit in SUITS) and (rank in RANKS):
			self.suit = suit
			self.rank = rank
		else:
			self.suit = None
			self.rank = None
			print( "Invalid card: ", suit, rank )

	def get_card(self):
		return (self.suit, self.rank)

class Stock:
	def __init__(self):
		self.Stock = [ Card(suit, rank) for suit in SUITS for rank in RANKS ]

	def shuffle(self):
		random.shuffle(self.Stock)

	def deal_card(self):
		return random.choice(self.Stock)

class Player:
	def __init__(self):
		print("skeleton")
#	def isContinue():
#		print("Continue? [yes/no]")

class Dealer:
	def __init__(self):
		pass

class GameManager:
	def __init__(self):
#		self.player = Player()
#		self.dealer = Dealer()
		self.name = "pythonBeginner"

def is_continue():
	ans = input("Continue? [yes/no]\n")
	if ans == "yes" or ans == "y" or ans == "Y":
		print("YES")
	elif ans == "no" or ans == "n" or ans == "N":
		print("NO")
		return False
	else:
		print("Invalid input.")
		return False

	return True

def main():
	print("===== Game Start ===== ")

	game = MainGame()
	game.player_draw()
	game.dealer_draw()
#	print(game.get_num_of_card())

	i = 0
#	card = Card()
	for suit in SUITS:
		for rank in RANKS:
			list = Card(suit, rank)
			print(list.get_card())
#			i += 1
	
#	print(list)

#	stock = Stock()
#	print(stock.deal_card())

	while True:
		if is_continue() == True:
			pass
		else:
			break

	game.judge()

if __name__ == '__main__':
	main()
