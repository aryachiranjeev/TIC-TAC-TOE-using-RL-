import torch
import random
from game import Game

class RLAgent:

	def __init__(self):
		self.state_values={} # map state hashkey -> state value
		self.history_states=[] # cache history states for updating
		
	def next_move(self, board):

		hashkey= Game.hash(board)

		if hashkey not in self.state_values:
			self.state_values[hashkey]=0.5

		candidate_moves=[] #store all possible values
		for y in range(3):
			for x in range(3):
				if board[y,x]== 0: #ai can take here
					next_board=board.clone()
					next_board[y,x]=1
					hashkey= Game.hash(next_board)
					if hashkey not in self.state_values:
						self.state_values[hashkey]=0.5

					candidate_moves.append([hashkey,self.state_values[hashkey],(x,y)])


		candidate_moves.sort(key=lambda x: x[1] , reverse=True)
		if random.random()<1:
			next_move=candidate_moves[0][2]

		else:
			next_move=random.choice(candidate_moves)[2]

		return next_move


	def update_state_values(self,last_state_values):
		lr=0.3
		N=len(self.history_states)

		for i in range(N-1,-1,-1): #update value function from last sate
			cur_state=self.history_states[i]

			if i==N-1:
				self.state_values[cur_state] = last_state_values
			else:
				next_state=self.history_states[i+1]

				#value_fn(state)=value_fn(state)+lr*[value_fn(next_state)-value_fn(state)]
				self.state_values[cur_state]+=lr*(self.state_values[next_state]-self.state_values[cur_state])


	def cache_move(self,board):
		self.history_states.append(Game.hash(board))


	def clear_history(self):
		self.history_states=[]


def test():
	agent = RLAgent()
	current_board= torch.zeros(3,3,dtype=torch.int)
	current_board[0,0]=-1

	print(agent.next_move(current_board))
