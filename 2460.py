class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        res = []
        zeros = []
        for i in range(len(nums)-1):
            if nums[i] > 0:
                if nums[i] == nums[i+1]:
                    res.append(nums[i]*2)
                    nums[i+1] = 0
                else:
                    res.append(nums[i])
            else:
                zeros.append(0)
        if nums[-1] > 0:
            res.append(nums[-1])
        else:
            zeros.append(nums[-1])
        
        return res + zeros
