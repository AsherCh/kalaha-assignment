# comparing the number of stones in all player's positions (pits+kalaha)
def evaluation_function(board):
    #calculate the utility value
    state = board.get_state()
    # the score of each player = the number of stealing stones
    human_score = sum(state[1])
    computer_score = sum(state[0])
    utility_value = computer_score - human_score
    return utility_value

# comparing the number of stones only in kalahas
def evaluation_function2(board):
    state = board.get_state()
    #last position in array [-1]
    human_kalah = state[1][-1]
    computer_kalah = state[0][-1]
    utility_value = computer_kalah - human_kalah
    return utility_value

# taking into consideration both kalaha and empty pits
def evaluation_function3(board):
    state = board.get_state()
    # last position in array [-1]
    human_kalah = state[1][-1]
    computer_kalah = state[0][-1]
    human_pits = state[1][:-1]
    computer_pits = state[0][:-1]
    human_empty_pits = 0
    computer_empty_pits = 0
    for i in human_pits:
        if i == 0:
            human_empty_pits += 1
    for i in computer_pits:
        if i == 0:
            computer_empty_pits += 1

    utility_value = (computer_kalah - human_kalah) * (human_empty_pits - computer_empty_pits)
    return utility_value

# taking into consideration all seeds in pits + kalaha and empty pits
def evaluation_function4(board):
    # calculate the utility value
    state = board.get_state()
    utility_value = 0
    # the score of each player = the number of stealing stones
    human_score = sum(state[1])
    computer_score = sum(state[0])
    human_pits = state[1][:-1]
    computer_pits = state[0][:-1]
    human_empty_pits = 0
    computer_empty_pits = 0
    for i in human_pits:
        if i == 0:
            human_empty_pits += 1
    for i in computer_pits:
        if i == 0:
            computer_empty_pits += 1

    utility_value = (computer_score - human_score) * (human_empty_pits - computer_empty_pits)
    return utility_value

def evaluation_function5(board):
    return 10


def evaluation_function6(board):
    return -8

