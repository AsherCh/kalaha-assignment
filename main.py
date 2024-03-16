from Board import *
from Minmax import *
from Evaluation_function import *
from Tree import *


if __name__ == "__main__":
    print("-------------Kalaha----------------")
    print("-------------By Group 39-----------")
    print(
        "You will play this game with the computer.Please pick up your stones from your side first"
    )
    # Play the game
    HUMAN = 1
    COMPUTER = 0
    MAX_DEPTH = 5
    # Human as the first player
    board = Board(HUMAN)
    # print the initial board
    board.print_board()
    # Set the board status as the node

    def find_children(node, a):
        children = node.get_children()
        return children[a]

    ##  evaluation_function2 and evaluation_function3 are better
    #minmax = Minmax(evaluation_fuction, find_children, MAX_DEPTH)
    minmax = Minmax(evaluation_function2, find_children, MAX_DEPTH)
    #minmax = Minmax(evaluation_function3, find_children, MAX_DEPTH)  
    #minmax = Minmax(evaluation_function4, find_children, MAX_DEPTH)

    game_end = False
    while not game_end:
        '''
        # Human input the first move
        current_player = board.get_turn()
        print(current_player, " Human,please pick up your stones from your side:")
        pit_index = board.get_user_move()
        board.take_stones(pit_index)
        board.print_board()
        
        '''
        '''
        root_node = Node(board)
        tree = Tree(root_node, MAX_DEPTH)
        tree.build(tree.get_root(), 0)
        #print ("First AI tree",tree.get_root().get_data().get_state())
        utility, move_i = minmax.alpha_beta(tree)
        print("First AI Best Move: Utility:", utility, "Best_Move:", move_i+1)
        board.take_stones(move_i)
        board.print_board()

        
        # """ AI player """
       # """ Comment below lines to disable AI """
        root_node = Node(board)
        tree = Tree(root_node, MAX_DEPTH)
        tree.build(tree.get_root(), 0)
        utility, move_i = minmax.alpha_beta(tree)
        print("Second AI Best Move: Utility:", utility, "Best_Move:", move_i+1)
        board.take_stones(move_i)
        board.print_board()

        '''
        root_node = Node(board)
        tree = Tree(root_node, MAX_DEPTH)
        tree.build(tree.get_root(), 0)
        utility, move_i = minmax.alpha_beta(tree)
        print("First AI Best Move: Utility:", utility, "Best_Move:", move_i+1)
        response = board.take_stones(move_i)
        board.print_board()
        if response == "continue":
            root_node = Node(board)
            tree = Tree(root_node, MAX_DEPTH)
            tree.build(tree.get_root(), 0)
            utility, move_i = minmax.alpha_beta(tree)
            print("Continue First AI Best Move: Utility:", utility, "Best_Move:", move_i+1)
            response = board.take_stones(move_i)
            board.print_board()
        
        game_end = board.terminate()
        if game_end:
            break

        board.reverse_player()
       
        root_node = Node(board)
        tree = Tree(root_node, MAX_DEPTH)
        tree.build(tree.get_root(), 0)
        utility, move_i = minmax.alpha_beta(tree)
        print("Second AI Best Move: Utility:", utility, "Best_Move:", move_i+1)
        response = board.take_stones(move_i)
        board.print_board()
        if response == "continue":
            root_node = Node(board)
            tree = Tree(root_node, MAX_DEPTH)
            tree.build(tree.get_root(), 0)
            utility, move_i = minmax.alpha_beta(tree)
            print("Continue Second AI Best Move: Utility:", utility, "Best_Move:", move_i+1)
            response = board.take_stones(move_i)
            board.print_board()

        game_end = board.terminate()
        if game_end:
            break

        '''
        
        """---------Player 2----------------"""
        """ Comment below lines to disable player 2 """
        print("Player 2 choose your move")
        pit_index_p2 = board.get_user_move()
        board.take_stones(pit_index_p2)
        board.print_board()
        """-------------end-----------------"""
       '''
        board.reverse_player()

  
    board.get_winner()
    print("Game is over")
