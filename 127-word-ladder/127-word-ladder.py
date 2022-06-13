class Solution:
    def ladderLength(self, begin: str, end: str, word_list: List[str]) -> int:
        # use a helper function to find all possible combinations of 4 letter words and each letter
        # and see if that letter is included in our set and if so, then it is a valid neighbor
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
