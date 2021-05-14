class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        output = [[1]]
        for i in range(1,rowIndex+1):
            output += [list(map(lambda x,y:x+y, output[-1]+[0], [0]+output[-1]))]
        return output[-1]
