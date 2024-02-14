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


# Find all unique subsets
unique_subsets = find_unique_subsets(nums)

# Calculate sums of all unique subsets
sums = subset_sums(unique_subsets)

# Print all repeated sums
repeated_sums = {k: v for k, v in sums.items() if len(v) > 1}
for sum_, subsets in repeated_sums.items():
    print(f"Sum: {sum_}, Subsets: {subsets}")
