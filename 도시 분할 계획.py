# 도시 분할 계획

def parent_find(parent,x):
  if parent[x] != x:
    parent[x] = parent_find(parent,parent[x])
  return parent[x]

def union_find(parent,a,b):
  a = parent_find(parent,a)
  b = parent_find(parent,b)

  if a<b:
    parent[b] = a
  else:
    parent[a] = b

n,m = map(int,input().split())

parent = [i for i in range(n+1)]
edges = []
result = 0
last = 0
for i in range(m):
  a, b, cost = map(int,input().split())
  edges.append((cost,a,b))

edges.sort()

for edge in edges:
  a,b,cost = edge
  if parent_find(parent,a) != parent_find(parent,b):
    union_find(parent,a,b)
    result += cost
    last = cost

print(result - last)