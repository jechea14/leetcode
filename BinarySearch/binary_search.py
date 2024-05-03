# #704 Binary Search
from typing import List


# #704 Binary Search
def search(nums: List[int], target: int) -> int:
    left: int = 0
    right: int = len(nums) - 1

    while left <= right:
        middle: int = (left + right) // 2
        if nums[middle] == target:
            return middle
        elif nums[middle] < target:
            left = middle + 1
        else:
            right = middle - 1

    return -1


# #35 Search Insert Position
def searchInsert(nums: List[int], target: int) -> int:
    left: int = 0
    right: int = len(nums) - 1

    while left <= right:
        middle: int = (left + right) // 2
        if nums[middle] == target:
            return middle
        elif nums[middle] < target:
            left = middle + 1
        else:
            right = middle - 1

    return left

# #74 Search a 2D Matrix
def searchMatrix(matrix: List[List[int]], target: int) -> bool:
    

nums: List[int] = [-1, 0, 3, 5, 9, 12]
print(search(nums, 9))
