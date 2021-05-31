class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
       
        columns = len(matrix[0])
        left, right = 0,len(matrix)*len(matrix[0])-1
        while left<=right:
            mid = (left+right)//2
            value = matrix[mid//columns][mid%columns]
            if target==value:
                return True
            elif target<value:
                right=mid-1
            else:
                left=mid+1
        return False
