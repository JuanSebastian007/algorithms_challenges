def max_pairwise_product(numbers):
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
    input_n = int(input())
    input_numbers = [int(x) for x in input().split()]
    print(max_pairwise_product(input_numbers))

