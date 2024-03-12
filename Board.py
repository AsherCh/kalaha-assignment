import copy
# track the game states
class Board:
      def __init__(self,turn):
              #set a dictionary to trace the number of the stones for the entire board
            self.state = {0:[4,4,4,4,4,4,0],
                        1:[4,4,4,4,4,4,0]}
              # who play the board right now
            self.turn = turn

      #def set_turn(self,turn):
       #     self.turn = turn
      
      def get_turn(self):
            return self.turn
       
       #Make the board snapshoot
      def get_state(self):
            return copy.deepcopy(self.state)
      
      def reverse_player(self):
            if self.turn == 1:
                  self.turn = 0
            else:
                  self.turn = 1
      
      def take_stones(self,pit_index):
            # if the pit_index exceed the range of the pit number 1,2,3,4,5,6 , return false
            if pit_index <0 or pit_index >5 :
                  return False
            # if the pit is empty, you can't pick up the stones from that pit, return false
            if self.state[self.turn][pit_index] == 0:
                  return False

            if self.turn == 1:
                  opposite_turn = 0
            else:
                  opposite_turn = 1
                  
            state_array = self.state[self.turn]+self.state[opposite_turn]

            # Take stones from the pit
            pit_stones = state_array[pit_index]
            state_array[pit_index] = 0
            # Add stone to the rest of pits as counterclockwise
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
            return True
                  
      def terminate(self):
            pass

