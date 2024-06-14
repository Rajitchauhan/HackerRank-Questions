# Sample Input

# 5 4(times rotate)
# 1 2 3 4 5
# Sample Output
# 5 1 2 3 4
#explaination 
# {
    # [1,2,3,4,5]
#     [2,3,4,5,1]
#     [3,4,5,1,2]
#     [4,5,1,2,3]
#     [5,1,2,3,4]
    
#  }
class Solution:
    def leftRot(self, nums, rotate):
        n = len(nums)
        # Normalize the number of rotations
        rotate = rotate % n
        # Perform rotations
        for _ in range(rotate):
            first_element = nums[0]
            for j in range(1, n):
                nums[j-1] = nums[j]
            nums[n-1] = first_element
        return nums

if __name__ == '__main__':
    n = list(map(int, input().split()))
    n1, n2 = n[0], n[1]
    nums = list(map(int, input().split()))
    obj = Solution()
    lt = obj.leftRot(nums, n2)
    print(' '.join(map(str, lt)))
