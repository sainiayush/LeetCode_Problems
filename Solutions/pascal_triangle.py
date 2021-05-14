class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        
        output = [[1]]
        for i in range(1,numRows):
            output += [list(map(lambda x,y:x+y, output[-1]+[0], [0]+output[-1]))]
        return output
                
