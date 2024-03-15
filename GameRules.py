class GameRules:
    def __init__(self, board):
        self.board = board

    def pit_not_empty_rule(self, player, pit_index):
        player_pits = self.board.state(player)
        if player_pits[pit_index] == 0:
            return False
        return True

    def check_pite_owner(self, player, pit_index):
        return player == self.board.get_pit_owner(pit_index)

    def check_if_pites_are_empty(self, player):
        player_pits = self.board.state(player)
        return any(stones > 0 for stones in player_pits)

    def capture_stones(board, player, last_pit_index):
    kalaha_index = len(board.state[player]) - 1
    opposite_pit_index = len(board.state[player]) - 1 - last_pit_index

    if board.state[player][last_pit_index] == 1 and board.state[player][last_pit_index] == 0 and board.state[player][opposite_pit_index] > 0:
        captured_stones = board.state[player][opposite_pit_index]
        board.state[player][opposite_pit_index] = 0
        board.state[player][kalaha_index] += captured_stones

    return board

    def distribute_stones(board, player, start_pit_index, stones):
    current_pit_index = start_pit_index
    num_pits = len(board.state[player]) - 1

    while stones > 0:
        current_pit_index = (current_pit_index + 1) % num_pits
        if current_pit_index == num_pits:
            continue
        board.state[player][current_pit_index] += 1
        stones -= 1

    return board

    def check_winning_state(self):
        total_stones_player1 = self.board.state(1)
        total_stones_player2 = self.board.state(2)
        if total_stones_player1 == 0 or total_stones_player2 == 0:
            if total_stones_player1 > total_stones_player2:
                return 1
            elif total_stones_player1 < total_stones_player2:
                return 2
            else:
                return 0  # Draw
        return None
