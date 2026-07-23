class Solution:
    def combinationSum2(self, candidates, target):
        candidates.sort()
        ans = []
        path = []

        def dfs(start, target):
            if target == 0:
                ans.append(path[:])
                return

            if target < 0:
                return

            for i in range(start, len(candidates)):

                if i > start and candidates[i] == candidates[i-1]:
                    continue

                path.append(candidates[i])

                dfs(i + 1, target - candidates[i])

                path.pop()

        dfs(0, target)
        return ans