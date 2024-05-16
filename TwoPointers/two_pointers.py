from typing import List

# #189 Rotate Array. Time O(n), Space O(1)
def rotate(nums: List[int], k: int) -> None:
    """
    Do not return anything, modify nums in-place instead.
    """
    # cases when k is greater than length of array
    k: int = k % len(nums)
    left: int = 0
    right: int = len(nums) - 1

    # reverse list by swapping
    while left < right:
        tmp: int = nums[left]
        nums[left] = nums[right]
        nums[right] = tmp
        left += 1
        right -= 1

    # reverse from start of list to k
    left = 0
    right = k - 1
    while left < right:
        tmp: int = nums[left]
        nums[left] = nums[right]
        nums[right] = tmp
        left += 1
        right -= 1

    # reverse from k to end of list
    left = k
    right = len(nums) - 1
    while left < right:
        tmp: int = nums[left]
        nums[left] = nums[right]
        nums[right] = tmp
        left += 1
        right -= 1


def main():
    nums: List[int] = [1, 2, 3, 4, 5, 6, 7]
    rotate(nums, 3)
    print(nums)


if __name__ == "__main__":
    main()