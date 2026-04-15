import random

class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        # quicksort
        def quicksort(left, right):
            if left >= right:
                return
            
            pivot_index = random.randint(left, right)
            nums[pivot_index], nums[right] = nums[right], nums[pivot_index]

            pivot = nums[right]
            i = left

            for j in range(left, right):
                if nums[j] < pivot:
                    nums[i], nums[j] = nums[j], nums[i]
                    i += 1
            
            nums[i], nums[right] = nums[right], nums[i]

            quicksort(left, i-1)
            quicksort(i+1, right)
                
        quicksort(0, len(nums)-1)
        return nums



