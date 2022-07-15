class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry = 1
        ptr = len(digits) - 1
        while carry:
            if digits[ptr] == 9 and ptr == 0:
                # corner case where input is [9] for example
                digits[ptr] = 0
                return [1] + digits
            elif digits[ptr] == 9:
                digits[ptr] = 0
                ptr -= 1
            else:
                digits[ptr] += 1
                carry = 0
        return digits
        