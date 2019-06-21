import torch
import random
from game import Game 
from agent import RLAgent 
from moves import Moves 

game=Game()
agent=RLAgent()
moves=Moves()

agent.state_values=torch.load('./tic_tac_toe.pth')

def check_board():
	win_or_tie=True
	if game.who_wins()==-1: #human win
		print("YOU WIN!!")
		game.clear()

	elif game.who_wins()==1: #ai win
		print("YOU LOSE!!")
		game.clear()

	elif game.who_wins()==2: #Tie
		print("TIE!!")
		game.clear()

	else:
		win_or_tie=False

	return win_or_tie

while True:
	x,y=moves.human_move()
	if game.board[y,x]!=0:
		print('(%d%d) is taken' %(x,y))
		continue

	game.take_move(x,y,-1)
	print(game)

	#check
	win_or_tie=check_board()

	if win_or_tie:
		continue

	#RL AI move
	x,y=agent.next_move(game.board)
	game.take_move(x,y,1)
	print(game)

	#check
	check_board()
