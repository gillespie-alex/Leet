class Solution:
    def findAnagrams(self, original: str, check: str) -> List[int]:
        original_len, check_len = len(original), len(check)
        if original_len < check_len:
            return []

        ans = []
        # stores the frequency of each character in the check string
        check_cnt = [ 0 ] * 26
        # stores the frequency of each character in the current window
        window = [ 0 ] * 26
        a = ord('a')  # ascii value of 'a'
        # first window
        for i in range(check_len):
            #this fills our base dictionary
            check_cnt[ord(check[i]) - a] += 1
            window[ord(original[i]) - a] += 1
        if check_cnt == window:
            ans.append(0)
        
        #sliding window
        #window moves from i to i + check_len
        for i in range(1, original_len - check_len + 1):
            #clear the first element of previous window
            window[ord(original[i - 1]) - a] -= 1
            #add new element to the window
            window[ord(original[i + (check_len - 1)]) - a] += 1
            if check_cnt == window:
                ans.append(i)
        return ans
