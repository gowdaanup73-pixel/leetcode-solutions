# from collections import Counter
# class Solution:
#     def minimumPushes(self, word: str) -> int:
#         freq = Counter(word)
#         counts = sorted(freq.values(), reverse=True)
#         total = 0
#         for i, f in enumerate(counts):
#             total += f * ((i // 8) + 1)
#         return total


#The simplest one 
class Solution:
    def minimumPushes(self, word: str) -> int:
        n = len(word)
        full_groups = n // 8
        remainder = n % 8
        total = sum(8 * (k + 1) for k in range(full_groups))
        total += remainder * (full_groups + 1)
        return total