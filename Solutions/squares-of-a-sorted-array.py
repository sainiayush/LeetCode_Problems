class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        output = collections.deque()
        l,r = 0,len(nums) - 1
        while l<=r:
            left = abs(nums[l])
            right = abs(nums[r])
            if left>right:
                output.appendleft(left*left)
                l += 1
            else:
                output.appendleft(right*right)
                r -= 1
        return output
            
