import copy
# track the game states
class Board:
      def __init__(self):
              #set a dictionary to trace the number of the stones for the entire board
            self.state = {0:[4,4,4,4,4,4,0],
                        1:[4,4,4,4,4,4,0]}
              # who play the board right now
            self.turn = 0

      def get_turn(self):
            return self.turn
       
      def get_state(self):
            return copy.deepcopy(self.state)
            
      def reverse_player(self):
            if self.turn == 1:
                  self.turn = 0
            else:
                  self.turn = 1
                  
      def take_stones(self,pit_index):
            if self.turn == 1:
                  opposite_turn = 0
            else:
                  opposite_turn = 1
                  
            state_array = self.state[self.turn]+self.state[opposite_turn]
            # Take stones from the pit
            pit_stones = state_array[pit_index]
            state_array[pit_index] = 0

            for i in range (pit_stones):
                  pit_index += 1
                  if pit_index >= len(state_array):
                        pit_index = 0
                  state_array[pit_index] += 1
            #Save the stone number to the state
            self.state[self.turn] = state_array[0:7]
            self.state[opposite_turn] = state_array[7:len(state_array)]
            
            ## steal the stones???
            ## capture stones
                  
      def terminate(self):
            pass

