class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        size = len(nums)
        f = [0]*size
        for i in range(size):
            f[i] = max(f[i-1]+nums[i],nums[i]) if i else nums[0]
        return max(f)
