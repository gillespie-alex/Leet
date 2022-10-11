class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n == 0: return False
        return True if not (n & (n - 1)) else False
    
    
    
    

        