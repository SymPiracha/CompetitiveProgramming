
def min_product(v1,v2, case_number):
    v1.sort()
    v2.sort(reverse=True) 
    # print(v1)
    # print(v2)
    product = 0
    for i in range(len(v1)):
        product = product + ( v1[i] * v2[i])
    print(f'Case #{case_number+1}: {product}')

   

def main():
    test_cases = int(input())
    # print(test_cases)

    for i in range(test_cases):
        number_of_cords = int(input())
        v1 = input().split()
        v1 = [int(coord) for coord in v1]
        v2 = input().split()
        v2 = [int(coord) for coord in v2]
        # print(v1)
        # print(v2)
        min_product(v1,v2, i)

if __name__ == '__main__':
    main()