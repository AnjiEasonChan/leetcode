import math

class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        ans = dividend / divisor if dividend / divisor < 2147483648 else 2147483647
        return math.ceil(ans) if ans < 0 else math.floor(ans)
