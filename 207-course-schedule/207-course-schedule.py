class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        def count_parents(graph):
            counts = { node: 0 for node in graph }
            for parent in graph:
                for node in graph[parent]:
                    counts[node] += 1
            return counts
        # topological sort based on Kahn's algorithm
        def top_sort(graph):
            res = 0
            queue = deque()
            counts = count_parents(graph)
            for nodes in counts:
                if counts[nodes] == 0:
                    queue.append(nodes)
            while len(queue) > 0:
                node = queue.popleft()
                res += 1
                for child in graph[node]:
                    counts[child] -= 1
                    if counts[child] == 0:
                        queue.append(child)
            return (res == numCourses)

        # first create graph from the prerequisites list of list
        graph = {num: [] for num in range(0,numCourses)}
        for a,b in prerequisites:
            # b comes before a so make adjacency list of all of the children following the pre-req
            graph[b].append(a)
        return top_sort(graph)

        