class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        val_index = []

        for num in nums:
            if num == val:
                val_index.append(num)

        for i in val_index:
            nums.remove(i)

        return len(nums)
        