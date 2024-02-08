class Solution:
    def solution(self, s):
        arr = [1, 3, 2]
        reps = [0, 0, 0]
        for letter in s:
            if letter == "B":
                reps[0] += 1
            if letter == "A":
                reps[1] += 1
            if letter == "N":
                reps[2] += 1
        count = 0
        while True:
            for i, v in enumerate(reps):
                reps[i] = reps[i] - arr[i]
                if reps[i] < 0:
                    return count
            count += 1

        
print(Solution().solution("QABAAAWOBL"))