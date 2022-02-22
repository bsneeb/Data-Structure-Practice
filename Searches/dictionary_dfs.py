''' Depth first search implementation on a dictionary
    Time Complexity: O(V+E)
    Space Complexity: O(V)
    Applications:
        - Finds the path quickly
        - Can find strongly connected components of a graph
        - Detects cycles in a graph
        - Not the optimal solution like BFS
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

    visited = set()

    def dfs(visited, graph, node):
        ''' Traverses all nodes until found them all. '''
        if node not in visited:
            print(f"Node: {node}")
            visited.add(node)
            for x in graph[node]:
                dfs(visited, graph, x)

    dfs(visited, graph, 5)
