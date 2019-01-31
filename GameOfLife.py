import numpy as np
import time

#board dimensions
board_width = 30
board_height = 15

#generation length in seconds
iteration_delay = 0.2

board = np.zeros((board_height, board_width))
adjacency_board = np.zeros((board_height, board_width))
rules = np.zeros((2, 8))


def board_setup():
	"""
	Setup the initial state of the board

	board[row][column] = 1
	"""
	board[6][12] = 1
	board[6][13] = 1
	board[6][14] = 1
	board[7][14] = 1
	board[8][13] = 1


def rule_setup():
	"""
	Specify whether a cell should be full after an iteration based on its
	current contents and number of adjacent full cells.
	A cell will empty without a rule to keep it alive.

	rules[is_full(True:1|False:0)][adjacent_full_cells] = 1
	"""
	rules[1][2] = 1
	rules[1][3] = 1
	rules[0][3] = 1


def print_board():
	"""
	Prints the current state of the board to standard output
	"""
	for row in board:
		print("|", end='')
		for cell in row:
			if cell == 1:
				print("#", end='')
			else:
				print(" ", end='')
		print("|")
	for dash in range(board_width+2):
		print("-", end='')
	print("")


def apply_rules():
	"""
	Applys the rules to the current game board based on the current state of the adjacency board
	"""
	global board
	for row in range(board_height):
		for column in range(board_width):
			board[row][column] = rules[int(board[row][column])][int(adjacency_board[row][column])]


def get_cell_content(row,column):
	"""
	Gets the contents of a cell, if the cell is out of bounds empty (0) is returned
	:param row:
	:param column:
	:return: The contents of the cell, will be 0 if the cell is out of bounds
	"""
	if row < 0 or row >= board_height or column < 0 or column >= board_width:
		return 0
	else:
		return board[row][column]


def calculate_adjacency_board ():
	"""
	Calculated the adjacency board with the current state of the game voard
	"""
	global adjacency_board
	for row in range(board_height):
		for column in range(board_width):
			adjacency_board[row][column] = get_cell_content(row - 1, column - 1) + \
										   get_cell_content(row, column - 1) + \
										   get_cell_content(row + 1, column - 1) + \
										   get_cell_content(row - 1, column) + \
										   get_cell_content(row + 1, column) + \
										   get_cell_content(row - 1, column + 1) + \
										   get_cell_content(row, column + 1) + \
										   get_cell_content(row + 1, column + 1)


rule_setup()
board_setup()
print_board()

while(True):
	#application loop
	calculate_adjacency_board()
	apply_rules()
	print_board()
	time.sleep(iteration_delay)