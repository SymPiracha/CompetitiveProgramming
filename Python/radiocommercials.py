
def profit_calc(slots,cost):
    # keep two variables that keep track of the best profit so far and one that keep trackts of the current profit being calculated
    best_profit = 0
    current_profit = 0
    # iterate through all the slots
    for slot in slots:
        # turn slot into an in and to get profit/loss per slot subtract the cost
        per_slot = int(slot) - cost
        # include the current slot in the current proft
        current_profit = current_profit + per_slot
        # if the current profit is negative, discard the slots and start over
        if current_profit <= 0:
            current_profit = 0
        # if current proft > best profit, change it to best profit
        if current_profit > best_profit:
            best_profit = current_profit
    
    return best_profit



def main():
    firstline = input().split()
    # get the cost of each commericial
    cost = int(firstline[1])
    # Get an array of slots
    slots = input().split()
    # print result from function
    print(profit_calc(slots, cost))
    
if __name__ == '__main__':
    main()
