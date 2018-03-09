class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        o = {}
        for i in range(len(nums)):
            if target - nums[i] in o:
                return [o[target - nums[i]],i]
            else :
                o[nums[i]] = i
