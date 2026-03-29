class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        window = set()
        for i in range(len(nums)):
            # check duplicates
            if nums[i] in window:
                return True

            # add element
            window.add(nums[i])

            # check window < k
            if len(window) > k:
                window.remove(nums[i-k])
        return False
                