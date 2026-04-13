class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        write = 0

        for read in range(1, len(nums)):
            if nums[read] == nums[write]:
                pass
            else:
                write += 1
                nums[write] = nums[read]

        return write+1

        
        