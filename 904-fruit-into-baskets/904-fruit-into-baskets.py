class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        if not fruits:
            return 0
        # this question essentially boils down to the longest contiguous sub-array  
        l,r = 0,0
        baskets = {}
        Max = 1
        baskets[fruits[r]] = baskets.get(fruits[r], 0) + 1
        while r < len(fruits) - 1:
            r += 1
            baskets[fruits[r]] = baskets.get(fruits[r], 0) + 1
            while len(baskets) > 2:
                baskets[fruits[l]] -= 1
                if baskets[fruits[l]] == 0:
                    del baskets[fruits[l]]
                l += 1
            Max = max(Max, r - l + 1)
        return Max