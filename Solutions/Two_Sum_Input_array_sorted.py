class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        # hashmap = {}
        # for i,each in enumerate(numbers):
        #     if target - each in hashmap:
        #         return [hashmap[target-each]+1,i+1]
        #     else:
        #         hashmap[each] = i
                
        left,right = 0,len(numbers) - 1
        
        while left<right:
            total = numbers[left] + numbers[right]
            if total == target:
                return [left+1, right+1]
            elif total < target:
                left += 1
            else:
                right -= 1