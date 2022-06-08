class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        memo = {}
        def backtrack(start_index):
            if start_index == len(s):
                return True
            if start_index in memo:
                return memo[start_index]
            current_path = False
            # this will cycle through and try every different permuation of the given wordDict to see if there is a valid path
            for words in wordDict:
                if words == s[start_index : start_index + len(words)]:
                    # if this is true we want to keep moving downt he state space tree
                    if backtrack(start_index + len(words)):
                        current_path = True
                        # now we can break out of the loop as this current path reaches the end
                        break
            memo[start_index] = current_path
            return current_path
        return backtrack(0)