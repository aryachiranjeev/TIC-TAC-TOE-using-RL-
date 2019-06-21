import random
import torch
from game import Game
from agent import RLAgent
from moves import 	Moves

game=Game()
agent=RLAgent()
moves=Moves()

num_win=0 #initialize no. of win by human
num_lose=0 #initialize no. of win by ai but loss by human
num_tie=0

random.seed(1000)

def check_board_and_may_update_state_values():

	global num_win, num_lose, num_tie

	win_or_tie=True

	if game.who_wins()==-1: #human win
		print("YOU WIN!!")
		agent.update_state_values(0)
		num_win+=1

	elif game.who_wins()==1: #ai win
		print("YOU LOSE!!")
		agent.update_state_values(1)
		num_lose+=1

	elif game.who_wins()==2: #tie
		print("TIE!!")
		num_tie+=1

	else:
		win_or_tie=False

	if win_or_tie:
		game.clear()
		agent.clear_history()

	return win_or_tie

while True:

	print("The number of wins are : {}\nThe number of loses : {}\nThe number of ties is : {}".format(num_win, num_lose, num_tie))

	if (num_win+num_lose+num_tie) == 30000:
		break


	#moves 
	x,y=moves.random_move(game.board)

	game.take_move(x,y,-1)

	print(game)

	#check
	win_or_tie=check_board_and_may_update_state_values()
	if win_or_tie:
		continue

	#RL AI move
	x,y=agent.next_move(game.board)
	game.take_move(x,y,1)
	agent.cache_move(game.board)
	print(game)

	#check
	check_board_and_may_update_state_values()

torch.save(agent.state_values,'tic_tac_toe.pth')



