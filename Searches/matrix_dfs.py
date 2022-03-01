''' Depth first search implementation on a 2d Matrix
    Time Complexity: O(V+E)
    Space Complexity: O(V)
    Applications:
        - Finds the path quickly
        - Can find strongly connected components of a graph
        - Detects cycles in a graph
        - Not the optimal solution like BFS
'''


def dfs(row, col, grid):

    stack = []
    stack.append([row,col])

    while len(stack) > 0:
        



if __name__ == '__main__':

    grid = [ [0, 0, 1],
             [0, 0, 1],
             [1, 0, 0] ]

    dfs(0, 0, grid)