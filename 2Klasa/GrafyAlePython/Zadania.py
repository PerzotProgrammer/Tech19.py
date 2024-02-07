def SumaWierzcholkow(graph: {}) -> int:
    suma = 0
    for v in graph:
        suma += len(graph[v])
    return suma


def SumaKrawedzi(graph: {}) -> int:
    suma = SumaWierzcholkow(graph)
    return suma // 2


def MaxKrawedzi(graph: {}) -> int:
    maxVal = 0
    for key, values in graph.items():
        for value in values:
            if value > maxVal:
                maxVal = value
    return maxVal


def DFS(graph: {}, node: int, visited=None) -> []:
    if visited == None:
        visited = []

    if node not in visited:
        visited.append(node)
        for neighbour in graph[node]:
            DFS(graph, neighbour, visited)
    return visited
