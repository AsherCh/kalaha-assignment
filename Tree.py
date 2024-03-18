import copy
from Board import *


class Tree:
    def __init__(self, node, max_depth):
        self.max_depth = max_depth
        self.root = node

    def set_root(self, root):
        self.root = root

    def get_root(self):
        return self.root

    def build(self, node, depth=0):
        if depth >= self.max_depth:
            return
        board = node.get_data()
        if depth >= 1:
            board.reverse_player()
        # Find all children
        for i in range(0, 6):
            board = copy.deepcopy(
                node.get_data()
            )  # Copy the root node and separate the children node
            if board.take_stones(i) != "empty_pit":
                child_node = Node(board)
                node.add_children(i, child_node)
        # Go through the next depth to find all children, Order might be optimized
        for child in node.get_children().values():
            self.build(child, depth + 1)


class Node:
    def __init__(self, data):
        self.data = data
        self.children = {}

    def add_children(self, move_id, child):
        self.children[move_id] = child

    def get_children(self):
        return self.children

    def set_data(self, data):
        self.data = data

    def get_data(self):
        return self.data

    # calculate the utility
    def get_utility(self, eval_func):
        return eval_func(self.data)


class Leaf:
    def __init__(self, data):
        self.data = data

    def get_data(self):
        return self.data

    # calculate the utility
    def get_utility(self, eval_func):
        return eval_func(self.data)
