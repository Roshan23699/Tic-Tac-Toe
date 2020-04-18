# Bot paying with the minimax algorithm impossible to win


#global section


def play_game():
	current_player = "X"
	game_still_going = True
	winner = None
	board = ["-", "-", "-", 
			"-", "-", "-",
			"-", "-", "-"]
			#display board
	display_board(board)
	while game_still_going:
		#handle turn
		if(current_player == "X"):
			temp_board = board
			pos = find_best_move(temp_board, "X")
			# board = temp_board
			board[pos] = "X"
			
		else :
			board = handle_turn(board, current_player)
		display_board(board)
		# print("this")
		#flip turn
		current_player = flip_turn(current_player)
		winner = check_for_winner(board)
		if(winner != None):
			break
		if(check_for_tie(board)):
			break

	return winner


#display board
def display_board(board):
	print(board[0] + " | " + board[1] + " | " + board[2])
	print(board[3] + " | " + board[4] + " | " + board[5])
	print(board[6] + " | " + board[7] + " | " + board[8])
	return

def handle_turn(board, current_player):
	pos = input()
	pos = int(pos) - 1
	board[pos] = current_player
	return board

def flip_turn(current_player):
	if(current_player == "X"):
		current_player = "O"
	else :
		current_player = "X"
	return current_player


#
def check_for_winner(board):
	winner = None
	row_winner = check_rows(board)
	column_winner = check_columns(board)
	diagonal_winner = check_diagonals(board)
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
	return winner
		

def check_for_tie(board):
	
	for i in range(0, 9):
		if(board[i] == "-"):
			return 0
 	return 1




def check_rows(board):
	#check if the rows are equal 
	row_1 = board[0] == board[1] == board[2] != "-"
	row_2 = board[3] == board[4] == board[5] != "-"
	row_3 = board[6] == board[7] == board[8] != "-"
	# return the winner
	if row_1 :
		return board[0]
	elif row_2 :
		return board[3]
	elif row_3 :
		return board[6]
	return
	


def check_columns(board):
	
	#check if the rows are equal 
	column_1 = board[0] == board[3] == board[6] != "-"
	column_2 = board[1] == board[4] == board[7] != "-"
	column_3 = board[2] == board[5] == board[8] != "-"
	
	# return the winner
	if column_1 :
		return board[0]
	elif column_2 :
		return board[1]
	elif column_3 :
		return board[2]
	return


def check_diagonals(board):
	
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









def find_best_move(board, current_player):
	# print("again")
	best_move = None
	best_score = -2
	for i in range(0, 9):
			if(if_available(board, i)):
				board[i] = current_player
				score = minimax(board, 0, 0)
				board[i] = "-"
				if(score > best_score):
					best_move = i
					best_score = score
	return best_move

def minimax(board, depth, ismax):
	if(check_for_winner(board) == "X"):
		return 1
	if(check_for_winner(board) == "O"):
		return -1
	if(check_for_tie(board)):
		return 0
	if(ismax):
		# print("now max")
		best_val = -2
		for i in range(0, 9):
			if(if_available(board, i)):
				board[i] = "X"
				val = minimax(board, depth + 1, 0)
				board[i] = "-"
				best_val = max(best_val, val)
		return best_val
	else :
		# print("now min")
		best_val = +2
		for i in range(0, 9):
			if(if_available(board, i)):
				board[i] = "O"

				val = minimax(board, depth + 1, 1)
				board[i] = "-"
				best_val = min(best_val, val)
		return best_val
				

#
#check if the square is available
def if_available(board, i):
	if(board[i] == "-"):
		return True
	return False


#driver program

if __name__ == "__main__":
	winner = play_game()
	if(winner != None):
		print(winner + " won.")
	else :
		print("Tie.")
