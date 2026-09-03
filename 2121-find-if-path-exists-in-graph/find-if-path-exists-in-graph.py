class Solution:
    def validPath(self, n, edges, source, destination):
        graph = [[] for _ in range(n)]

        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)

        stack = [source]
        seen = {source}

        while stack:
            node = stack.pop()

            if node == destination:
                return True

            for nei in graph[node]:
                if nei not in seen:
                    seen.add(nei)
                    stack.append(nei)

        return False