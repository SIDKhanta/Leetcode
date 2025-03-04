class Solution:
    def twoSum(self, nums, target):
        hash_map = {}  
        for i in range(len(nums)):
            razn = target - nums[i]  
            if razn in hash_map:  
                return [hash_map[razn], i] 
            hash_map[nums[i]] = i 