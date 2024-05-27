from typing import List


def permute(nums):
    def backtrack(path):
        # If the path length is equal to nums length, we have a complete permutation
        if len(path) == len(nums):
            res.append(path[:])  # Append a copy of path to results
            return

        # Iterate through the available numbers
        for num in nums:
            if num in path:
                continue  # Skip already used numbers
            path.append(num)  # Choose
            backtrack(path)  # Explore
            path.pop()  # Un-choose (backtrack)

    res = []
    backtrack([])
    return res


# #77 Combinations
def combine(n: int, k: int) -> List[List[int]]:

    def backtrack(start, path):
        # if path length is equal to k, we have a combination
        # add to result
        # return to go back up
        if len(path) == k:
            result.append(path[:])
            return

        # starting from 1
        for i in range(start, n + 1):
            path.append(i)
            # prevnt from adding previous numbers
            backtrack(i + 1, path)
            path.pop()  # backtrack

    result = []
    path = []
    backtrack(1, path)  # start from 1 and pass in empty list
    return result


# Example usage:
nums = [1, 2, 3]
# print(permute(nums))
print(combine(4, 2))
