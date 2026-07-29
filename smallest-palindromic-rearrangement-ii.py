from collections import Counter
from math import factorial

class Solution:
    def smallestPalindrome(self, s: str, k: int) -> str:
        freq = Counter(s)
        odd_chars = [c for c, v in freq.items() if v % 2 == 1]
        mid = odd_chars[0] if odd_chars else ''

        half_counts = {c: v // 2 for c, v in freq.items() if v // 2 > 0}
        half_len = sum(half_counts.values())
        chars_sorted = sorted(half_counts.keys())

        total = factorial(half_len)
        for v in half_counts.values():
            total //= factorial(v)

        if k > total:
            return ""
        k -= 1  
        counts = dict(half_counts)
        remaining = half_len
        result = []

        for _ in range(half_len):
            for c in chars_sorted:
                v = counts.get(c, 0)
                if v == 0:
                    continue
                trial = total * v // remaining
                if k < trial:
                    result.append(c)
                    counts[c] -= 1
                    remaining -= 1
                    total = trial
                    break
                else:
                    k -= trial

        half_str = ''.join(result)
        return half_str + mid + half_str[::-1]