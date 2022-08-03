class Solution:
    def findReplaceString(self, S: str, indices: List[int], sources: List[str], targets: List[str]) -> str:
        # put everything in hashmap before and then do the checking so when the indices are
        # unsorted you can still access them in order, just use the indices as keys mapped to sources
        lookup = {i: (src, tgt) for i, src, tgt in zip(indices, sources, targets)}
        i, result = 0, []
        while i < len(S):
            if i in lookup and S[i:].startswith(lookup[i][0]):
                result.append(lookup[i][1])
                i += len(lookup[i][0])
            else:
                result.append(S[i])
                i += 1
        return "".join(result)