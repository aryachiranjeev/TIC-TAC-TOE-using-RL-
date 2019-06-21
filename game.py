import torch

class Game:
	def __init__(self):
		self.board=torch.zeros(3,3,dtype=torch.int)

	#taking move position and value
	def take_move(self, x, y, value):
		self.board[y,x]=value

	#clearing board after game wins loses or ties
	def clear(self):
		self.board=torch.zeros(3,3,dtype=torch.int)

	def who_wins(self):
		sum_rows=self.board.sum(0)

		sum_cols=self.board.sum(1)

		#if ai wins
		if(sum_rows==3).any() or (sum_cols==3).any() or (self.board.diag().sum()==3) or (self.board.flip(1).diag().sum()==3):
			return 1 

		#if human wins
		if(sum_rows==-3).any() or (sum_cols==-3).any() or (self.board.diag().sum()==-3) or (self.board.flip(1).diag().sum()==-3):
			return -1

		#if ties
		if(self.board==0).sum()==0:
			return 2

		return 0 
	
	@staticmethod
	def hash(board):
		height,width=board.shape
		s=''
		for y in range(height):
			for x in range(width):
				if board[y,x]==0:
					s+='#'
				elif board[y,x]==1:
					s+='o'

				else:
					s+='x'
			if y<height-1:
				s+='\n'
		s+='\n'
		return s

	def __str__(self):
		return self.hash(self.board)
