# #704 Binary Search
from typing import List
import math


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
    row_left: int = 0
    row_right: int = len(matrix) - 1
    col_left: int = 0
    col_right: int = len(matrix[0]) - 1
    row_middle: int = 0

    while row_left <= row_right:
        row_middle = (row_left + row_right) // 2
        if target < matrix[row_middle][0]:
            row_right = row_middle - 1
        elif target > matrix[row_middle][-1]:
            row_left = row_middle + 1
        else:
            break

    while col_left <= col_right:
        col_middle: int = (col_left + col_right) // 2
        if matrix[row_middle][col_middle] == target:
            return True
        elif matrix[row_middle][col_middle] < target:
            col_left = col_middle + 1
        else:
            col_right = col_middle - 1

    return False


# #153 Find Minimum in Rotated Sorted Array
def findMin(nums: List[int]) -> int:
    min_val: int = math.inf
    left: int = 0
    right: int = len(nums) - 1

    while left <= right:
        # if the array is sorted
        if nums[left] < nums[right]:
            min_val = min(min_val, nums[left])
            break
        mid: int = (left + right) // 2
        # compare min value with current mid value
        min_val = min(min_val, nums[mid])
        if nums[mid] >= nums[left]:
            # search to the right
            left = mid + 1
        else:
            # search to the left
            right = mid - 1

    return min_val


# #33 Search in Rotated Sorted Array
def searchRotatedArray(nums: List[int], target: int) -> int:
    left: int = 0
    right: int = len(nums) - 1

    while left <= right:
        mid: int = (left + right) // 2

    return -1


# matrix: List[List[int]] = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]]
# nums: List[int] = [-1, 0, 3, 5, 9, 12]
# print(search(nums, 9))
# print(searchMatrix(matrix, 13))
# print(findMin([2, 1]))
print(searchRotatedArray([4, 5, 6, 7, 0, 1, 2], 0))
