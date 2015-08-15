class Solution:
    # @param {integer[]} nums
    # @return {integer}
    def removeDuplicates(self, nums):
        i = 0
        for n in nums:
            if i < 2 or nums[i-2] < n:
                nums[i] = n
                i += 1
        return i 
                