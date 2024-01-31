import RandomGraph as rg
from random import randint

# rg.StumilowyLas()

# n, m = map(int, input().split())
graph = rg.MakeGraph(10, 10)
print(graph)

print()
print()

M = [[randint(0, 9) for i in range(10)] for j in range(10)]

for i in M:
    print(i)
