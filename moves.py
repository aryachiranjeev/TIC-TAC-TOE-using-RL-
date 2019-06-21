import random
import numpy as np 

class Moves:
	def __init__(self):
		pass

	#random moves of ai 
	def random_move(self,board):
		found=False
		for y in np.random.permutation(3):
			for x in np.random.permutation(3):
				if board[y,x]==0:
					found=True
					break

				if found:
					break

		return x,y

	def human_move(self):
		inputs=input("human turn:")
		x,y=int(inputs[0]),int(inputs[1])
		return x,y
