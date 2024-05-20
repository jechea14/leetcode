"""


"""
from typing import List, Dict


# #1 Two Sum
def twoSum(nums: List[int], target: int) -> List[int]:
    number_map = {}
    result = []
    for i in range(len(nums)):
        diff = target - nums[i]
        # if the difference is found as a key in the dict
        # result has the dict key of difference, i
        if diff in number_map:
            result = [number_map[diff], i]
        else:
            # create a nums key with i value
            number_map[nums[i]] = i
    return result


# #169 Majority Element
def majorityElements(nums: List[int]) -> int:
    occurrences = {}

    for i in range(len(nums)):
        if nums[i] in occurrences:
            occurrences[nums[i]] += 1
        else:
            occurrences[nums[i]] = 1

    val = [0, 0]
    for key in occurrences:
        if occurrences[key] > val[1]:
            val[0] = key
            val[1] = occurrences[key]

    print(occurrences)
    return val[1]


print(majorityElements([3, 2, 3]))
print(twoSum([2, 7, 11, 15], 9))
