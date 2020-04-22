class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        #         string_list = [k for k in s]

        #         long_string = []
        #         len_string = 0
        #         for i,each in enumerate(string_list):
        #             if each in long_string:
        #                 index = long_string.index(each)
        #                 del long_string[:index+1]
        #                 long_string.append(each)
        #             else:
        #                 long_string.append(each)
        #             len_string = max(len_string,len(long_string))
        store = {}
        max_length = init = 0

        for i, each in enumerate(s):
            if each in store and init <= store[each]:
                init = store[each] + 1
            else:
                max_length = max(max_length, i - init + 1)
            store[each] = i

        return max_length
