class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        card = {}

        for i in nums:
            card[i] = card.get(i, 0) + 1

        major = 0
        major_n = 0
        for i, j in card.items():
            if j > major:
                major = j
                major_n = i
        return major_n

        