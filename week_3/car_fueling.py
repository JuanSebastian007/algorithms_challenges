# python3
import sys


def compute_min_refills(distance, tank, stops):
    num_refill, curr_refill = 0, 0 #Define numbers refill and current reffil position.
    while tank < distance: # If the distance is bigger that the tank capacity, return -1
        if curr_refill >= n or stops[curr_refill] > tank:
            return -1
        while curr_refill < n-1 and stops[curr_refill+1] <= tank: #If it's possible to arrival to the second station, then avance one station without refill
            curr_refill += 1
        #If tank capcity is less than the second station, 
        # then refill in the next station and added one refill. 
        num_refill += 1
        tank = stops[curr_refill] + tank
        curr_refill += 1
    return num_refill

if __name__ == '__main__':
    d = int(input())
    m = int(input())
    n = int(input())
    stops = list(map(int, input().split()))
    print(compute_min_refills(d, m, stops))
    print(compute_min_refills(d, m, stops))
