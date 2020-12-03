class Solution:
    def reverse(self, x: int) -> int:
        s = str(x)
        if s[0] == '-':
            x = int('-' + s[1:][::-1])
        else:
            x = int(s[::-1])
        return x if -2147483648< x <2147483647 else 0
