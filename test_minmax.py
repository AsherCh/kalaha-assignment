from Board import *
from Minmax import *
from Evaluation_function import *
from Tree import *

def test_minimax_simple_case():
    # Build tree from slides
    sample_tree = Node(0)
    sample_tree.children = {0: Node(0), 1:Node(0), 2:Node(0)}
    sample_tree.children[0].children = {0: Leaf(21), 1: Leaf(12), 2: Leaf(8)}
    sample_tree.children[1].children = {0: Leaf(2), 1: Leaf(4), 2: Leaf(6)}
    sample_tree.children[2].children = {0: Leaf(3), 1: Leaf(2), 2: Leaf(5)}

   # print ("Tree:", sample_tree.get_data())
    #print ("Tree:", sample_tree.children[0].get_children()[0].get_data())

    obj = Tree(sample_tree,2)

    # Return the value from the Node
    def evaluation_fuction(data):
        return data

    def result_function(data, a):
        return data.children[a]

    minimax = Minmax(evaluation_fuction, result_function, 2)

    v,slot = minimax.alpha_beta(obj)
    print (v,slot)

if __name__ == "__main__":
    test_minimax_simple_case()
