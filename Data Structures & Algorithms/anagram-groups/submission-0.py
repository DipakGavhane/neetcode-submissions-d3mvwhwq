class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        map = {}

        for i in strs:
            sorted_i = "".join(sorted(i))

            if sorted_i in map:
                ## yes
                map[sorted_i].append(i)

            else:
                ## No
                map[sorted_i] = [i]

        result = [i for i in map.values()]
        return result
        
