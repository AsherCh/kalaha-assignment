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
        """This method handles the moment of the stones"""
        # Check the choosed pit is not empty
        if not self.pit_not_empty_rule(pit_index):
            return "empty_pit"

        # get the pit_index
        pit_index = pit_index if self.turn == 1 else 12 - pit_index

        state_array = self.state[1] + self.state[0]

        pit_stones = state_array[pit_index]

        state_array[pit_index] = 0

        for i in range(pit_stones):
            pit_index += 1
            # skip the kalaha's of the opponent player
            if self.turn == 1 and pit_index == 13:
                pit_index = 0
            elif self.turn == 0 and pit_index == 6:
                pit_index = 7
            elif pit_index > 13:
                pit_index = 0
            # Destribute the stones from choosen pit in to next pits, including players own kalaha
            state_array[pit_index] += 1
        # print (state_array)
        # If the last stone ends up in an empty pit and the opponent has stones, then steal the opponent's stones
        if state_array[pit_index] == 1:
            # check the last stone doesn't end up in kalaha's
            if pit_index not in (6, 13):
                # get the index of opponent's pit
                to_capture_pit = abs(pit_index - 12)
                # check player and some inital knowledge
                if self.turn == 1:
                    player_kalaha = 6
                    pit_start_index = 0
                else:
                    player_kalaha = 13
                    pit_start_index = 7

                # check that the opponent's pit is not empty, and also that the last pit is player's own pit
                if (
                    state_array[to_capture_pit] != 0
                    and pit_start_index <= pit_index < player_kalaha
                ):
                    # get stones from both pits
                    capture_stones = (
                        state_array[to_capture_pit] + state_array[pit_index]
                    )
                    # empty opponents pit
                    state_array[to_capture_pit] = 0
                    # empty player's pit
                    state_array[pit_index] = 0
                    # add captured/stealed stones into player's kalaha
                    state_array[player_kalaha] += capture_stones

        # update board state after move
        self.state[1] = state_array[:7]
        self.state[0] = state_array[7:]

        # check if the last stone ends in player's kalaha
        if (pit_index == 6 and self.turn == 1) or (pit_index == 13 and self.turn == 0):
            return "continue"

        return True

    def terminate(self):
        """This method implements kalaha termination/end by checking that either player's pits are empty"""

        player_one_pits = self.state[1][:-1][::-1]
        player_two_pits = self.state[0][:-1][::-1]
        return all(stones == 0 for stones in player_one_pits) or all(
            stones == 0 for stones in player_two_pits
        )

    def pit_not_empty_rule(self, pit_index):
        """This method implements kalaha rule that the player can't choose an empty pit."""

        if self.turn == 0:
            player_pits = self.state[self.turn][:-1][::-1] + [self.state[self.turn][-1]]
        else:
            player_pits = self.state[self.turn]

        if player_pits[pit_index] == 0:
            return False
        return True

    def pit_empty(self):
        print("You can not pick from an empty pit, try another one")
        pit_index = self.get_user_move()
        response = self.take_stones(pit_index)
        if response == "empty_pit":
            self.pit_empty()
        return response

    def continue_playing(self):
        """This method implements kalaha rule that if the last stone ends up in players kalaha then the player can make another move.
        Therefore, named as continue_playing"""
        response = False
        if not self.terminate():
            print("Hurry!! pick another stone from your side :)")
            pit_index = self.get_user_move()
            response = self.take_stones(pit_index)
            self.print_board()

        return response

    def get_winner(self):
        """This method is defined to get the winner of the game."""

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

    def get_user_move(self):
        """Validates the user input and ensure that the input must be an int and in range of valid moves."""

        try:
            move = int(input()) - 1
            if move in range(6):
                return move
            else:
                print("Invalid input please enter a number between 1 and 6")
                self.get_user_move()
        except ValueError:
            print("Invalid input please enter a number between 1 and 6")
            self.get_user_move()
