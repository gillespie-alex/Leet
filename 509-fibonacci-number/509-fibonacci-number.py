class Solution:
    def fib(self, n: int) -> int:
        cache = {}
        def dfs(n):
            if n in cache:
                return cache[n]
            elif n == 0:
                return 0
            elif n == 1:
                return 1
            val = dfs(n-1) + dfs(n-2)
            cache[n] = val
            return val
        return dfs(n)
            
        