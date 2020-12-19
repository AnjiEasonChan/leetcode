class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        n = len(nums)
        begin = 0
        end = n-1
        while begin <= end:
            mid = (begin + end) // 2
            if nums[mid] > target:
                end = mid - 1
            elif nums[mid] < target:
                begin = mid + 1
            else:
                return mid
        return begin
