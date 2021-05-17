class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        
        n = len(arr)
        zeros_count = arr.count(0)
        total = n+zeros_count
        
        i = n - 1
        j = total - 1
        
        while j>=0:
            if j<n:arr[j]=arr[i]
            j -= 1
            if arr[i] == 0:
                if j<n:arr[j]=arr[i]
                j-=1
            i-=1
