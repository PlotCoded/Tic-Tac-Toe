from random import randint
from itertools import combinations

class TwoPlayers:
	def __init__(self):
		self.possibilities = [[1,2,3], [4,5,6], [7,8,9], [1,4,7], [2,5,8], [3,6,9], [1,5,9], [3,5,7]]
		self.player_x = []
		self.player_o = []
		self.game_over_message = ""
		self.guide_message = ""

	def play(self, grid):
		#The if  and elif statement condition checks if the player to play if X or O.
		#It is done by checking if the sum of the player grid/boxes is even or odd.
		#If even, it is X's turn
		#If odd, it is O's turn
		if type(grid) != int or (grid not in [1,2,3,4,5,6,7,8,9]):
			raise Exception('The "grid" argument must be an integer from 1-9')

		if (len(self.player_x) + len(self.player_o)) % 2 == 0: #This is even so it's X's turn now
			self.turn = "O"
			self.player_x.append(grid)
			self.guide_message = f"It is player {self.turn}'s turn now"

		elif (len(self.player_x) + len(self.player_o)) % 2 == 1: #This is odd so it's O turn now
			self.turn = "X"
			self.player_o.append(grid)
			self.guide_message = f"It is player {self.turn}'s turn now"

		#Checking if we have a winner/loser/a draw for player X
		for _ in list(combinations(self.player_x, 3)):
			if sorted(list(_)) in self.possibilities:
				self.game_over_message = "X wins"
				print(self.game_over_message)
			elif (len(self.player_x) + len(self.player_o)) == 9:
				self.game_over_message = "We have a draw"
				print(self.game_over_message)

		#Checking if we have a winner/loser/a draw for player O
		for _ in list(combinations(self.player_o, 3)):
			if sorted(list(_)) in self.possibilities:
				self.game_over_message = "O wins"
				print(self.game_over_message)
			elif (len(self.player_x) + len(self.player_o)) == 9:
				self.game_over_message = "We have a draw"
				print(self.game_over_message)

class SinglePlayer:
	def __init__(self, player="X", computer="O",level="Easy"):
		self.player = player.upper()
		self.computer = computer
		self.possibilities = [[1,2,3], [4,5,6], [7,8,9], [1,4,7], [2,5,8], [3,6,9], [1,5,9], [3,5,7]]
		self.player_choices = []
		self.computer_choices = []

		if self.player not in ("X","O"):
			raise Exception("Player's Letter' must be 'X' or 'O'")

	def PlayersTurn(self, player_number_choice):
		if player_number_choice not in tuple(range(1,10)):
			raise Exception("'player_number_choice' must be in range of (1-9)")

		#This exception doesn't check for invalid input, but check if a player has
		#picked a number that has bee choosesn by the computer or themselves
		if player_number_choice in self.player_choices or player_number_choice in self.computer_choices:
			raise KeyError(f'This number {player_number_choice} has been choosen')

		self.player_number_choice = player_number_choice
		self.player_choices.append(self.player_number_choice)

		self.Result()

	def ComputersTurn(self):
		def computer_guess():
			self.computer_number_choice = randint(1,9)

			if self.computer_number_choice in self.computer_choices or self.computer_number_choice in self.player_choices:
				computer_guess()
		computer_guess()

		self.computer_choices.append(self.computer_number_choice)

		self.Result()

	def Result(self):
		self.players_outcomes = list(combinations(sorted(self.player_choices), 3))
		self.computer_outcomes = list(combinations(sorted(self.computer_choices), 3))
	
		self.result = 'It\'s a draw'

		for line in self.computer_outcomes:
			for lane in self.possibilities:
				if list(line) == lane:
					self.result = 'You lose'
					self.scores["player"]+=1
					self.result_founded = True
					break

		for line in self.players_outcomes:
			for lane in self.possibilities:
				if list(line)  == lane:
					self.result = 'You win'
					self.scores["computer"]+=1
					self.result_founded = True
					break

	def Delete(self):
		if len(self.player_choices) > 1:
			del self.player_choices[len(self.player_choices)-1]
		if len(self.computer_choices) > 1:
			del self.computer_choices[len(self.computer_choices)-1]

if __name__ == "__main__":
	two_players = TwoPlayers()
	two_players.play(20)
	print(two_players.guide_message)
	two_players.play(8)
	print(two_players.guide_message)
	two_players.play(1)
	print(two_players.guide_message)
	two_players.play(4)
	print(two_players.guide_message)
	two_players.play(3)
	print(two_players.guide_message)
	two_players.play(5)
	print(two_players.guide_message)
	print(two_players.player_x, two_players.player_o)
	print(two_players.game_over_message)

"""To find accurate information about this source code and its details, try the HTML Documentation
in this folder"""