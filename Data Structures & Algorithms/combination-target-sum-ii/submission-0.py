class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:

        res, sub_sets = [], []
        candidates.sort()


        def dfs(i, curr, sub_set):

            if curr == target:
                res.append(sub_set.copy())

            for j in range(i, len(candidates)):

                if j > i and candidates[j] == candidates[j - 1]:
                    continue
                
                if curr + candidates[j] > target:
                    break
                
                sub_set.append(candidates[j])
                dfs(j + 1, curr + candidates[j], sub_set)
                sub_set.pop()
        
        dfs(0, 0,[])
        return res

        