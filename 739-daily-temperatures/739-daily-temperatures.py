class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # for this problem we will use a monotonic decreasing stack
        dec_stack = []
        output = [0]*len(temperatures)
        for i, temp in enumerate(temperatures):
            if dec_stack:
                _, deg = dec_stack[-1]
                while dec_stack and deg < temp:
                    index, _ = dec_stack.pop()
                    output[index] = i - index
                    if dec_stack: _, deg = dec_stack[-1]
            dec_stack.append((i,temp))
        return output