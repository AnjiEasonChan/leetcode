class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n = len(nums)
        if n <= 1: return n
        # i慢 j快
        i, j = 0, 1
        for inx in range(n - 1):
            if nums[i] == nums[j]:
                j += 1
                continue
            else:
                i += 1
                nums[i] = nums[j]
                j += 1
        nums = nums[0:i + 1]
        return len(nums)

