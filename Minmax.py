import copy
from Tree import *


class Minmax:
    def __init__(self, eval_func, find_child, max_depth):
        self.eval_func = eval_func
        self.find_child = find_child
        self.max_depth = max_depth

    def alpha_beta(self, tree):
        utility, best_move = self.max_value(tree.root, float("-inf"), float("inf"), 0)
        return utility, best_move

    def max_value(self, node, a, b, depth):
        if depth >= self.max_depth:
            value = node.get_utility(self.eval_func)
            # print ("max_value Utility:",value)
            return value, 0
        # alpha
        v = float("-inf")
        best_move = -1

        if len(node.get_children()) != 0:
            for i in node.get_children().keys():
                child_node = self.find_child(node, i)
                # print ("max_value node.get_children().key():",node.get_children().keys())
                # print ("max_value: ",child_node.get_data().get_state())
                v = max(v, self.min_value(child_node, a, b, depth + 1)[0])
                # cut off
                if v >= b:
                    #     print ("max_value():cut off")
                    return v, best_move
                if v > a:
                    best_move = i
                a = max(a, v)
        else:
            return node.get_utility(self.eval_func), 0
        return v, best_move

    def min_value(self, node, a, b, depth):
        if depth >= self.max_depth:
            value = node.get_utility(self.eval_func)
            return value, 0
        v = float("inf")
        best_move = -1
        # print ("min_value node.get_children().key():",node.get_children().keys())
        if len(node.get_children()) != 0:
            for i in node.get_children().keys():
                child_node = self.find_child(node, i)
                # print ("min_value: ",child_node.get_data().get_state())
                v = min(v, self.max_value(child_node, a, b, depth + 1)[0])
                # cut off
                if v <= a:
                    #   print ("min_value():cut off")
                    return v, best_move
                if v < b:
                    best_move = i

                b = min(b, v)
        else:
            return node.get_utility(self.eval_func), 0
        return v, best_move
