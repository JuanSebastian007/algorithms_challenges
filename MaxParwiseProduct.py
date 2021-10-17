def max_pairwise_product(numbers):

    """""
    A function that computing a Fibonacci Series in a way that successive executing a sum.

    Params
    n: The number that runs Fibonacci Serie. Type: Integer.
    """

    long = len(numbers)
    size = long - 1
    index = 0
    for i in range(1, long):
        if numbers[i] > numbers[index]:
            index = i
    numbers[index], numbers[size] = numbers[size], numbers[index]

    index = 0
    for i in range(1, long - 1):
        if numbers[i] > numbers[index]:
            index = i
    numbers[index], numbers[size-1] = numbers[size-1], numbers[index]

    return numbers[size-1]*numbers[size]

if __name__ == '__main__':

    input_n = int(input()) #Array length 
    input_numbers = [int(x) for x in input().split()] #Numbers at the array
    print(max_pairwise_product(input_numbers))

