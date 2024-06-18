# Input: nums = [3,2,2,3], val = 3
# Output: 2, nums = [2,2,_,_]

# Input: nums = [0,1,2,2,3,0,4,2], val = 2
# Output: 5, nums = [0,1,4,0,3,_,_,_]


# 2 != 2
# count += 1 -> 5

class Solution:
    def removeElement(self, nums, val):
        n = len(nums)
        m = nums.count(val)
        return (n-m)
    
    def removeElement(self, nums, val):
        dup = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[dup] = nums[i]
                dup += 1
        return dup