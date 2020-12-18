class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        index = 0
        for i in range(len(nums)-1, 0, -1):
            if nums[i] > nums[i-1]:
                index = i
                break
        if index == len(nums)-1:
            nums[index], nums[index-1] = nums[index-1], nums[index]
        elif index == 0:
            self.Reverse(nums, 0, len(nums)-1)
        else:
            self.Reverse(nums, index, len(nums)-1)
            for s in range(index, len(nums)):
                if nums[s] > nums[index-1]:
                    nums[index-1], nums[s] = nums[s], nums[index-1]
                    break
    def Reverse(self, nums, start, end):
        mid = (start+end+1) // 2
        k = 0
        for j in range(start, mid):
            nums[j], nums[end-k] = nums[end-k], nums[j]
            k += 1

