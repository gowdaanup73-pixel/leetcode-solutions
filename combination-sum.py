class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        def dfs(index,target,path):
            if target == 0:
                ans.append(path[:])
                return
            if target < 0:
                return
            if index == len(candidates):
                return
            path.append(candidates[index])
            dfs(index,target - candidates[index],path)

            path.pop()
            dfs(index + 1,target,path)
        dfs(0,target,[])
        return ans