def main():
    while(True):
        # get a case 
        case = input().split()
        # assign no of calls and no of intervals to variables
        no_calls = int(case[0])
        no_intervals = int(case[1])

        # check if we are at end case
        if (no_calls == 0 and no_intervals == 0):
            exit()


        # create an array to keep track of call intervalas
        call_intervals = a = [[0] * 2 for i in range(no_calls)]

        # populate array by keep track of each intreval for each call for example
        # [2,5] becomes [2,7] as we add duration to start to get end time
        for i in range(no_calls):
            call = input().split()
            call = [int(x) for x in call]
            call_intervals[i][0] = call[2]
            call_intervals[i][1] = call[2] + call[3]


        # keep track of intersecting intervals
        no_of_calls_in_interval = 0
        for i in range(no_intervals):
            # get intervals to check and change them to the same format as for calls
            # ex: interval [8,2] becomes [8,10] as we add duration to start to get end time
            intervals = input().split()
            intervals = [int(x) for x in intervals]
            intervals[1] = intervals[0] + intervals[1]
            
            # print("call intervals: ", call_intervals)
            # print("intervals: ",intervals)

            # to check if two intervals overlap we check if the the start of the first
            # is less than the end of the second AND that the start of the second
            # is smaller than the end of the first
            for j in range(no_calls):
                x1 = call_intervals[j][0]
                x2 = call_intervals[j][1]
                y1 = intervals[0]
                y2 = intervals[1]
                # print("x1", x1)
                # print("x2", x2)
                # print("y1", y1)
                # print("y2", y2)
                if (x1<y2 and y1<x2):
                    no_of_calls_in_interval += 1
                
            print(no_of_calls_in_interval)
            no_of_calls_in_interval = 0
        


if __name__ == '__main__':
    main()