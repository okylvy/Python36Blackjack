#!/usr/bin/python3.6
#-*- coding:utf-8 -*-

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

	def judge(self):
		print("You win.")

def isContinue():
	print("Continue? [yes/no]")
	return False

def main():
	game = GameManager()

	print("===== Game Start ===== ")
	print("")

	while True:
		if not isContinue():
			break

	game.judge()

if __name__ == '__main__':
	main()
