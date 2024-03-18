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

    def get_ai_move():
        root_node = Node(board)
        tree = Tree(root_node, MAX_DEPTH)
        tree.build(tree.get_root(), 0)
        utility, best_move = minmax.alpha_beta(tree)
        print("AI Best Move: Utility:", utility, "Best_Move:", best_move + 1)
        return best_move

    def continue_playing(is_ai=False):
        if is_ai:
            move_i = get_ai_move()
            response = board.take_stones(move_i)
            board.print_board()
        else:
            response = board.continue_playing()
            if response == "empty_pit":
                board.pit_empty()
                board.print_board()

        if response == "continue":
            continue_playing(is_ai)

        return True

    minmax = Minmax(evaluation_function2, find_children, MAX_DEPTH)

    game_end = False
    while not game_end:
        # Human input the first move
        current_player = board.get_turn()
        print(current_player, " Human,please pick up your stones from your side:")
        pit_index = board.get_user_move()
        response = board.take_stones(pit_index)
        board.print_board()
        if response == "empty_pit":
            board.pit_empty()
            board.print_board()
        elif response == "continue":
            continue_playing()

        game_end = board.terminate()
        if game_end:
            break

        board.reverse_player()

        move_i = get_ai_move()
        response = board.take_stones(move_i)
        board.print_board()
        if response == "empty_pit":
            board.pit_empty()
            board.print_board()
        elif response == "continue":
            continue_playing(True)

        game_end = board.terminate()
        if game_end:
            break

        board.reverse_player()

    board.get_winner()
    print("Game is over")
