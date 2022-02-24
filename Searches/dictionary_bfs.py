''' Breadth first search implementation on a dictionary
    Time Complexity: O(V+E)
    Space Complexity: O(V)
    Applications:
        - Finds the best solution for shortest path
        - Slower than DFS
        - Cycle detection in undirected graph
'''

if __name__ == '__main__':

    graph = {
        5: [3, 7],
        3: [2, 4],
        7: [8],
        2: [],
        4: [8],
        8: [1],
        1: [9],
        9: []
    }

    visited = []
    queue = []

    def bfs(visited, graph, node):
        visited.append(node)
        queue.append(node)

        while queue:
            s = queue.pop(0)
            print(s, end=" ")

            for x in graph[s]:
                if x not in visited:
                    visited.append(x)
                    queue.append(x)

    bfs(visited, graph, 5)
