''' This file includes an implementation of an adjacency list 
    to practice Graph representation. 
    Adjacency List representation of a graph. 
        Space Complexity:
            Average Case: O(V+E)
            Worst case: O(V^2)
        Pros:
            - Helps find all the vertices adjacent to a vertex easily
            - Less space than 2D matrix
            - Faster when graphs have less number of edges (No storing empty 0's in 2D matrix if mostly empty)
        Cons: 
            - Slower than matrix due to exploring all connected nodes first'''


class adjNode:
    ''' Node of adjacency list '''

    def __init__(self, value):
        self.vertex = value
        self.next = None


class Graph:

    def __init__(self, num):
        self.v = num
        self.graph = [None] * self.v

    def add_edge(self, s, d):
        ''' Add an edge to the adjlist '''
        node = adjNode(d)
        node.next = self.graph[s]
        self.graph[s] = node

        node = adjNode(d)
        node.next = self.graph[d]
        self.graph[d] = node

    def print_graph(self):
        ''' Print the adjacency list'''
        for i in range(self.v):
            print(f"Vertex {str(i)}:", end="")
            temp = self.graph[i]
            while temp:
                print(" -> {}".format(temp.vertex), end="")
                temp = temp.next
            print("\n")

    def num_nodes(self):
        print(f"There are {self.v} vertices in this list.")


if __name__ == '__main__':

    v = 6
    graph = Graph(v)
    graph.add_edge(0, 1)
    graph.add_edge(0, 2)
    graph.add_edge(0, 3)
    graph.add_edge(1, 2)
    graph.add_edge(2, 3)
    graph.add_edge(2, 5)
    graph.add_edge(2, 3)
    graph.add_edge(3, 5)
    graph.add_edge(4, 1)

    graph.print_graph()
