import itertools

def remaining_fruit_weight(all_fruits, i):
    remaining_fruits = 0
    for fruit in itertools.islice(all_fruits, i + 1, len(all_fruits), 1):
        remaining_fruits += fruit
    return remaining_fruits


def weights(all_fruits, index, no_of_fruits, boolean_array):
    # if we are at the last index, try calculating the sum both with last fruit included and excluded
    if index == no_of_fruits - 1:
        boolean_array[index] = True
        last_included = 0
        for j in range(index + 1):
            if boolean_array[j]:
                last_included += all_fruits[j]
        # if sum with the last included <200, return 0
        if last_included < 200:
            return 0

        # calculate sum with last excluded now
        boolean_array[index] = False
        last_excluded = 0
        for j in range(index + 1):
            if boolean_array[j]:
                last_excluded += last_excluded
        # if sum with last excluded is < 200, included last fruit
        if last_excluded < 200:
            return last_included
        else:
            return last_excluded

    # do not included the fruit if we are not at the last index and try calculating the weight both with current
    # fruit in the basket and without
    else:
        # include fruit at current index
        boolean_array[index] = True
        sum_fruit_included = 0
        for j in range(index + 1):
            if boolean_array[j]:
                sum_fruit_included += all_fruits[j]
        # if weight of fruits is greater than 200 add all fruits after the index too
        # calculate sum of fruits that come after the current index
        remaining_fruits = remaining_fruit_weight(all_fruits, index)
        # if weight is > 200 get all combinations of fruits where the current ones are included
        if sum_fruit_included >= 200:
            w2 = 2 ** (no_of_fruits - index - 2) * (2 * sum_fruit_included + remaining_fruits)
        else:
            # else call the function but for the next fruit, including current fruit in basket
            w2 = weights(all_fruits, index + 1, no_of_fruits, boolean_array)
        # do not include at current index and calculate weight of fruits remaining
        boolean_array[index] = False
        remaining_fruits = remaining_fruit_weight(all_fruits, index)
        # calculate weight of fruits so far
        sum_fruit_included = 0
        for j in range(index + 1):
            if boolean_array[j]:
                sum_fruit_included += all_fruits[j]
        if sum_fruit_included >= 200:
            w1 = 2 ** (no_of_fruits - index - 2) * (2 * sum_fruit_included + remaining_fruits)
        else:
            # else call the function but for the next fruit, excluding current fruit
            w1 = weights(all_fruits, index + 1, no_of_fruits, boolean_array)
        return w1 + w2


def main():
    # Get Number of fruits
    no_of_fruits = int(input())

    # Get an array of all the weights of the fruits
    all_fruits = input().split()

    # Convert strings array into int array
    for i in range(len(all_fruits)):
        all_fruits[i] = int(all_fruits[i])

    # Sort all fruits in descending order of weight
    all_fruits = sorted(all_fruits, reverse=True)

    # Create a boolean array to keep track of if we want to included fruit or not
    boolean_array = [False] * no_of_fruits

    print(weights(all_fruits, 0, no_of_fruits, boolean_array))



if __name__ == "__main__":
    main()
