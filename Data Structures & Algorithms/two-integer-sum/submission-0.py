#use an index loop
#create a hash map with each number and its complement (target - value)
#if number in hash map vals, return number and key 


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        check = {}
        for i in range(0, len(nums)):
            complement = target - nums[i]
            if complement in check:
                return [check[complement], i]
            check[nums[i]] = i
                