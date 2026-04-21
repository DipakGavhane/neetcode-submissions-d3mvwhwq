class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # Step 1: Sort list
        strs.sort()

        # Step 2: Compare first and last item
        first = strs[0]
        last = strs[-1]
        prefix = ""

        for i in range(min(len(first), len(last))):
            if first[i] != last[i]:
                break
            prefix += first[i]
            
        
        # Step 3: Return common chars
        return prefix