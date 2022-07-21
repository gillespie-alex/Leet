class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        # the hard part of this problem is realizing that taking a letter away from word2 is equivalent
        # to inserting that letter at the end of word1 and comparing the old word1 with the substring of
        # word2 excluding the letter that was inserted, apply this same form of logic for replacing and deleting
        dp = [[0 for _ in range(len(word2) + 1)] for _ in range(len(word1) + 1)]
        for row in range(len(dp)):
            for col in range(len(dp[row])):
                if row == 0:
                    dp[row][col] = col
                elif col == 0:
                    dp[row][col] = row
                # in all other cases we need to do some calculations
                elif word1[row-1] == word2[col-1]:
                    dp[row][col] = dp[row-1][col-1]
                else:
                    replace = dp[row-1][col-1]
                    delete = dp[row-1][col]
                    insert = dp[row][col-1]
                    dp[row][col] = 1 + min(replace, delete, insert)
        return dp[-1][-1]
        