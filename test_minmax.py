#from Board import *
from Minmax import *
#from Evaluation_function import *
from Tree import *

def test_minimax_simple_case():
    # Build the 
    simple_tree = Node(0)
    simple_tree.children = {0: Node(0), 1:Node(0), 2:Node(0)}
    simple_tree.children[0].children = {0: Leaf(3), 1: Leaf(2), 2: Leaf(5)}
    simple_tree.children[1].children = {0: Leaf(2), 1: Leaf(4), 2: Leaf(6)}
    simple_tree.children[2].children = {0: Leaf(4), 1: Leaf(12), 2: Leaf(8)}

    obj = Tree(simple_tree,2)

    # Return the value from the Node
    def evaluation_fuction(data):
        return data

    def find_children(data, a):
        return data.children[a]

    minimax = Minmax(evaluation_fuction, find_children, 2)

    utiltiy,best_move = minimax.alpha_beta(obj)
    print ("utility:",utiltiy,"best_move",best_move)

if __name__ == "__main__":
    test_minimax_simple_case()
