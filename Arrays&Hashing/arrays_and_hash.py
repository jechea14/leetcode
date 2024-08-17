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


# #49. Group Anagrames
"""Given an array of strings strs, group the anagrams together. You can return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

Example 1:

Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

Example 2:

Input: strs = [""]
Output: [[""]]

Example 3:

Input: strs = ["a"]
Output: [["a"]]
"""


def groupAnagrams(strs):
    """
    :type strs: List[str]
    :rtype: List[List[str]]
    """
    sorted_dict = {}  # sorted_string: [strs]
    result = []

    # For each string, sort it then join it back together
    for s in strs:
        sorted_str = "".join(sorted(s))
        # Insert the sorted string into a dict based on key
        if sorted_str in sorted_dict:
            sorted_dict[sorted_str].append(s)
        # If not found then create an entry of the sorted string
        else:
            sorted_dict[sorted_str] = []
            sorted_dict[sorted_str].append(s)

    # Grab the values of the sorted_strings then append to result arr
    for items in sorted_dict.values():
        result.append(items)
    return result


# #238 Product of Array Except Self
"""
Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].
The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
You must write an algorithm that runs in O(n) time and without using the division operation.

Example 1:

Input: nums = [1,2,3,4]
Output: [24,12,8,6]

Example 2:

Input: nums = [-1,1,0,-3,3]
Output: [0,0,9,0,0]

Constraints:

    2 <= nums.length <= 105
    -30 <= nums[i] <= 30
    The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
"""


def productExceptSelf(nums):
    """
    :type nums: List[int]
    :rtype: List[int]
    """


# print(majorityElements([3, 2, 3]))
# print(twoSum([2, 7, 11, 15], 9))
print(groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
