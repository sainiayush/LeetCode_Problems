class TimeMap:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.dictionary = collections.defaultdict(list)
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.dictionary[key].append([timestamp, value])

    def get(self, key: str, timestamp: int) -> str:
        arr = self.dictionary[key]
        n = len(arr)
        left, right = 0,n
        
        while left<right:
            mid = left+(right-left)//2
            if arr[mid][0]>timestamp:
                right = mid
            else:
                left = mid+1
        return "" if right==0 else arr[right-1][1]


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
