# i/p : rajit
# o/p : tijar

#with out slicing and in-buuld function
# s = [1 ,2 ,3 , 4]
# st = []
# for i in range(len(s)-1 , -1 , -1):
#     # st += s[i]
#     st.append(s[i])
# print(st)
    
# idx : 0 1  2  3  4    
# lt : 50 40 30 20 10
#             ij
            
# def reverse(st):
#     n = len(st)
#     i , j = 0 , (n-1)
#     # st = st.split()
#     st = list(st)
#     while(i<j):
#         st[i] , st[j] = st[j] , st[i]
#         i += 1
#         j -= 1
#     return " ".join(st)
    

# res = reverse("rajit")
# print(res)   

# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
# You can return the answer in any order.
 
# Example 1:
# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]

# 0 1 2 3 4  5
# 1 2 4 7 11 15  -> 15
#     i    j    

class Solution:
    def twoSum(self, nums, target):
        n = len(nums)
        i , j =0 , (n-1)
        while(i < j):
            add = nums[i] + nums[j]
            if add == target:
                return [i , j]
            elif add > target:
                j -= 1
            else:
                i += 1
        return [-1 , -1]