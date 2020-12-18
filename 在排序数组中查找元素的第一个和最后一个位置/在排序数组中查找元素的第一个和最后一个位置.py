class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            if nums[i] == target:
                j = i + 1
                while j < len(nums) and nums[j] == target: j+=1
                return [i, j-1]
        return [-1, -1]
