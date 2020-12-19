def countAndSay(self, n: int) -> str:
    if n == 1:
        return '1'
    s = self.countAndSay(n-1)
    
    i, res = 0, ''
    for j, c in enumerate(s):
        if c != s[i]:
            res += str(j-i) + s[i]
            i = j
    res += str(len(s) - i) + s[-1]  # 最后一个元素莫忘统计
    return res
