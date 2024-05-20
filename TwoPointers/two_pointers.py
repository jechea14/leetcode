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


# #1768 Merge String Alternately
def mergeAlternately(word1: str, word2: str) -> str:
    result = ""
    # start at beginning
    p1 = 0
    p2 = 0

    # iterate through input lengths
    while p1 < len(word1) and p2 < len(word2):
        # concatenate character to result
        result += word1[p1]
        result += word2[p2]
        # move pointers forward
        p1 += 1
        p2 += 1

    # for arrays that are longer than the other
    # in which it broke out of the while loop
    # append the remaining characters to result
    if p1 < len(word1):
        result += word1[p1:]
    if p2 < len(word2):
        result += word2[p2:]
    return result


def main():
    nums: List[int] = [1, 2, 3, 4, 5, 6, 7]
    rotate(nums, 3)
    print(nums)


if __name__ == "__main__":
    main()
