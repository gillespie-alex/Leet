class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        # if not fruits:
        #     return 0
        # # this question essentially boils down to the longest contiguous sub-array  
        # l,r = 0,0
        # baskets = set()
        # baskets.add(fruits[0])
        # Max = 1
        # while r < len(fruits) - 1:
        #     r += 1
        #     baskets.add(fruits[r])
        #     while len(baskets) > 2:
        #         prev = l
        #         l += 1
        #         if fruits[prev] in fruits[l:r]:
        #             continue
        #         else:
        #             baskets.remove(fruits[prev])
        #     Max = max(Max, r-l+1)
        #     #Max = max(Max, len(fruits[l:r+1]))
        # return Max
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
        # count, i = {}, 0
        # for j, v in enumerate(fruits):
        #     count[v] = count.get(v, 0) + 1
        #     if len(count) > 2:
        #         count[fruits[i]] -= 1
        #         if count[fruits[i]] == 0: del count[fruits[i]]
        #         i += 1
        # return j - i + 1