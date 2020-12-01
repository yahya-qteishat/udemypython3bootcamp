import random

'''Step 1: Write a function that can print out a board. 
Set up your board as a list, where each index 1-9 corresponds 
with a number on a number pad, so you get a 3 by 3 board representation. '''

#board = ['#','X','O','X','O','X','O','X','O','X']
board = [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ']

def display_board(board):
    
    print('   |   |')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('   |   |')

    print('\n' *5) # scroll up

''' Step 2: Write a function that can take in a player input 
and assign their marker as 'X' or 'O'. Think about using while 
loops to continually ask until you get a correct answer. '''

def player_input():
	marker = ' '
	print('wrap choice in singular quotes')

	while not (marker == 'X' or marker == 'O'):
		marker = str(input('Player 1: Choose X or O: '))

	if marker == 'X':
		return ('X','O')
	else:
		return ('O','X')

''' Step 3: Write a function that takes in the board list 
object, a marker ('X' or 'O'), and a desired position 
(number 1-9) and assigns it to the board. '''

def place_marker(board, marker, position):

	board[position] = marker

''' *Step 4: Write a function that takes in 
a board and a mark (X or O) and then checks 
to see if that mark has won. * '''

def win_check(board, mark):
	# defining the 8 cases where its a win
	return ((board[7] == mark and board[8] == mark and board[9] == mark) or # across the top
    (board[4] == mark and board[5] == mark and board[6] == mark) or # across the middle
    (board[1] == mark and board[2] == mark and board[3] == mark) or # across the bottom
    (board[7] == mark and board[4] == mark and board[1] == mark) or # down the middle
    (board[8] == mark and board[5] == mark and board[2] == mark) or # down the middle
    (board[9] == mark and board[6] == mark and board[3] == mark) or # down the right side
    (board[7] == mark and board[5] == mark and board[3] == mark) or # diagonal
    (board[9] == mark and board[5] == mark and board[1] == mark)) # diagonal

''' Step 5: Write a function that uses the random module to randomly
 decide which player goes first. You may want to lookup random.randint()
  Return a string of which player went first. '''

def choose_first():
	randomint = random.randint(0,1)
	if randomint == 0:
		return 'Player 1 goes first.'
	else:
		return 'Player 2 goes first.'

'''
Step 6: Write a function that returns a boolean 
indicating whether a space on the board is freely available.'''

def space_check(board, position):
	if board[position] != 'X' and board[position] != 'O':
		return True #the board is free
	else:
		return False

'''Step 7: Write a function that checks if the board is full 
and returns a boolean value. True if full, False otherwise.'''

def full_board_check(board):
	for i in range(1,9):
		if board[i] == ' ': # if one is empty
			return False #board is not full
	return True #if it iterated no problem then yes it is full

'''Step 8: Write a function that asks for a player's next position 
(as a number 1-9) and then uses the function from step 6 to check if it's a free position. 
If it is, then return the position for later use.'''

def player_choice(board):
	pos = input('Enter the next position: ') # ask for the  next position
	if space_check(board,pos): # if its free
		return pos # return it..
	else: #if spacecheck is false...
		return 0

''' Step 9: Write a function that asks the player if 
they want to play again and returns a boolean True 
if they do want to play again. '''

def replay():
	answer = input('Play Again? (Y/N): ')
	if answer == 'Y':
		return True
	else:
		return False

''' Step 10: Here comes the hard part! Use while loops 
and the functions you've made to run the game! '''

print('Welcome to Tic Tac Toe!')

while True:
	board = [' ',' ',' ',' ',' ',' ',' ',' ',' ',' '] #clear board
	player1_marker, player2_marker = player_input()
	turn = choose_first()
	print(turn)

	play_game = input('Are you ready to play? Enter Yes or No.')
    
	if play_game.lower()[0] == 'y':
		game_on = True
	else:
		game_on = False

	while game_on:
		if turn == 'Player 1 goes first.':
			display_board(board)
			position = player_choice(board)
			place_marker(board, player1_marker,position)

			if win_check(board, player1_marker):
				display_board(board)
				print('Congratulations ! You have won the game!')
				game_on = False
			else:
				if full_board_check(board):
					display_board(board)
					print('The game is a draw!')
					break
				else:
					turn = 'Player 2 goes first.'
		else:
			# player 2's turn
			display_board(board)
			position = player_choice(board)
			place_marker(board, player2_marker, position)

			if win_check(board, player2_marker):
				display_board(board)
				print('Player 2 has won!')
				game_on = False
			else:
				if full_board_check(board):
					display_board(board)
					print('The game is a draw')
					break
				else:
					turn = 'Player 1 goes first.'
	if not replay():
		break
	
