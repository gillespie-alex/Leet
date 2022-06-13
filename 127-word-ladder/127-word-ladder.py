class Solution:
    # def ladderLength(self, begin: str, end: str, word_list: List[str]) -> int:
    #     # need a helper function to see if the string is allowed
    #     # could just use a hash of the previous word vs the new word 
    #     def get_neighbors(word):
    #         res = []
    #         for i in range(len(word)):
    #             for letter in string.ascii_letters[0:26]:
    #                 next_word = word[:i] + letter + word[i+1:]
    #                 if next_word in word_list:
    #                     res.append(next_word)
    #         return res
    #     def BFS(word):
    #         counter = 1
    #         queue = deque([word])
    #         # this visited set only needs to include the 'begin' word
    #         visited = set([word])
    #         while len(queue) > 0:
    #             for i in range(len(queue)):
    #                 new = queue.popleft()
    #                 if new == end:
    #                     return counter
    #                 for neighbor in get_neighbors(new):
    #                     if neighbor in visited:
    #                         continue
    #                     queue.append(neighbor)
    #                     visited.add(neighbor)
    #             counter += 1
    #         return 0 
    #     return BFS(begin)
    
    def ladderLength(self, begin: str, end: str, word_list: List[str]) -> int:
        # need a helper function to see if the string is allowed
        # could just use a hash of the previous word vs the new word 
        def get_neighbors(word,visited):
            res = []
            for i in range(len(word)):
                for letter in string.ascii_letters[0:26]:
                    next_word = word[:i] + letter + word[i+1:]
                    if next_word in visited:
                        res.append(next_word)
            return res
        def BFS(word):
            counter = 1
            queue = [word]
            # this visited set only needs to include the 'begin' word
            visited = set(word_list)
            if word in visited: visited.remove(word)
            while len(queue) > 0:
                for i in range(len(queue)):
                    new = queue.pop(0)
                    if new == end:
                        return counter
                    for neighbor in get_neighbors(new,visited):
                        visited.remove(neighbor)
                        queue.append(neighbor)
                counter += 1
            return 0 
        return BFS(begin)
