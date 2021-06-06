class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        
        
        output = [-1,-1]
        
        output[0] = self.start_index(nums,target)
        output[1] = self.end_index(nums,target)
        
        return output 
    
    def start_index(self, nums,target):
        index = -1
        left,right = 0,len(nums)-1
        output =[-1,-1]
        while left<=right:
            mid = left+(right-left)//2

            if nums[mid]>target:
                right = mid-1
            elif nums[mid]<target:
                left = mid+1
            else:
                index = mid
                right = mid-1
        return index

    def end_index(self, nums,target):
        index = -1
        left,right = 0,len(nums)-1
        output =[-1,-1]
        while left<=right:
            mid = left+(right-left)//2

            if nums[mid]>target:
                right = mid-1
            elif nums[mid]<target:
                left = mid+1
            else:
                index = mid
                left = mid+1
        return index
