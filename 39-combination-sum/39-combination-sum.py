class Solution:
    
    # this helper function determines if the prosective candidate will exceed the target value when added to the current path
    # this helps prune the state space tree
    def helper(self, current_list: List[int], prospect: int, target: int) -> bool:
        if prospect + sum(current_list) > target:
            return False
        return True
    
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        def backtrack(current: List[int], i_start:int):
            if sum(current) == target:
                # now check if this combination is already in our result
                current_copy = current.copy()
                current_copy.sort()
                if current_copy not in res:
                    res.append(current_copy)
                return
            
            # we don't backtrack to previous indices as those have already been explored in the state space tree
            # this essentially "prunes" the state space tree and prevents duplicates from being searched
            for j in range(i_start, len(candidates)):
                if self.helper(current, candidates[j], target):
                    current.append(candidates[j])
                    backtrack(current,j)
                    current.pop()
        backtrack([],0)
        return res