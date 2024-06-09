# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]

class Solution:
    # if array is not sorted
    # a + b = tar 
    # tar - a = b
    def twoSum(self , nums , target):
        dt = {}
        for i in range(len(nums)):
            if target - nums[i] in dt :
                return [dt[target-nums[i]] , i]
            dt[nums[i]] = i
        return [-1  ,-1]
    
    if array is sorted
    def twoSum(self , nums , target):
        n = len(nums)
        i , j = 0 , n-1
        while(i<j):
            add = nums[i] + nums[j]
            if add == target:
                return [i , j]
            elif(add < target):
                i += 1
            else:
                j -= 1
        return [-1  , -1]
    bruite force O(n^2)
    def twoSum(self , nums , target):   
        n = len(nums)
        for i in range(n):
            for j in range(i+1  , n):
                if nums[i]+nums[j] == target:
                    return [i , j]
                

if __name__ == "__main__":
    nums = list(map(int , input().split()))
    target = int(input())
    obj = Solution()
    res = obj.twoSum(nums , target)
    print(res)
    
    
 # geeksforgeeks version slighty change   
class Solution:
    def Countpair (self, arr, n, sum) : 
        i , j = 0 , n-1
        count = 0
    
        while(i<j):
            add = arr[i] + arr[j]
            if add == sum:
               
                count += 1
                i += 1
                j -= 1
            elif add < sum:
                i += 1
            else:
                j -= 1
        return -1 if count == 0 else count