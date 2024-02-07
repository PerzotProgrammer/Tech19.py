import RandomGraph as rg
import Zadania as zd

# rg.StumilowyLas()

# n, m = map(int, input().split())
graph = rg.MakeGraph(10, 10)
print(graph)
print()
print()
print(f"Suma wierzchołków: {zd.SumaWierzcholkow(graph)}")
print(f"Suma krawędzi: {zd.SumaKrawedzi(graph)}")
print(f"Max krawędzi: {zd.MaxKrawedzi(graph)}")
print()
print("DFS")

dfs = zd.DFS(graph, 0)

for node in dfs:
    print(f"{node} -> ", end="")
print("None")
