import copy


# track the game states
class Board:
    def __init__(self, turn):
        # set a dictionary to trace the number of the stones for the entire board
        self.state = {0: [4, 4, 4, 4, 4, 4, 0], 1: [4, 4, 4, 4, 4, 4, 0]}
        # who play the board right now
        self.turn = turn

    def print_board(self):
        state = self.get_state()
        print("==========================================")
        print("Computer", end=" ")
        print("|", end="  ")
        print(" |", end=" ")
        print(*state[0][:-1][::-1], sep=" | ", end="")
        print(" |", end="  ")
        print(" |")
        print("        ", end=" ")
        print("|", end=" ")
        print(state[0][-1], end=" ")
        print("|", end="")
        print("----------------------", end="")
        print(" |", end=" ")
        print(state[1][-1], end=" ")
        print("|")
        print("   Human", end=" ")
        print("|", end="  ")
        print(" |", end=" ")
        print(*state[1][0:-1], sep=" | ", end="")
        print(" |", end="  ")
        print(" |")
        print("==========================================")

    def get_turn(self):
        return self.turn

    # Make the board snapshoot
    def get_state(self):
        return copy.deepcopy(self.state)

    def reverse_player(self):
        if self.turn == 1:
            self.turn = 0
        else:
            self.turn = 1

    def take_stones(self, pit_index):
        if not self.pit_not_empty_rule(pit_index):
            return False

        pit_index = pit_index if self.turn == 1 else 12 - pit_index

        state_array = self.state[1] + self.state[0]

        pit_stones = state_array[pit_index]

        state_array[pit_index] = 0

        for i in range(pit_stones):
            pit_index += 1
            if self.turn == 1 and pit_index == 13:
                pit_index = 0
            elif self.turn == 0 and pit_index == 6:
                pit_index = 7
            elif pit_index > 13:
                pit_index = 0
            state_array[pit_index] += 1

        if state_array[pit_index] == 1:
            if self.turn == 1:
                to_capture_pit = abs(pit_index - 12)
                capture_stones = state_array[to_capture_pit] + state_array[pit_index]
                state_array[to_capture_pit] = 0
                state_array[pit_index] = 0
                state_array[6] += capture_stones

        self.state[1] = state_array[:7]
        self.state[0] = state_array[7:]

        if pit_index == 6 and self.turn == 1:
            self.continue_playing()

        if pit_index == 13 and self.turn == 0:
            self.continue_playing()

        return True

    def terminate(self):
        player_one_pits = self.state[1][:-1][::-1]
        player_two_pits = self.state[0][:-1][::-1]
        return all(stones == 0 for stones in player_one_pits) or all(
            stones == 0 for stones in player_two_pits
        )

    def pit_not_empty_rule(self, pit_index):
        if self.turn == 0:
            player_pits = self.state[self.turn][:-1][::-1] + [self.state[self.turn][-1]]
        else:
            player_pits = self.state[self.turn]

        if player_pits[pit_index] == 0:
            print("You can not pick from an empty pit, try another one")
            pit_index = int(input()) - 1
            self.take_stones(pit_index)
            return False
        return True

    def continue_playing(self):
        if not self.terminate():
            self.print_board()
            print("Hurry!! pick another stone from your side :)")
            pit_index = int(input()) - 1
            self.take_stones(pit_index)
        return True

    def get_winner(self):
        self.state[1][-1] += sum(self.state[1][:-1][::-1])
        self.state[1][:-1] = [0] * (len(self.state[1]) - 1)
        self.state[0][-1] += sum(self.state[0][:-1][::-1])
        self.state[0][:-1] = [0] * (len(self.state[0]) - 1)
        self.print_board()
        player1Stones = self.state[1][-1]
        player2Stones = self.state[0][-1]
        if player1Stones > player2Stones:
            print("Player 1 has won the game")
        elif player1Stones < player2Stones:
            print("Player 2 has won the game")
        else:
            print("The match has been drawn")
