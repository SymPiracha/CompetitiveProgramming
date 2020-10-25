

def main():
    n = int(input())

    for i in range(n):
        line = input().split()
        if line[0] == 'Simon' and line[1] == 'says':
           
            str = ' '.join(line[2:])
            print(str)

if __name__ =='__main__':
    main()