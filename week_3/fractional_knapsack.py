# Uses python3
import sys

def get_optimal_value(capacity, weights, values):
     index = list(range(len(values))) #Make a index list according to values size
     ratio = [v/w for v, w in zip(values, weights)] #First, I take a tuples array with v and w. Then, I divide v/W with a foor loop into an array
     index.sort(key=lambda i: ratio[i], reverse=True) #Sorts the list accordign to the ratio value

     value = 0
     fractions = [0]*len(values) # Starting the fractions arrays and filled value
     for i in index:
        if weights[i] <= capacity: #If the largest value is less bigger that the capacity, I should use whole object.
            fractions[i] = 1
            value += value[i]
            capacity -= weights[i]
        else:  #If the larguest value is bigger that the capacity, I should fill the capacity with these object.
            fractions[i] = capacity / weights[i]
            value += value[i] * capacity / weights[i]
            break
     return value

if __name__ == "__main__":
    data = list(map(int, sys.stdin.readline().split()))
    n, capacity = data[0:2]
    values = data[2:(2 * n + 2):2]
    weights = data[3:(2 * n + 2):2]
    opt_value = get_optimal_value(capacity, weights, values)
    print("{:.10f}".format(opt_value))
