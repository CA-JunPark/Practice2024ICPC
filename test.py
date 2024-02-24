from itertools import combinations
from collections import defaultdict

# Given list
nums = [21, 13, 13, 11, 11, 11, 18, 18, 18, 18, 16,16,16, 19,19]

# Function to find all unique subsets and their sums


def find_unique_subsets(nums):
    subsets = set()
    for i in range(len(nums) + 1):
        # Sort each subset and add to set
        subsets.update(combinations(sorted(nums), i))
    return subsets

# Calculate sum of subsets


def subset_sums(subsets):
    sums = defaultdict(list)
    for subset in subsets:
        sums[sum(subset)].append(subset)
    return sums


def binarySearch(arr, l, r, x):
    while l <= r:
        mid = l + (r - l) // 2
        # Check if x is present at mid
        if arr[mid] == x:
            return mid
        # If x is greater, ignore left half
        elif arr[mid] < x:
            l = mid + 1
        # If x is smaller, ignore right half
        else:
            r = mid - 1
    # If we reach here, then the element
    # was not present
    return -1


a = [1,2,3,4,5,6,7,8,110, 2312, 213123]

print(binarySearch(a,0,len(a)-1,4))