class Solution:
    def helper(self, sub_word: str) -> bool:
        return sub_word == sub_word[::-1]
    def partition(self, s: str) -> List[List[str]]:
        res = []
        def backtrack(start_index, current_list):
            if start_index == len(s):
                res.append(current_list.copy())
                return
            new = s[start_index:]
            for i in range(len(new)):
                if self.helper(new[0 : i+1]):
                    current_list.append(new[0 : i+1])
                    backtrack(start_index + i + 1, current_list)
                    current_list.pop()
        backtrack(0,[])
        return res
            