class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        # check length
        if len(nums) <= 1:
            return nums

        # setting pivot
        pivot = nums[len(nums) // 2]
        
        # sorting
        left = [x for x in nums if x < pivot]
        middle = [x for x in nums if x == pivot]
        right = [x for x in nums if x > pivot]

        return self.sortArray(left) + middle + self.sortArray(right)