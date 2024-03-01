def print_board():
    state={0:[4]*6+[0],
           1:[4]*6+[0]}
    
    print ("-------------Kalaha----------------")
    print ("-------------By Group 39-----------")

    print ("You will play this game with the computer.Please pick up your stones from your side first")
    print("==========================================")
    print("Computer", end=" ");print("|", end="  "); print(" |",end=" ");print(*state[0][0:-1],sep=" | ",end="");print(" |",end="  ");print(" |")
    print("        ", end=" ");print("|", end=" "); print(state[0][-1],end=" ");print("|",end="");print("----------------------",end="");print(" |",end=" ");print(state[1][-1],end=" ");print("|")
    print("   Human", end=" ");print("|", end="  "); print(" |",end=" ");print(*state[1][0:-1],sep=" | ",end="");print(" |",end="  ");print(" |")
    print("==========================================")

if __name__ == "__main__":
    print_board()
   

