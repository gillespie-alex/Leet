class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        # hash map holding all the prefix sums, the key will hold the sum while
        # the value holds the number of prefix_sum instances of this key exist
        prefix_sums = {0 : 1}
        arr_sum = 0
        res = 0
        for elements in nums:
            arr_sum += elements
            
            # this is the hardest part of solution to problem
            # The key observation is that the the sum of a subarray [i, j] is equal to the sum of [0, j] minus the sum of [0, i - 1].
            
            if (arr_sum - k) in prefix_sums.keys():
                res += prefix_sums.get(arr_sum - k)
            
            #must add the default '0' argument in .get() method if this key in the hash table is empty
            prefix_sums[arr_sum] = 1 + prefix_sums.get(arr_sum, 0)
        return res