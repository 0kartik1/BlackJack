import random

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
cards = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
Val = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':10,'Queen':10, 'King':10, 'Ace':11}

class card:
	"""docstring for card"""
	def __init__(self):
		self.deck = []
		for suit in suits:
			for card in cards:
				se

	def __str__(self):
		return "{} of {}".format(self.suit,self.value)





