


def days(list_of_seeds):
    # create an int array which will keep track of days left for each seed
    list_days = [None] * len(list_of_seeds)
    # loop through all the seeds 
    for i in range(len(list_of_seeds)):
        # for each seed add it to the list that keeps tracks of days. Compute the days it will take for each key by subtracting the days left to plant the rest of the seeds
        # this will be done by subtracting seed by the seeds that have to be planted after the current seed
        list_days[i] = list_of_seeds[i] - (len(list_of_seeds) - i)
    # days left will be the max days left for any particular seed + the the days it took to plant the all the seeds
    days = max(list_days) + len(list_of_seeds) + 2
    print(days)




def main():
    # get the number of seedlings to be be planted
    n = int(input())
    # get list of  seedling as an int array
    list_of_seeds = input().split()
    list_of_seeds = [int(seed) for seed in list_of_seeds]
    # sort list into reverse, starting with seeds taking the most days 
    list_of_seeds.sort(reverse=True)
    days(list_of_seeds)



if __name__ == '__main__':
    main()
