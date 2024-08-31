from random import randint
from itertools import combinations

class TwoPlayers:
	def __init__(self):
		self.possibilities = [[1,2,3], [4,5,6], [7,8,9], [1,4,7], [2,5,8], [3,6,9], [1,5,9], [3,5,7]]
		self.player_x = []
		self.player_o = []
		self.game_over_message = ""
		self.guide_message = ""
		self.result_found = False

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
		#Note: self.result_found is to prevent the program from checking other combinations that aren't a straight line particularly for "player_o"
		for _ in list(combinations(self.player_x, 3)):
			if sorted(list(_)) in self.possibilities:
				self.game_over_message = "X wins"
				self.result_found = True
				break #This break statement stops the loop and prevent the program from checking other combinations that aren't a straight line
			elif (len(self.player_x) + len(self.player_o)) == 9 and (sorted(list(_)) not in self.possibilities):
				self.game_over_message = "We have a draw"
				self.result_found = True

		#Checking if we have a winner/loser/a draw for player O
		for _ in list(combinations(self.player_o, 3)):
			if self.result_found == False: #If we didn't find a straight line(a win) in "player's choices"
				if sorted(list(_)) in self.possibilities:
					self.game_over_message = "O wins"
					break #This break statement stops the loop and prevent the program from checking other combinations that aren't a straight line
				elif (len(self.player_x) + len(self.player_o)) == 9 and (sorted(list(_)) not in self.possibilities):
					self.game_over_message = "We have a draw"

class SinglePlayer:
	def __init__(self, level="Easy"):
		self.possibilities = [[1,2,3], [4,5,6], [7,8,9], [1,4,7], [2,5,8], [3,6,9], [1,5,9], [3,5,7]]
		self.player_choices = []
		self.computer_choices = []
		self.result_found = False
		self.game_over_message = "Computer Wins"
		self.level = level
		#Note: game over message here ("Computer Wins") is different from the final game over message "Computer wins"
		#I did this to stop the timer, sort of, in "main.py". It is very confusing to explain and loads of text will be used to explain it
		#So i didn't fully explain it but just wanted to state that out

		if level not in ["Easy","Medium","Hard","Impossible"]:
			raise Exception("Levels value must be 'Easy','Medium','Hard' or 'Impossible'")

	def playersTurn(self, grid):
		if grid not in tuple(range(1,10)):
			raise Exception("'grid' must be in range of (1-9)")

		#This exception checks if a player has picked a number that has been choosen
		#by the computer or themselves(the player)
		if grid in self.player_choices or grid in self.computer_choices:
			raise KeyError(f'This number {grid} has been choosen')

		self.player_choices.append(grid)

		self.result()

	def computersTurn(self):
		def computer_guess():
			#Here, the "grid" is actually a box(number) picked by the computer at random
			self.grid = randint(1,9) #Default mode which is "Easy" mode

			if self.grid in self.computer_choices or self.grid in self.player_choices:
				if len(self.computer_choices) + len(self.player_choices) < 9:
					#This if block above is to prevent to computer from guessing a box(number) even if there are not boxes left or 1-9 are filled
					computer_guess() #Run(guess) again if the number has been picked by the player or the computer previously
		computer_guess()

		self.computer_choices.append(self.grid)

		self.result()

	def result(self):
		self.players_outcomes = list(combinations(sorted(self.player_choices), 3))
		self.computer_outcomes = list(combinations(sorted(self.computer_choices), 3))
	
		#Checking if we have a winner/loser/a draw for Player/User
		#Note: self.result_found is to prevent the program from checking other combinations that aren't a straight line particularly for "computers_choices"
		for _ in list(combinations(self.player_choices, 3)):
			if sorted(list(_)) in self.possibilities:
				self.game_over_message = "Player wins"
				self.result_found = True
				break #This break statement stops the loop and prevent the program from checking other combinations that aren't a straight line
			elif (len(self.player_choices) + len(self.computer_choices)) == 9 and (sorted(list(_)) not in self.possibilities):
				self.game_over_message = "We have a draw"
				self.result_found = True

		#Checking if we have a winner/loser/a draw for Computer
		for _ in list(combinations(self.computer_choices, 3)):
			if self.result_found == False: #If we didn't find a straight line(a win) in "player's choices"
				if sorted(list(_)) in self.possibilities:
					self.game_over_message = "Computer wins"
					break #This break statement stops the loop and prevent the program from checking other combinations that aren't a straight line
				elif (len(self.player_choices) + len(self.computer_choices)) == 9 and (sorted(list(_)) not in self.possibilities):
					self.game_over_message = "We have a draw"

if __name__ == "__main__":
	if False:
		#Testing the "TwoPlayer" class
		two_players = TwoPlayers()
		two_players.play(2)
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

	else:
		#Testing the "SinglePlayer" class
		single_player = SinglePlayer()
		single_player.playersTurn(1)
		print(single_player.player_choices)
		single_player.computersTurn()
		print(single_player.computer_choices)
		single_player.playersTurn(3)
		print(single_player.player_choices)
		single_player.computersTurn()
		print(single_player.computer_choices)
		single_player.playersTurn(5)
		print(single_player.player_choices)
		single_player.computersTurn()
		print(single_player.computer_choices)
		single_player.playersTurn(9)
		print(single_player.player_choices)
		single_player.computersTurn()
		print(single_player.computer_choices)
		print(single_player.game_over_message)