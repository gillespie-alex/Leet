class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        # first step is to sort the envelopes in with increasing width and decreasing height
        
        dolls = sorted(envelopes, key = lambda x: [x[0],-x[1]])
        res = []
        res.append(dolls[0][1])
        for i, (_, h) in enumerate(dolls):
            if i == 0 or dolls[i][1] == res[-1]:
                continue
            else:
                bin_search = bisect_left(res, h)
                if bin_search > len(res) - 1:
                    res.append(dolls[i][1])
                else:
                    res[bin_search] = dolls[i][1]
        return len(res)