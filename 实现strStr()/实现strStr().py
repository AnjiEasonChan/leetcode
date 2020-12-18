class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        # if not needle:return 0
        # n,l = len(haystack),len(needle)
        # for start in range(n-l+1):
        #     if haystack[start] != needle[0]:
        #         continue
        #     if haystack[start:start+l]==needle:
        #         return start
        # return -1

        # return haystack.find(needle)
        
        L, n = len(needle), len(haystack)
        
        if L == 0:
            return 0
        
        start = 0
        
        while start < n - L + 1:
            curr_len = 0
            while curr_len < L and haystack[start] == needle[curr_len]:
                start += 1
                curr_len += 1
            if curr_len == L:
                return start - L
            start = start - curr_len + 1
        return -1
