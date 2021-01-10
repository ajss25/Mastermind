# Mastermind
# The game will set the solution each game by randomly selecting four pegs and arranging them.
# The pegs include: Red, Orange, Yellow, Green, Blue, and Purple.
# Players have 8 attempts to guess the correct color and sequence of four pegs (e.g. ROYG).
# After each attempt, player will be provided with hints to influence their next set of attempts.
# The sequence can use any combination of colors, including two or more of the same color.

import os
import sys
import random

class Mastermind:
	def __init__(self):
		# get terminal size to center display in terminal, initialize six pegs
		self.terminal_size = os.get_terminal_size().columns
		self.pegs = ['R', 'O', 'Y', 'G', 'B', 'P']

		# for each game instance, randomly create solution and keep track of player guesses and feedback to provide
		self.solution = random.choices(self.pegs, k=4)
		self.player_guesses = 1
		self.feedback = []

	# rules and instructions before starting game
	def game_start(self):
		print("\n")
		print("MASTERMIND".center(self.terminal_size))
		print("\n")
		print("Do you have what it takes to become a Mastermind?".center(self.terminal_size))
		print("\n")
		print("HOW TO PLAY:".center(self.terminal_size))
		print("There are total six available pegs: Red | Orange | Yellow | Green | Blue | Purple".center(self.terminal_size))
		print("The game will set the solution by randomly selecting four pegs and arranging them".center(self.terminal_size))
		print("To win, guess the correct color sequence of four pegs by typing in your guessing sequence (e.g. ROYG)".center(self.terminal_size))
		print("\n")
		print("HINTS ALONG THE WAY:".center(self.terminal_size))
		print("Black - number of pegs that are correct color and in correct position".center(self.terminal_size))
		print("White - number of pegs that are correct color but in the wrong position".center(self.terminal_size))
		print("Null - number of pegs that are not in the solution".center(self.terminal_size))
		print("ex) Solution: ROBB | Guess: BBBY -> Black: 1 | White: 1 | Null: 2".center(self.terminal_size))
		print("\n")
		print("Any combination of colors can be used, including two or more of the same color".center(self.terminal_size))
		print("You have a total of 8 attempts per game".center(self.terminal_size))
		print("\n")
		input("PRESS ENTER TO START".center(self.terminal_size))
		print("\n")
		self.take_guess()
	
	# prompt player to enter guesses and call the verification function
	def take_guess(self):
		while self.player_guesses <= 8:
			player_attempt = list(input("\n TAKE A GUESS: "))

			# make sure the player's guess is the correct size using allowed colors
			while len(player_attempt) != 4 or any(peg not in self.pegs for peg in player_attempt):
				player_attempt = list(input("\n INVALID INPUT, TRY AGAIN: "))
			self.verification(player_attempt)

	# verification algorithm that checks player's guess against the solution to provide hints
	def verification(self, player_attempt):
		if player_attempt == self.solution:
			self.game_end()

		# store instances of player's attempt and game instance's solution to separate lists
		attempt_tracker = player_attempt[:]
		solution_tracker = self.solution[:]
		
		# initialize feedback pegs to provide hints
		black = white = null = 0

		# count number of pegs with correct color and position
		for i, peg in enumerate(attempt_tracker):
			if peg == solution_tracker[i]:
				black += 1
				attempt_tracker[i] = "X"
				solution_tracker[i] = "X"
		
		# count number of pegs with correct color but incorrect position
		for i, peg in enumerate(attempt_tracker):
			if peg != "X" and peg in solution_tracker:
				white += 1
				solution_tracker[solution_tracker.index(peg)] = "X"
				attempt_tracker[i] = "X"

		# count number of pegs not in the solution
		null = 4 - (black + white)

		# keep track of user attempts and hints after each turn
		hints = "Black: " + str(black) + " White: " + str(white) + " Null: " + str(null)
		self.feedback.append("[ Attempt " + str(self.player_guesses) + ": " + ''.join(player_attempt) + " - " + hints + " ]")
		for hint in self.feedback:
			print(''.join(hint).center(self.terminal_size))

		# limit player to 8 attempts
		self.player_guesses += 1
		if self.player_guesses > 8:
			self.game_end()

	# ends the game if user guessed the correct solution or exhausted all attempts
	def game_end(self):
		if self.player_guesses == 1:
			print("\n")
			print(str("You are a Mastermind! It took only " + str(self.player_guesses) + " try!").center(self.terminal_size))
		elif self.player_guesses <= 8:
			print("\n")
			print(str("You are a Mastermind after " + str(self.player_guesses) + " tries!").center(self.terminal_size))
		else:
			print("\n")
			print(str("You exhausted all 8 attempts. The solution was: " + ' '.join(self.solution)).center(self.terminal_size))
		
		# option to replay or exit the game
		while True:
			print("\n")
			replay_or_exit = input("Enter: Y - play again | N - exit \n".center(self.terminal_size))
			if replay_or_exit.lower() == "y":
				# restart the program
				os.execl(sys.executable, sys.executable, *sys.argv)

			elif replay_or_exit.lower() == "n":
				# clear the terminal and terminate the program
				os.system('cls' if os.name == 'nt' else 'clear')
				exit()

# clear the terminal, instantiate and start the game
if __name__ == "__main__":
	os.system('cls' if os.name == 'nt' else 'clear')
	game_instance = Mastermind()
	game_instance.game_start()
