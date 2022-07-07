class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        # if not fruits:
        #     return 0
        # # this question essentially boils down to the longest contiguous sub-array  
        # l,r = 0,0
        # baskets = {}
        # Max = 0
        # while r < len(fruits):
        #     if fruits[r] not in baskets:
        #         baskets[fruits[r]] = 1
        #     else:
        #         baskets[fruits[r]] += 1
        #     while len(baskets) > 2:
        #         baskets[fruits[l]] -= 1
        #         if baskets[fruits[l]] == 0:
        #             del baskets[fruits[l]]
        #         l += 1
        #     r += 1
        #     Max = max(Max, len(fruits[l:r+1]))
        # return Max
        count, i = {}, 0
        for j, v in enumerate(fruits):
            count[v] = count.get(v, 0) + 1
            if len(count) > 2:
                count[fruits[i]] -= 1
                if count[fruits[i]] == 0: del count[fruits[i]]
                i += 1
        return j - i + 1