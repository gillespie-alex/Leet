class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        if "0000" in deadends:
            return -1
        def get_combos(combo):
            next_combos = []
            for i in range(4):
                temp = (int(combo[i])+1) % 10
                next_combos.append(combo[:i] + str(temp) + combo[i+1:])
                temp = (int(combo[i])- 1 + 10) % 10
                next_combos.append(combo[:i] + str(temp) + combo[i+1:])
            return next_combos
        queue = deque(["0000"])
        visited = set(deadends)
        attempts = 0
        while len(queue) > 0:
            for i in range(len(queue)):
                lock = queue.popleft()
                if lock == target:
                    return attempts
                for children in get_combos(lock):
                    if children in visited:
                        continue
                    queue.append(children)
                    visited.add(children)
            attempts += 1
        return -1

            