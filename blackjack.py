#!/usr/bin/env python3
import random
import sys
from time import sleep

class MainGame:
	def __init__(self, player_sum, dealer_sum):
		card = Card()
		self.deck = card.make_deck()
		self.player_sum = player_sum
		self.dealer_sum = dealer_sum

	def __draw_card(self):
		card = Card()
		card_num = card.get_card(len(self.deck)) - 1
		drawn_card = self.deck[card_num]
		del self.deck[card_num]
		return drawn_card

	def __add_num(self, who, card):
		num = card[1]
		if num == 'J' or num == 'Q' or num == 'K':
			num = 10
		elif num == 'A':
			num = 1
		else:
			num = int(num)

		if who == 'player':
			self.player_sum += num
			if self.__is_burst(self.player_sum) == False:
				print("===== RESULT =====")
				print("You're burst! [Player] Sum = {}".format(self.player_sum))
				sys.exit(0)
		elif who == 'dealer':
			self.dealer_sum += num
		else:
			print('{} isn not here'.format(player))

	def __is_burst(self, sum):
		if sum > 21:
			return False
		else:
			return True

	def get_player_sum(self):
		return self.player_sum

	def get_dealer_sum(self):
		return self.dealer_sum

	def player_draw(self):
		card = self.__draw_card()
		print("Player draw {}".format(card))
		self.__add_num('player', card)
		print("Player Sum = ", self.get_player_sum())  # DEBUG

	def dealer_draw(self):
		card = self.__draw_card()
		print("Dealer draw {}".format(card))
		self.__add_num('dealer', card)
		print("Dealer Sum = ", self.get_dealer_sum())  # DEBUG

	def dealer_draw_hide(self):
		card = self.__draw_card()
		print("Dealer draw ***")
		self.__add_num('dealer', card)
		return card

	def dealers_turn(self, dealers_2nd_card):
		# Dealer draws until the sum is 17 or more.
		print("Dealer's 2nd card was " + str(dealers_2nd_card))
		while self.get_dealer_sum() <= 17:
			print("DDDDD")
			card = self.__draw_card()
			print("Dealer draw {}".format(card))
			self.__add_num('dealer', card)
			if self.get_dealer_sum() > 21:
				print("===== RESULT =====")
				print("Dealer's burst! [Dealer] Sum = {}".format(dealer_sum))
				print('You win!')
			sleep(1)

	def judge(self):
		player_sum = self.get_player_sum()
		dealer_sum = self.get_dealer_sum()
		if player_sum > dealer_sum:
				print("===== RESULT =====")
				print('[Player] {} vs [Dealer] {}'.format(player_sum, dealer_sum))
				print('You win!')
		elif player_sum < dealer_sum:
				print("===== RESULT =====")
				print('[Player] {} vs [Dealer] {}'.format(player_sum, dealer_sum))
				print('You lose!')
		else:
				print("===== RESULT =====")
				print('[Player] {} vs [Dealer] {}'.format(player_sum, dealer_sum))
				print('Even!')

class Card:
	SUITS = ('SPADE', 'HEART', 'DIAMOND', 'CLUB')
	RANKS = ('A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K')

	def make_deck(self):
		deck = []
		for suit in Card.SUITS:
			for rank in Card.RANKS:
				deck.append((suit, rank))
		return deck

	def get_card(self, deck_len):
		if deck_len == 0:
			print('No card anymore!')
			sys.exit(0)
		card = random.randint(1, deck_len)
		return card

def is_continue():
	print('Draw card? [yes/no]')
	while True:
		ans = input()
		if ans == 'yes' or ans == 'y' or ans == 'Y':
			return True
		elif ans == 'no' or ans == 'n' or ans == 'N':
			return False
		else:
			print('Type "yes" or "no"')

def main():
	print("===== Game Start =====")

	player_init = 0
	dealer_init = 0
	main_game = MainGame(player_init, dealer_init)

	main_game.player_draw()
	main_game.player_draw()
	main_game.dealer_draw()
	dealers_2nd_card = main_game.dealer_draw_hide()

	# Main game loop.
	while is_continue() == True:
		main_game.player_draw()

	main_game.dealers_turn(dealers_2nd_card)

	main_game.judge()

if __name__ == '__main__':
	main()
