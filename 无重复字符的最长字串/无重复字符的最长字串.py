class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        start = 0
        dict={}
        max = 0
        for i in range(len(s)):
            if s[i] not in dict:
                dict[s[i]] = i
            else:
                if dict[s[i]] + 1 > start:
                    start = dict[s[i]] + 1
                dict[s[i]] = i
            if i - start + 1 > max:
                    max = i - start + 1
        return max
