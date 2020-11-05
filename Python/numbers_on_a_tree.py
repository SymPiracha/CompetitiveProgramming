def main():
    # get input case
    case = input().split()
    # extract first value of input array
    height = int(case[0])
    # calculate the size of the array needed to hold this tree
    # this will be the number of nodes in the tree
    array_size = (2**(height+1)) - 1 
    
    # numbering from right to left is the same as creating an array and filling it from height to one
    # parent node = i-1/2
    # left child = 2i + 1
    # right child = 2i+2

    # iterate through the traversal order if given
    array_index = 0
    if len(case) > 1:
        traversal = case[1]
        for letter in traversal:
            # if letter is R, go to right child
            if letter == 'R':
                array_index = 2*array_index+2
            # if letter is L, go to left child
            elif letter == 'L':
                array_index = 2*array_index+1

    # get node value by subtracting array size with which index we are at
    print(array_size - array_index)
    
if __name__ == '__main__':
    main()