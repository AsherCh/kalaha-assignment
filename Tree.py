import copy
from Board import *

class Tree:
    def __init__(self,node,max_depth):
        self.max_depth = max_depth
        self.root = node

    def set_root(self,root):
        self.root = root
    
    def get_root(self):
        return self.root
    
    def build(self,node,depth=0):
        #Exit the tree if exceeded the depth limit 2 =  0,1
        if depth >=self.max_depth:
            return 
        board = node.get_board()
        print ("          ")
        print ("Depth:", depth," Root:",board.get_state())
        print ("          ")
        #Find all children
        for i in range(0, 6):
            board = copy.deepcopy(node.get_board()) # Copy the root node and seperate the children node
            if board.take_stones(i):
               node.add_children(i,Node(board))
               print ("  Children:",node.get_children()[i].get_board().get_state())    
        #Go through the next depth to find all children, Order might be optimized

        for child in node.get_children().values():
            self.build(child,depth+1)

class Node:
    def __init__(self,board):
        self.board = board
        self.children = {}

    def add_children(self,move_id,child):
        self.children[move_id] = child

    def get_children(self):
        return self.children
    
    def set_board(self,board):
        self.board = board
    
    def get_board(self):
        return self.board
    
    #calculate the utility
    def get_utility(self,eval_func):
        return eval_func(self.board)
