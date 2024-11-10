class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        nums.sort()

        i,j = 0,len(nums)-1

        while i < j and nums[j] > 0:
            if -nums[i] == nums[j]:
                return nums[j]
            if -nums[i] > nums[j]:
                i += 1
            else:
                j -= 1
        return -1
