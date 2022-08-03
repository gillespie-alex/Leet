class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        running_sum = 0
        max_base = len(columnTitle) - 1
        for letter in columnTitle:
            val = ord(letter) - 64
            running_sum += ((26 ** max_base) * val)
            max_base -= 1
        return running_sum