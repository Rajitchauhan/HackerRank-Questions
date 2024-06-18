# Input: nums = [-1,0,1,2,-1,-4]
# Output: [[-1,-1,2],[-1,0,1]]
# Explanation: 
# nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
# nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
# nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
# The distinct triplets are [-1,0,1] and [-1,-1,2].


 nums = [-1,0,1,2,-1,-4]
#  nums.sort()
#  sorted(nums)
nums= [-4 , -1 , -1 , 0 , 1 , 2]
        a    i                j
            

            
            
            
            
            
            
            
            
            
            
nums= [-4 ,-1 , -1 ,  -1 , -1 , 0 , 1 , 2 , 2 ]
            a          i                j
            
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        nums.sort()
        res = []
        for a in range(n-2):
            
            if a==0 or ( a>0 and nums[a] != nums[a-1]):
                i , j =  a+1 , n-1
                while i < j:
                    curr = []
                    sum = nums[a] + nums[i] + nums[j]
                    if sum == 0:
                        curr.append(nums[a])
                        curr.append(nums[i])
                        curr.append(nums[j])

                        res.append(curr)

                        i += 1
                        j -= 1

                        # avoid duplicate

                        while i < j and nums[i] == nums[i-1]:
                            i += 1

                        while i <j and nums[j] == nums[j+1]:
                            j -= 1
                    elif sum > 0:
                        j -= 1
                    else:
                        i += 1
        return res
