"""
program: twodicegui.py
Author: Jude 11/18/2021

***Note: the file breezypythongui.py Must be in the same directory as this file for the application to work.
***
"""

from breezypythongui import EasyFrame
from tkinter.font import Font
import random

class TwoDice(EasyFrame):
	""" Displays multiple labels in a window."""

	def __init__(self):
		"""Sets up the window and the label."""
		EasyFrame.__init__(self, title = "Two Dice", background = "DarkSeaGreen", resizable = False, width = 320, height = 240)
		self.addLabel(text = "Two Dice ", row = 0, column = 0, columnspan = 2, sticky = "NSWE", font = Font(family = "courier", size = 20, weight = "bold"), background = "DarkSeaGreen", foreground = "white")

		# Labels and fields for the dice rolls
		self.addLabel(text = "Player's roll is:", row = 1, column = 0, background = "DarkSeaGreen")
		self.playRoll = self.addIntegerField(value = 0, row = 1, column = 1, state = "readonly")

		self.addLabel(text = "Computer's roll is:", row = 2, column = 0, background = "DarkSeaGreen")
		self.compRoll = self.addIntegerField(value = 0, row = 2, column = 1, state = "readonly")

		# The command method
		self.addButton(text = "Roll!", row = 3, column = 0, columnspan = 2, command  = self.playGame)
		# Label for the game finale result
		self.resultArea = self.addLabel(text = "", row = 4, column = 0, columnspan = 2, sticky = "NWES", background = "DarkSeaGreen", foreground = "yellow")

	def playGame(self):
		# Variables and constants
		playerDie = random.randint(1, 6)
		compDie = random.randint(1, 6)

		# Calculation phase
		if playerDie > compDie:
			result = "Congrats! You have won!"
			self.resultArea["foreground"] = "green"
			#self.resultArea["background"] = "white"
		elif compDie > playerDie:
			result = "Sorry, the computer wins."
			self.resultArea["foreground"] = "red"
		else:
			result = "We have a tie!"
			self.resultArea["foreground"] = "blue"

		# Output phase
		self.playRoll.setNumber(playerDie)
		self.compRoll.setNumber(compDie)
		self.resultArea["text"] = result

		

# definition of the main() function for program entry
def main():
	"""Instantiation and pops up the window."""
	TwoDice().mainloop()

# global call to trigger the main() function
if __name__ == "__main__":
	main()

