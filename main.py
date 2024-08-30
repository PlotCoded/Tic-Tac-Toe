import tkinter as tk
import customtkinter as ctk
import Backend

game = ctk.CTk()
game.geometry("600x400")
game.title("Tic-Tac-Toe")

#Applying a theme of the game: Don't worry about this part
#ctk.set_default_color_theme("Theme.json")

class TwoPlayer:
	def __init__(self, game):
		self.game = game

	def displayButton(self):
		self.button = ctk.CTkButton(self.game, text="Two Players", command=self.forgetButtons)
		self.button.pack(side="left", expand=True)

	def forgetButtons(self):
		computer.button.pack_forget()
		self.button.pack_forget()

		#Displaying the grid, quit button, play again button, etc
		self.ttt()

	def ttt(self): #ttt --> Tic-Tac-Toe
		#Making the window bigger and better to fit the 9 by 9 grid in the game
		game.geometry("600x600+100+50")

		self.guide = ctk.CTkLabel(self.game, text="Click a grid to play")
		self.guide.pack()

		#Creating a grid to display the buttons: These button are what the user will click to display "X" or "O"
		self.grid_frame = ctk.CTkFrame(self.game)
		self.grid_frame.pack()

		#Creating a grid layout in the "self.grid_frame" frame
		self.grid_frame.rowconfigure(3)
		self.grid_frame.columnconfigure(3)

		#Creating each buttons
		self.button1 = ctk.CTkButton(self.grid_frame,text="", command=lambda: self.buttonClicked(self.button1))
		self.button2 = ctk.CTkButton(self.grid_frame,text="", command=lambda: self.buttonClicked(self.button2))
		self.button3 = ctk.CTkButton(self.grid_frame,text="", command=lambda: self.buttonClicked(self.button3))
		self.button4 = ctk.CTkButton(self.grid_frame,text="", command=lambda: self.buttonClicked(self.button4))
		self.button5 = ctk.CTkButton(self.grid_frame,text="", command=lambda: self.buttonClicked(self.button5))
		self.button6 = ctk.CTkButton(self.grid_frame,text="", command=lambda: self.buttonClicked(self.button6))
		self.button7 = ctk.CTkButton(self.grid_frame,text="", command=lambda: self.buttonClicked(self.button7))
		self.button8 = ctk.CTkButton(self.grid_frame,text="", command=lambda: self.buttonClicked(self.button8))
		self.button9 = ctk.CTkButton(self.grid_frame,text="", command=lambda: self.buttonClicked(self.button9))

		#Placing each button
		self.button1.grid(row=0,column=0)
		self.button2.grid(row=0,column=1)
		self.button3.grid(row=0,column=2)
		self.button4.grid(row=1,column=0)
		self.button5.grid(row=1,column=1)
		self.button6.grid(row=1,column=2)
		self.button7.grid(row=2,column=0)
		self.button8.grid(row=2,column=1)
		self.button9.grid(row=2,column=2)

		self.buttons = [self.button1, self.button2, self.button3, self.button4, self.button5, self.button6, self.button7, self.button8, self.button9]

		#These boolean variables tell if it's X's or O's turn to play
		self.x_turn = True
		self.o_turn = False

		self.game_over_frame = ctk.CTkFrame(self.game)
		self.game_over_frame.pack()

		self.game_over_message = ctk.CTkLabel(self.game_over_frame, text=f"Game Over: It's a tie")

		self.quit_button = ctk.CTkButton(self.game_over_frame, text="Quit", command=self.quit)
		self.quit_button.pack(side="left")

		self.play_again_button = ctk.CTkButton(self.game_over_frame, text="Play Again", command=self.play_again)

		self.back_button = ctk.CTkButton(self.game_over_frame, text="Back", command=self.back)

		#Initializing the backend(In simple terms, allowing us to use backend.py in this file "main.py")
		self.backend = Backend.TwoPlayers()

	def forgetTTT(self):
		#Changing the size of the window to its original size
		game.geometry("600x400")

		self.guide.pack_forget()
		self.grid_frame.pack_forget()
		self.game_over_frame.pack_forget()

	def buttonClicked(self, button):
		#Changing the text to "X" or "O" if it's X's turn or O's turn
		if self.x_turn:
			button.configure(text="X")
			button.configure(state="disabled")

			#Making it O's turn next after playing X of course
			self.x_turn = False
			self.o_turn = True

		elif self.o_turn:
			button.configure(text="O")
			button.configure(state="disabled")

			#Making it X's turn next after playing O of course
			self.x_turn = True
			self.o_turn = False

		#Processing the user's info
		#Note: "grid" is just to get the last number on its name in other to tell us which grid was pressed
		grid = str(button)[-1]
		if grid == "n":
			grid = 1 #I did this because if you try to get the last thing on the string "grid" if you clicked the first button, it will be "n" not 1
		else:
			grid = int(grid)
		
		#Processing the user's info
		self.backend.play(grid)
			
		#Updating the guide message based on the user input(the button he/she clicks). If it is X's turn or O's turn
		self.guide.configure(text=self.backend.guide_message)
		
		if self.backend.game_over_message == "X wins":
			#Displaying the game over message, quit, play again and back button accurately
			self.game_over_message.pack()
			self.game_over_message.configure(text = self.backend.game_over_message)
			self.quit_button.pack_forget()
			self.play_again_button.pack(side="left")
			self.back_button.pack(side="left")

			#Disabling all the buttons so the user doesn't input "X" or "O" after the game is over
			for _ in self.buttons:
				_.configure(state="disabled")

		elif self.backend.game_over_message == "O wins":
			#Displaying the game over message, play again and back button accurately
			self.game_over_message.pack()
			self.game_over_message.configure(text = self.backend.game_over_message)
			self.quit_button.pack_forget()
			self.play_again_button.pack(side="left")
			self.back_button.pack(side="left")

			#Disabling all the buttons so the user doesn't input "X" or "O" after the game is over
			for _ in self.buttons:
				_.configure(state="disabled")

		elif self.backend.game_over_message == "We have a draw":
			#Displaying the game over message, quit, play again and back button accurately
			self.game_over_message.pack()
			self.game_over_message.configure(text = self.backend.game_over_message)
			self.quit_button.pack_forget()
			self.play_again_button.pack(side="left")
			self.back_button.pack(side="left")

			#Disabling all the buttons so the user doesn't input "X" or "O" after the game is over
			for _ in self.buttons:
				_.configure(state="disabled")

	def quit(self):
		#Asking the user if he actually wants to quit
		quit = tk.messagebox.askyesno(title="Quit", message="Are you sure you want to quit?")

		if quit: #If they want to quit
			self.forgetTTT()
			self.displayButton()
			computer.displayButton()

	def play_again(self):
		self.forgetTTT()
		self.ttt()

	def back(self):
		self.forgetTTT()
		self.displayButton()
		computer.displayButton()

