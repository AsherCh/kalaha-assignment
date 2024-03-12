import copy
from Tree import *

class Minmax:
    def __init__(self,eval_func,find_child,max_depth):
        self.eval_func = eval_func
        self.find_child = find_child
        self.max_depth = max_depth

    def alpha_beta(self,tree):
        # return utility value and the index of the best move
        #Peuscode
        # player <---game.To-Move(state)
        #value,move <-Max-Value(game,state,-inf,+inf)
        utility,best_move= self.max_value(tree.root,float('-inf'),float('inf'),0)
        # return an action
        return utility,best_move
    
    def max_value(self,node,a,b,depth):
        #Peuscode
        #if game.IS-TERMINAL(state) then return game.UTILITY(state,player),null
        #v <--- -inft
        #for each a in game.Actions(state) do
        # v2,a2 <--- MIN-VALUE(game,game.RESULT(state,a),a,b)
        # if v2 > v then
            # v,move <--- v2,a
            # a <---- MAX(a,v)
        # if v >= b then return v,move
        if depth >= self.max_depth:
            return node.get_utility(self.eval_func),0
        
        #board = node.get_data()
        # alpha
        v = float('-inf')
        best_move=-1

        for i in node.get_children().keys():
            #board_copy = copy.deepcopy(board)
            child_node = self.find_child(node,i)
            print ("max_value: ",child_node.get_data())
            #if result_node.get_board().get_turn() == 1:
            v = max(v,self.min_value(child_node,a,b,depth+1)[0])
            #node.set_data(board_copy)
            # cut off
            if v >= b:
                print ("max_value():cut off")
                return v,best_move
            if v > a:
                best_move = i

            a = max(a,v)
        return v,best_move

    def min_value(self,node,a,b,depth):
        if depth >= self.max_depth:
            return node.get_utility(self.eval_func)
        
        #board = node.get_data()
        v = float('inf')
        best_move=-1

        for i in node.get_children().keys():
            #board_copy = copy.deepcopy(board)
            child_node = self.find_child(node,i)
            print ("min_value: ",child_node.get_data())
            #if result_node.get_board().get_turn() == 1:
            v = min(v,self.max_value(child_node,a,b,depth+1)[0])
            #node.set_data(board_copy)
            # cut off
            if v <= a:
                print ("min_value():cut off")
                return v,best_move
            if v < b:
                best_move = i

            b = min(b,v)
        return v,best_move
