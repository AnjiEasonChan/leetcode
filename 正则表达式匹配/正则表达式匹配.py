class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        if not p: return not s  # 结束条件

        first_match = (len(s) > 0) and p[0] in {s[0], '.'}
        # 先处理 `*`
        if len(p) >=2 and p[1] == '*':
            # 匹配0个 | 多个
            return self.isMatch(s, p[2:]) or (first_match and self.isMatch(s[1:], p))
        
        # 处理 `.` ，匹配一个
        return first_match and self.isMatch(s[1:], p[1:])


