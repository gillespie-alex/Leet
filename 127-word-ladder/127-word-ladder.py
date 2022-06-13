class Solution:
    def ladderLength(self, begin: str, end: str, word_list: List[str]) -> int:
        # # need a helper function to see if the string is allowed
        # # could just use a hash of the previous word vs the new word 
        # def get_neighbors(word):
        #     res = []
        #     for i in range(len(word)):
        #         for letter in string.ascii_letters[0:26]:
        #             next_word = word[:i] + letter + word[i+1:]
        #             if next_word in word_list:
        #                 res.append(next_word)
        #     return res
        # def BFS(word):
        #     counter = 1
        #     queue = deque([word])
        #     # this visited set only needs to include the 'begin' word
        #     visited = set([word])
        #     while len(queue) > 0:
        #         for i in range(len(queue)):
        #             new = queue.popleft()
        #             if new == end:
        #                 return counter
        #             for neighbor in get_neighbors(new):
        #                 if neighbor in visited:
        #                     continue
        #                 queue.append(neighbor)
        #                 visited.add(neighbor)
        #         counter += 1
        #     return 0 
        # return BFS(begin)
        words = set(word_list) # make a set because existence query is O(1) vs O(N) for list
        queue = deque([begin])
        distance = 1
        while len(queue) > 0:
            n = len(queue)
            distance += 1
            for _ in range(n):
                word = queue.popleft()
                for i in range(len(word)):
                    for c in ascii_letters:
                        next_word = word[:i] + c + word[i + 1:]
                        if next_word not in words:
                            continue
                        if next_word == end:
                            return distance
                        queue.append(next_word)
                        words.remove(next_word) # removing from the set is equivalent as marking the word visited
        return 0
