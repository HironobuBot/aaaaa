class Solution:
    def solution(self, s):
        Xreq = 0
        Oreq = 0
        for round in s:
            if round == "X":
                Xreq += 1
                if Oreq < 3:
                    Oreq = 0
            if round == "O":
                Oreq += 1
                if Xreq < 3:
                    Xreq = 0
        if Xreq >= 3 and Oreq < 3:
            return "X"
        if Xreq < 3 and Oreq >= 3:
            return "O"
        return "tie"
        
print(Solution().solution("XXOOOOOXX"))