from random import randint
from itertools import combinations
from random import choice

class TwoPlayers:
    def __init__(self):
        self.possibilities = [[1,2,3], [4,5,6], [7,8,9], [1,4,7], [2,5,8], [3,6,9], [1,5,9], [3,5,7]]
        self.player_x = []
        self.player_o = []
        self.game_over_message = ""
        self.guide_message = ""
        self.result_found = False

    def play(self, grid):
        if type(grid) != int or (grid not in [1,2,3,4,5,6,7,8,9]):
            raise Exception('The "grid" argument must be an integer from 1-9')

        if (len(self.player_x) + len(self.player_o)) % 2 == 0: 
            self.turn = "O"
            self.player_x.append(grid)
            self.guide_message = f"It is player {self.turn}'s turn now"

        elif (len(self.player_x) + len(self.player_o)) % 2 == 1: 
            self.turn = "X"
            self.player_o.append(grid)
            self.guide_message = f"It is player {self.turn}'s turn now"

        for _ in list(combinations(self.player_x, 3)):
            if sorted(list(_)) in self.possibilities:
                self.game_over_message = "X wins"
                self.result_found = True
                break
            elif (len(self.player_x) + len(self.player_o)) == 9 and (sorted(list(_)) not in self.possibilities):
                self.game_over_message = "We have a draw"
                self.result_found = True

        for _ in list(combinations(self.player_o, 3)):
            if self.result_found == False:
                if sorted(list(_)) in self.possibilities:
                    self.game_over_message = "O wins"
                    break
                elif (len(self.player_x) + len(self.player_o)) == 9 and (sorted(list(_)) not in self.possibilities):
                    self.game_over_message = "We have a draw"

class SinglePlayer:
    def __init__(self, level="Hard"):
        self.possibilities = [[1,2,3], [4,5,6], [7,8,9], [1,4,7], [2,5,8], [3,6,9], [1,5,9], [3,5,7]]
        self.player_choices = []
        self.computer_choices = []
        self.result_found = False
        self.game_over_message = "Computer Wins"
        self.level = level

        if level not in ["Easy", "Medium", "Hard", "Impossible"]:
            raise Exception("Levels value must be 'Easy','Medium','Hard' or 'Impossible'")

    def playersTurn(self, grid):
        if grid not in tuple(range(1,10)):
            raise Exception("'grid' must be in range of (1-9)")

        if grid in self.player_choices or grid in self.computer_choices:
            raise KeyError(f'This number {grid} has been choosen')

        self.player_choices.append(grid)
        self.result()

    def computersTurn(self):
        def computer_guess():
            self.doNoThink = lambda: randint(1, 9)
            self.move = choice([self.doNoThink, self.think])

            if self.level == "Easy":
                self.grid = randint(1, 9)
            elif self.level in ["Medium", "Hard"]:
                self.grid = self.move()
            elif self.level == "Impossible":
                self.grid = self.think()

            if self.grid in self.computer_choices or self.grid in self.player_choices:
                if len(self.computer_choices) + len(self.player_choices) < 9:
                    computer_guess()
        
        computer_guess()
        self.computer_choices.append(self.grid)
        self.result()

    def think(self):
        def check_winner(choices):
            for combination in list(combinations(choices, 3)):
                if sorted(list(combination)) in self.possibilities:
                    return True
            return False

        def minimax(player_choices, computer_choices, depth, is_maximizing):
            if check_winner(self.computer_choices):
                return 10 - depth
            if check_winner(self.player_choices):
                return depth - 10
            if len(player_choices) + len(computer_choices) == 9:
                return 0
            
            if is_maximizing:
                best_score = -float('inf')
                available_moves = [x for x in range(1, 10) if x not in player_choices and x not in computer_choices]
                for move in available_moves:
                    computer_choices.append(move)
                    score = minimax(player_choices, computer_choices, depth + 1, False)
                    computer_choices.remove(move)
                    best_score = max(score, best_score)
                return best_score
            else:
                best_score = float('inf')
                available_moves = [x for x in range(1, 10) if x not in player_choices and x not in computer_choices]
                for move in available_moves:
                    player_choices.append(move)
                    score = minimax(player_choices, computer_choices, depth + 1, True)
                    player_choices.remove(move)
                    best_score = min(score, best_score)
                return best_score
        
        best_move = None
        best_score = -float('inf')
        available_moves = [x for x in range(1, 10) if x not in self.player_choices and x not in self.computer_choices]
        for move in available_moves:
            self.computer_choices.append(move)
            score = minimax(self.player_choices, self.computer_choices, 0, False)
            self.computer_choices.remove(move)
            if score > best_score:
                best_score = score
                best_move = move

        return best_move

    def result(self):
        self.players_outcomes = list(combinations(sorted(self.player_choices), 3))
        self.computer_outcomes = list(combinations(sorted(self.computer_choices), 3))
    
        for _ in list(combinations(self.player_choices, 3)):
            if sorted(list(_)) in self.possibilities:
                self.game_over_message = "Player wins"
                self.result_found = True
                break
            elif (len(self.player_choices) + len(self.computer_choices)) == 9 and (sorted(list(_)) not in self.possibilities):
                self.game_over_message = "We have a draw"
                self.result_found = True

        for _ in list(combinations(self.computer_choices, 3)):
            if self.result_found == False:
                if sorted(list(_)) in self.possibilities:
                    self.game_over_message = "Computer wins"
                    break
                elif (len(self.player_choices) + len(self.computer_choices)) == 9 and (sorted(list(_)) not in self.possibilities):
                    self.game_over_message = "We have a draw"

if __name__ == "__main__":
    if False:
        # Testing the "TwoPlayer" class
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
        # Testing the "SinglePlayer" class
        single_player = SinglePlayer(level="Hard")
        single_player.playersTurn(1)
        print(single_player.player_choices)
        single_player.computersTurn()
        print(single_player.computer_choices)
        single_player.playersTurn(3)
        print(single_player.player_choices)
        single_player.computersTurn()
        print(single_player.computer_choices)
        # single_player.playersTurn(5)
        # print(single_player.player_choices)
        # single_player.computersTurn()
        # print(single_player.computer_choices)
        # single_player.playersTurn(9)
        # print(single_player.player_choices)
        # single_player.computersTurn()
        # print(single_player.computer_choices)
        # print(single_player.game_over_message)
