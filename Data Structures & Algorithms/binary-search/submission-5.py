class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # find middle index
        mid = 0 + (len(nums)-1) // 2

        # moving to right
        if nums[mid] < target:
            while mid < len(nums):
                if nums[mid] == target:
                    return mid
                mid += 1
            return -1


        # moving to left
        else:
            while mid >= 0:
                if nums[mid] == target:
                    return mid
                mid -= 1
            return -1
        

