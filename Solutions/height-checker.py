from collections import Counter
class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        dict_heights = Counter(heights)
        number, output = 1,0
        for each in heights:
            while dict_heights[number]==0:
                number+=1
            if number!=each:
                output+=1
            dict_heights[number]-=1
        return output
        
            
