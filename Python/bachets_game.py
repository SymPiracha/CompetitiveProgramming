import sys


def result(game):
    
    list_of_moves = game[2:]
    list_of_results = [False] * (game[0]+1)

    # if one stone is left and it is your turn you always win
    list_of_results[1] = True
    
    # iterate through all possible turns starting from the second one and moving up
    for i in range(2,game[0] + 1):
        number_left = i
        for move in list_of_moves:
            stones_after_move = number_left-move
            # if playing a certain move leaves 0 or more stones on the table continue
            if (stones_after_move >= 0):
                # if by removing all the stones, you win then change the result to true in the array
                if stones_after_move == 0:
                    list_of_results[i] = True
                # else if by picking a certain move you get to false value, this means that the opponent cant win so you win
                elif list_of_results[stones_after_move] == False:
                    list_of_results[i] = True

    if list_of_results[game[0]]:
        print("Stan wins")
    else:
        print("Ollie wins")

def main(): 
    for line in sys.stdin:
        line = line.split()
        game = [int(numeric_string) for numeric_string in line]
        result(game)

if __name__ == '__main__':
    main()
