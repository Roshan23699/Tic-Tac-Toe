#___Global Variables____
#Game board
board = ["-", "-", "-", 
		"-", "-", "-", 
		"-", "-", "-"]

#If the game is still going
game_still_going = True

#whos turn is it
current_player = "X"

#who is the winner 
winner = None


def display_board():
	print(board[0] + " | " + board[1] + " | " + board[2])
	print(board[3] + " | " + board[4] + " | " + board[5])
	print(board[6] + " | " + board[7] + " | " + board[8])
def play_game():
	#display the board 
	display_board()
	while game_still_going:

		#handle the turn
		handle_turn(current_player)

		check_if_game_over()

		flip_player()

	# the game has ended
	if winner == "X" or winner == "O":
		print(winner + " Won.")
	elif winner == None:
		print("Tie.")

def handle_turn(current_player):
	position = input("Enter Your Choice")
	position = int(position) - 1
	while((position > 8 or position < 0) or board[position] != "-"):
		position = input("Enter a valid choice")
		position = int(position) - 1

	board[position] = current_player
	display_board()

def check_if_game_over():
	check_for_winner()
	check_if_tie()

def check_for_winner():
	global winner
	#check rows
	row_winner = check_rows()
	column_winner = check_columns()
	diagonal_winner = check_diagonals()
	if(row_winner):
		winner = row_winner
		#there was win
	elif column_winner:
		winner = column_winner
		#there was win
	elif diagonal_winner:
		#there was a win
		winner = diagonal_winner

	else :
		#there was no win
		winner = None
	return

	
def check_rows():
	#set up global variable
	global game_still_going
	#check if the rows are equal 
	row_1 = board[0] == board[1] == board[2] != "-"
	row_2 = board[3] == board[4] == board[5] != "-"
	row_3 = board[6] == board[7] == board[8] != "-"
	if(row_1 or row_2 or row_3):
		game_still_going = False
	# return the winner
	if row_1 :
		return board[0]
	elif row_2 :
		return board[3]
	elif row_3 :
		return board[6]
	return
	


def check_columns():
	#set up global variable
	global game_still_going
	#check if the rows are equal 
	column_1 = board[0] == board[3] == board[6] != "-"
	column_2 = board[1] == board[4] == board[7] != "-"
	column_3 = board[2] == board[5] == board[8] != "-"
	if(column_1 or column_2 or column_3):
		game_still_going = False
	# return the winner
	if column_1 :
		return board[0]
	elif column_2 :
		return board[1]
	elif column_3 :
		return board[2]
	return


def check_diagonals():
	#set up global variable
	global game_still_going
	#check if the rows are equal 
	diagonal_1 = board[0] == board[4] == board[8] != "-"
	diagonal_2 = board[2] == board[4] == board[6] != "-"
	if(diagonal_1 or diagonal_2):
		game_still_going = False
	# return the winner
	if diagonal_1 :
		return board[4]
	elif diagonal_2 :
		return board[4]
	return



def check_if_tie():
	global game_still_going
	for i in range(0, 9):
		if(board[i] == "-"):
			return
	game_still_going = False
 	return

def flip_player():
	global current_player
	if(current_player == "X"):
		current_player = "O"
	else :
		current_player = "X"
	return
if __name__ == "__main__":
	play_game()