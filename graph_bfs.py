edges = [(0, 1), (0, 4), (1, 4), (1, 2), (1, 3), (2, 3), (3, 4)]
edges2 = [(0, 1), (0, 3), (1, 2), (2, 3), (4, 5), (4, 6), (5, 6), (7, 8)]
num_of_nodes = 9


class Graphs:
    def __init__(self, num_nodes, edges):
        self.nodes = num_nodes
        self.data = [[] for _ in range(num_nodes)]
        for n1, n2 in edges:
            self.data[n1].append(n2)
            self.data[n2].append(n1)

    def __repr__(self):
        return "\n".join(['{}: {}'.format(n, neighbours) for n, neighbours in enumerate(self.data)])

    def __str__(self):
        return self.__repr__()


graph = Graphs(num_nodes=7, edges=edges)
print(graph.__str__())


# Breadth first search
def bfs(graph, root):
    queue = []
    discovered = [False] * len(graph.data)
    distance = [None] * len(graph.data)

    discovered[root] = True
    distance[root] = 0
    queue.append(root)
    idx = 0

    while idx < len(queue):
        current = queue[idx]
        idx += 1
        for node in graph.data[current]:
            if not discovered[node]:
                distance[node] = 1 + distance[current]
                discovered[node] = True
                queue.append(node)

    return queue, distance


print(bfs(graph, 3))