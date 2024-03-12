import copy
from Tree import *

class Minmax:
    def __init__(self,eval_func,result_func,max_depth):
        self.eval_func = eval_func
        self.resut_func = result_func
        self.max_depth = max_depth

    def alpha_beta(self,tree):
        # return utility value and the index of the best move
        # player <---game.To-Move(state)
        #value,move <-Max-Value(game,state,-inf,+inf)
        utility,move_i= self.max_value(tree.root,float('-inf'),float('inf'),0)
        # return an action
        return utility,move_i
    
    def max_value(self,node,a,b,depth):
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
        
        board = node.get_data()
        # alpha
        v = float('-inf')
        best_move=-1

        for i in node.get_children().keys():
            board_copy = copy.deepcopy(board)
            result_node = self.resut_func(node,i)
            #if result_node.get_board().get_turn() == 1:
            v = max(v,self.min_value(result_node,a,b,depth+1)[0])

            node.set_data(board_copy)
            # cut off
            if v >= b:
                print ("cut off")
                return v,best_move
            if v > a:
                best_move = i

            a = max(a,v)
            return v,best_move

        #return (utility,move)  pair

    def min_value(self,node,a,b,depth):
        if depth >= self.max_depth:
            return node.get_utility(self.eval_func)
        
        board = node.get_data()
        #beta
        v = float('inf')
        best_move=-1

        for i in node.get_children().keys():
            board_copy = copy.deepcopy(board)
            result_node = self.resut_func(node,i)
            #if result_node.get_board().get_turn() == 1:
            v = min(v,self.max_value(result_node,a,b,depth+1)[0])

            node.set_data(board_copy)
            # cut off
            if v <= a:
                print ("cut off")
                return v,best_move
            if v < b:
                best_move = i

            b = min(b,v)
            return v,best_move
