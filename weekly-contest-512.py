class Solution:
    def largestInteger(self, n: int, s: int) -> int:
        if s == 0:
            return 0
        if s > 9 * n:
            return -1
    
        digits = []
        remaining = s
        for _ in range(n):
            if remaining <= 0:
                break
        d = min(9, remaining)
        digits.append(d)
        remaining -= d
    
        return int(''.join(map(str, digits)))
        