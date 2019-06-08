#!/usr/bin/env python3
import random

SUITS = ('SPADE', 'HEART', 'DIAMOND', 'CLUB')
RANKS = ('A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K')

class MainGame:
	def __draw_card(self):
		card = Card()
		return card.draw_card()

	def player_draw(self):
		card = self.__draw_card()
		print("Player draw {}".format(card))
		num = card[1]
		if num == 'J' or num == 'Q' or num == 'K':
			num = 10
		elif num == 'A':
			num = 1
		else:
			num = int(num)
		return num

	def dealer_draw(self):
		card = self.__draw_card()
		print("Dealer draw {}".format(card))
		num = card[1]
		if num == 'J' or num == 'Q' or num == 'K':
			num = 10
		elif num == 'A':
			num = 1
		else:
			num = int(num)
		return num

	def dealer_draw_hide(self):
		card = self.__draw_card()
		print("Dealer draw ***")
		num = card[1]
		if num == 'J' or num == 'Q' or num == 'K':
			num = 10
		elif num == 'A':
			num = 1
		else:
			num = int(num)
		return num

	def dealers_turn(self, player_sum, dealer_sum):
		# Dealer draws until the sum is 17 or more.
		dealer_card = self.dealer_draw()
		dealer_sum += dealer_card
		while True:
			if dealer_sum > 21:
				print("Dealer's bust! [Dealer] Sum = {}".format(dealer_sum))
				print("===== RESULT =====")
				print('You win!')
				break
			elif dealer_sum >= 17 and dealer_sum <=21:
				print("[Dealer] Sum = {}".format(dealer_sum))
				print("===== RESULT =====")
				break
				if player_sum > dealer_sum:
					print("===== RESULT =====")
					print("You win!")
					break
				elif player_sum == dealer_sum:
					print("===== RESULT =====")
					print("Even!")
					break
				else:
					print("===== RESULT =====")
					print("You lose!")
					break
			else:
				pass

	def judge(self):
		print("You win.")

class Card:
	'''
	def __init__(self):
		for suit in SUITS:
			for rank in RANKS:
				stock = [suit, rank]

		if (suit in SUITS) and (rank in RANKS):
			self.suit = suit
			self.rank = rank
		else:
			self.suit = None
			self.rank = None
			print( "Invalid card: ", suit, rank )
	'''

	def draw_card(self):
		suit_index = random.randint(0, len(SUITS)-1)
		rank_index = random.randint(0, len(RANKS)-1)
#		return (self.list(suit_index, rand_index))
		return (SUITS[suit_index], RANKS[rank_index])

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
	print("===== Game Start =====")

	player_sum = 0
	dealer_sum = 0

	main_game = MainGame()

	player_card = main_game.player_draw()
	player_sum += player_card
	player_card = main_game.player_draw()
	player_sum += player_card

	dealer_card = main_game.dealer_draw()
	dealer_sum += dealer_card
	dealer_card = main_game.dealer_draw_hide()
	dealer_sum += dealer_card

	print("")
	print("[Player] Current Sum: {}".format(player_sum))

	# Print all of the cards.
#	list = []
#	i = 0
	'''
	for suit in SUITS:
		for rank in RANKS:
			list = Card(suit, rank)
			print(list.draw_card())
	'''
#			list.append(Card(suit, rank))
#			i += 1
#			print(list.draw_card())
#	for x in list:
#		print(x)
#	print(list.draw_card())

	# Draw 52 cards randomly.


	while True:
		if is_continue() == True:
			player_card = main_game.player_draw()
			player_sum += player_card
			print('')
			# Bust check.
			if player_sum > 21:
				print('Bust! You lose.')
				break
			print('')
			print('[Player] Current Sum: {}'.format(player_sum))
		else:
			main_game.dealers_turn(player_sum, dealer_sum)
			break

if __name__ == '__main__':
	main()
