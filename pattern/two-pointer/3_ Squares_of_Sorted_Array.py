# Given an integer array nums sorted in non-decreasing order, return an array of the squares of each number sorted in non-decreasing order.
 
# Example 1:
# Input: nums = [-4,-1,0,3,10]
# Output: [0,1,9,16,100]
# Explanation: After squaring, the array becomes [16,1,0,9,100].
# After sorting, it becomes [0,1,9,16,100].


# Example 2:
# Input: nums = [-7,-3,2,3,11]
# Output: [4,9,9,49,121]



# Input: nums = [-4,-1,0,3,10]
#               [16,1,0,9.100]
# Output: [0,1,9,16,100]
#         idx
# temp = [0 , 1 , 9 , 16 , 100]
# nums = [-4 ,-1, 0 , 3, 10]
#                 ij

# n = len(nums)

# # temp = []
# # for i in range(n):
# #     temp.append(0)

# temp = [0 for i in range(n)]

# i = 0
# j = n-1
# idx = j     

# while (i <= j):
#     if abs(nums[i]) > abs(nums[j]):
#         temp[idx] = nums[i] * nums[i]
#         i += 1
#         idx -= 1
#     else:
#         temp[idx] = nums[j] * nums[j]
#         j -= 1
#         idx -= 1
# return temp



class Solution:
    def sortedSquares(self, nums):
        arr = [0 for i in range(len(nums))]
        i , j = 0 , len(nums)-1 
        idx = j

        while i<=j:
            if abs(nums[i]) > abs(nums[j]):
                arr[idx] = nums[i] * nums[i]
                i += 1
                #idx -= 1
            else:
                arr[idx] = nums[j] * nums[j]
                j -= 1
                #idx -= 1
            idx -= 1
        return arr
    
lt =[-4,-1,0,3,10]
obj = Solution()
res = obj.sortedSquares(lt)
print(res)
