class Solution:
    def calPoints(self, operations: List[str]) -> int:
        ans = []
        for i in range(len(operations)):
            if operations[i] == "D":
                next_score = ans[-1] * 2
                ans.append(next_score)
            elif operations[i] == "C":
                ans.pop()
            elif operations[i] == "+":
                next_score = ans[-1] + ans[-2]
                ans.append(next_score)
            else:
                next_score = int(operations[i])
                ans.append(next_score)
        return sum(ans)
        
        