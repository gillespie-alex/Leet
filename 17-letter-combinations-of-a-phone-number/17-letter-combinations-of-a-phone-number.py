class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        #base case
        if not digits:
            return
        #first create hash map of all phone numbers and letters
        dial = {'2':'abc', '3':'def', '4':'ghi', '5':'jkl', '6':'mno', '7':'pqrs', '8':'tuv', '9':'wxyz'}
        def backtrack(combination,res):
            if len(combination) == len(digits):
                res.append(''.join(combination))
                return
            #the length of the current combination tells us which digit to use next
            next_digit = digits[len(combination)]
            for letter in dial[next_digit]:
                combination.append(letter)
                backtrack(combination,res)
                combination.pop()
        res = []
        backtrack([],res)
        return res
                
                
