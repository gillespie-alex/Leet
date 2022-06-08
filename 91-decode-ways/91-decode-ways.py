class Solution:
    def numDecodings(self, s: str) -> int:
        # first we create a list of all the decodings
        encoded = [str(i) for i in range(1,27)]
        # then a hash map for memoization
        memo = {}
        def backtrack(start_index):
            # first check if the given start index is in the hash map
            if start_index in memo:
                return memo[start_index]
            
            if start_index == len(s):
                return 1
            
            # variable to hold all the possible encoded combos at this given index
            combos = 0
            for vals in encoded:
                if s[start_index:].startswith(vals):
                    combos += backtrack(start_index + len(vals))
            # add the new number of combos to the hash map for the given start_index
            memo[start_index] = combos
            return combos
        return backtrack(0)