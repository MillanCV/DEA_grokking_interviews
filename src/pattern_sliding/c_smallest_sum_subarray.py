'''
Given an array of positive numbers and a positive number ‘S’, 
find the length of the smallest contiguous subarray whose sum 
is greater than or equal to ‘S’. Return 0, if no such subarray exists.
'''


def find_small_sum_subarray(s, arr):
    lenArray = 0
    winStart, winSum = 0, 0
    
    for winEnd in range(len(arr)):
        winSum += arr[winEnd]
        
        if winSum > s:
            lenArray = len(arr[winStart, winEnd])
            winStart += 1
    
    return lenArray


def main():
    result = find_small_sum_subarray(7, [2, 1, 5, 2, 3, 2])
    print(f'Subarray with maximum sum is {result}')


main()
