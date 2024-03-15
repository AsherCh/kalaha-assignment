def evaluation_fuction(board):
    #calculate the utility value
    state = board.get_state()
    utility_value = 0
    # the score of each player = the number of stealing stones
    human_score = sum(state[0])
    computer_score = sum(state[1])
    #utility = player1_score - player2_score
    utility_value = computer_score - human_score
    return utility_value


def check_utility():
    #check the player utilty 
    pass
