def printboard(xState, zState):
    print(f"0 | 1 | 2")
    print(f"__|___|__")
    print(f"3 | 4 | 5")
    print(f"__|___|__")
    print(f"6 | 7 | 8")
    print(f"__|___|__")

if __name__ == "__main__":
    xState=[0, 0, 0, 0, 0, 0, 0, 0, 0, ]
    zState=[0, 0, 0, 0, 0, 0, 0, 0, 0, ]
    turn = 1 #1 for X and 0 for O
    print("welcome to tic tac toe")
    while(True):
        printboard(xState, zState)
        if(turn==1):
            print("X's chance")
            value= int(input("please a enter a value"))
            xState[value]=1
        else:
            print("Y's chance")
            value= int(input("please a enter a value"))
            xState[value]=1
            break