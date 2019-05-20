#!/usr/bin/env python3
#-*- coding:utf-8 -*-

class MainGame:
	def player_draw(self):
		print("Player draw")

	def dealer_draw(self):
		print("Dealer draw")

	def judge(self):
		print("You win.")

class Stock:
	def __init__(self):
		pass

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
	else:
		print("Invalid input.")
	
	return False

def main():

	print("===== Game Start ===== ")

	game = MainGame()
	game.player_draw()
	game.dealer_draw()

	while True:
		if not is_continue():
			break

	game.judge()

if __name__ == '__main__':
	main()
