class Solution:
    def solution(self, s, c):
        cost = 0
        i = 0
        while i < len(s) - 1:
            arr = [c[i]]
            for j in range(i + 1, len(s)):
                if s[i] == s[j]:
                    arr.append(c[j])
                    continue
                break
            i = j - 1
            if len(arr) > 1:
                arr.remove(max(arr))
                for item in arr:
                    cost += item
            i += 1
        return cost
        
print(Solution().solution("abccbd", [0, 1, 2, 3, 4, 5, 6]))