from typing import List

def find_max_sum_subarray(k, arr: List):
    maxSum, maxSubArray = 0.0, []
    windowSum, windowStart = 0.0, 0
    for windowEnd in range(len(arr)):
        windowSum += arr[windowEnd]
        if windowEnd >= k - 1:
            if windowSum >= maxSum:
                maxSum = windowSum
                maxSubArray = arr[windowStart:windowEnd+1]
            windowSum -= arr[windowStart]
            windowStart += 1
    return maxSubArray


def main():
    result = find_max_sum_subarray(2, [2, 3, 4, 1, 5])
    print(f'Subarray with maximum sum is {result}')


main()