class Computer:
	def __init__(self, game):
		self.game = game

	def displayButton(self):
		self.button = ctk.CTkButton(self.game, text="Against Computer", command=self.choice)
		self.button.pack(side="left", expand=True)

	def forgetButtons(self):
		two_player.button.pack_forget()
		self.button.pack_forget()

	def choice(self):
		#Clearing the previous page (Two Player  and Computer button)
		self.forgetButtons()

		#Giving the player the choice to pick "x" or "o"  and the level to play against the computer and 
		self.x_o_frame = ctk.CTkFrame(self.game)
		self.x_o_frame.pack(pady=30)

		def radio_command():
			#Knowing what letter the player/user chooses
			if self.x_o_var.get():
				self.player = "player O"
				self.opponent = "player X"
				print("Choose O")
			else:
				print("Choose X")
				self.player = "player X"
				self.opponent = "player O"

		#Creating X or O buttons
		self.x_o_var = tk.IntVar(value=0)
		self.play_x = ctk.CTkRadioButton(self.x_o_frame, text="Play with X", value=0, variable=self.x_o_var, command=radio_command)
		self.play_o = ctk.CTkRadioButton(self.x_o_frame, text="Play with O", value=1, variable=self.x_o_var, command=radio_command)

		radio_command() #The reason why i am running this function here is to make sure that "self.player" is the right option(X or O) choosen by the user when ever the user presses "Back","Play Again" or "Quit" buttons

		#Displaying the buttons
		self.play_x.pack(side="left", padx=40)
		self.play_o.pack(side="right", padx=40)

		#Displaying the levels option menu
		self.levels()

	def levels(self):
		self.levels_var = tk.StringVar(value="Hard")
		self.levelsMenu = ctk.CTkOptionMenu(self.game, variable=self.levels_var, values=["Easy", "Medium","Hard","Impossible"])
		self.levelsMenu.pack(pady=30)

		#Displaying the Cancel and Next buttons
		self.cancelOrNext()

	def cancelOrNext(self):
		self.cancelOrNextFrame = ctk.CTkFrame(self.game)
		self.cancelOrNextFrame.pack(pady=30)

		self.cancel_button = ctk.CTkButton(self.cancelOrNextFrame, text="Cancel", command=self.cancelFunc)
		self.cancel_button.pack(side="left", padx=50)

		self.next_button = ctk.CTkButton(self.cancelOrNextFrame, text="Next", command=self.nextFunc)
		self.next_button.pack(side="left", padx=50)

	def cancelFunc(self):
		#Clearing the "choice" page, the page with "Play X radiobutton, Play O radiobutton, levels Menu, cancel button, next button"
		self.x_o_frame.pack_forget()
		self.levelsMenu.pack_forget()
		self.cancelOrNextFrame.pack_forget()

		#Displaying the Two Player and Computer button
		two_player.displayButton()
		self.displayButton() 

	def nextFunc(self):
		#Clearing the "choice" page, the page with "Play X radiobutton, Play O radiobutton, levels optionmenu, cancel button, next button"
		self.x_o_frame.pack_forget()
		self.levelsMenu.pack_forget()
		self.cancelOrNextFrame.pack_forget()

		#Displaying the "grid frame", "quit" button, "play again" button, etc
		self.ttt()

	def ttt(self): #ttt --> Tic-Tac-Toe
		#Making the window bigger and better to fit the 9 by 9 grid in the game
		game.geometry("600x600+100+50")

		self.guide = ctk.CTkLabel(self.game, text="Click a grid to play")
		self.guide.pack()
		
		self.seconds = 3.3
		if self.levels_var.get() == "Hard" or self.levels_var.get() == "Impossible":
			self.timer_label = ctk.CTkLabel(self.game, text=f"Timer: {self.seconds} seconds left for {self.player}")

			global countdown
			def countdown():
				if self.seconds > 0: #If the seconds are not over
					self.seconds-=0.1
					self.timer_label.configure(text=f"Timer: {abs(round(self.seconds,2))} seconds left for {self.player}")
					game.after(100, countdown)
				else: #If the seconds are over
					self.timer_label.pack_forget()
					#Game over for the user. A bit harsh but that's what the user choose
					#Displaying the game over message, quit, play again and back button accurately
					self.game_over_message.configure(text="Computer wins")
					self.game_over_message.pack()
					self.quit_button.pack_forget()
					self.play_again_button.pack(side="left")
					self.back_button.pack(side="left")

					#Starting the timer
					self.seconds = 3.3
			
			self.timer_label.pack()
			countdown()

		#Creating a grid to display the buttons: These button are what the user will click to display "X" or "O"
		self.grid_frame = ctk.CTkFrame(self.game)
		self.grid_frame.pack()

		#Creating a grid layout in the "self.grid_frame" frame
		self.grid_frame.rowconfigure(3)
		self.grid_frame.columnconfigure(3)

		#Creating each buttons
		self.button1 = ctk.CTkButton(self.grid_frame,text="", command=lambda: self.buttonClicked(self.button1))
		self.button2 = ctk.CTkButton(self.grid_frame,text="", command=lambda: self.buttonClicked(self.button2))
		self.button3 = ctk.CTkButton(self.grid_frame,text="", command=lambda: self.buttonClicked(self.button3))
		self.button4 = ctk.CTkButton(self.grid_frame,text="", command=lambda: self.buttonClicked(self.button4))
		self.button5 = ctk.CTkButton(self.grid_frame,text="", command=lambda: self.buttonClicked(self.button5))
		self.button6 = ctk.CTkButton(self.grid_frame,text="", command=lambda: self.buttonClicked(self.button6))
		self.button7 = ctk.CTkButton(self.grid_frame,text="", command=lambda: self.buttonClicked(self.button7))
		self.button8 = ctk.CTkButton(self.grid_frame,text="", command=lambda: self.buttonClicked(self.button8))
		self.button9 = ctk.CTkButton(self.grid_frame,text="", command=lambda: self.buttonClicked(self.button9))

		#Placing each button
		self.button1.grid(row=0,column=0)
		self.button2.grid(row=0,column=1)
		self.button3.grid(row=0,column=2)
		self.button4.grid(row=1,column=0)
		self.button5.grid(row=1,column=1)
		self.button6.grid(row=1,column=2)
		self.button7.grid(row=2,column=0)
		self.button8.grid(row=2,column=1)
		self.button9.grid(row=2,column=2)

		self.buttons = [self.button1, self.button2, self.button3, self.button4, self.button5, self.button6, self.button7, self.button8, self.button9]

		#These boolean variables tell if it's X's or O's turn to play based on the selection of the radiobutton "play_x" and "play_o"
		self.x_turn = bool(self.x_o_var.get() == self.play_x.cget("value"))
		self.o_turn = bool(self.x_o_var.get()  == self.play_o.cget("value"))

		self.game_over_frame = ctk.CTkFrame(self.game)
		self.game_over_frame.pack();

		self.game_over_message = ctk.CTkLabel(self.game_over_frame, text=f"Game Over: It's a tie")

		self.quit_button = ctk.CTkButton(self.game_over_frame, text="Quit", command=self.quit)
		self.quit_button.pack(side="left")

		self.play_again_button = ctk.CTkButton(self.game_over_frame, text="Play Again", command=self.play_again)

		self.back_button = ctk.CTkButton(self.game_over_frame, text="Back", command=self.back)

		#Run computer if only O is True because the computer has to start first because it is X

	def forgetTTT(self):
		#Changing the size of the window to its original size
		game.geometry("600x400")

		self.guide.pack_forget()
		self.timer_label.pack_forget()
		self.grid_frame.pack_forget()
		self.game_over_frame.pack_forget()

	def buttonClicked(self, button):
		#Setting up the timer to the opponent
		self.seconds = 0 #Setting the timer to 0 seconds. It's purpose is to allow it to restart
		if self.levels_var.get() == "Hard" or self.levels_var.get() == "Impossible":
			countdown()

		#Redisplaying the widgets accurately because the widgets disappeared and got rearranged after the seconds was 0
		self.grid_frame.pack_forget()
		self.game_over_frame.pack_forget()
		self.game_over_message.pack_forget()
		self.play_again_button.pack_forget()
		self.back_button.pack_forget()
		
		#Reseting the display message of the timer
		if self.levels_var.get() == "Hard" or self.levels_var.get() == "Impossible":
			self.timer_label.configure(text=f"Timer: {abs(round(self.seconds))} seconds left for {self.player}")
			self.timer_label.pack()
		
		#Redisplaying the widgets again
		self.grid_frame.pack()
		self.game_over_frame.pack()
		self.quit_button.pack(side="left")

		#Changing the text to "X" or "O" if it's X's turn or O's turn
		if self.x_turn:
			button.configure(text="X")
			button.configure(state="disabled")

			#Making it O's turn next after playing X of course
			self.x_turn = False
			self.o_turn = True

			#buttonClicked function must be run again to run the Computer in the elif statement

		elif self.o_turn:
			#Running computer

			#Making it X's turn next after playing O of course
			self.x_turn = True
			self.o_turn = False

			button.configure(text="O")
			button.configure(state="disabled")

		#Processing the game input to determine a winner/loser/draw

		#Disabling the buttons so the user can't click an empty box while after the game is over and change the content to "X" or "O"

	def quit(self):
		#Asking the user if he actually wants to quit
		quit = tk.messagebox.askyesno(title="Quit", message="Are you sure you want to quit?")

		if quit: #If they want to quit
			#Reseting the timer
			self.seconds = 0

			self.forgetTTT()
			self.choice()

	def play_again(self):
		self.forgetTTT()
		self.ttt()

	def back(self):
		self.forgetTTT()
		self.choice()

#Initializing(Making the "Two Player" and "Against Computer" buttons)
two_player = TwoPlayer(game)
two_player.displayButton()

computer = Computer(game)
computer.displayButton()

game.mainloop()