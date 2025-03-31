# Problem 1: Two Sum
# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

nums = [2,7,11,15]
target = 9
def twoSum(nums, target):
    num_map = {}  
    for i, num in enumerate(nums):
        res = target - num
        if res in num_map:
            return [num_map[res], i]
        num_map[num] = i
    return []


nums = [2, 7, 11, 15]
target = 9
print(twoSum(nums, target))  



# The enumerate() function adds a counter to an iterable and returns it in the form of an enumerate object.
# This enumerate object can then be used directly in for loops or converted into a list of tuples using the list() method.
# The enumerate() function is useful when you need a counter with the values in the iterable.
# It allows you to loop over something and have an automatic counter.

