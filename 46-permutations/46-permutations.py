class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        #create boolean array to hold used values, could also use set or hash map for this
        visit = [False] * len(nums)
        res = []
        permutations = []
        def backtrack(res,subset):
            if len(subset) == len(nums):
                #append to make a list of lists
                res.append(subset)
            
            for i, vals in enumerate(nums):
                if not visit[i]:
                    visit[i] = True
                    #concatenate the list to our subset list
                    backtrack(res, subset + [vals])
                    visit[i] = False
                    
        backtrack(res,permutations)
        return res