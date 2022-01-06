def find_parent(x):
  if parent[x] != x:
    parent[x] = find_parent(parent[x])
  return parent[x]

def union_find(a,b):
  a = find_parent(a)
  b = find_parent(b)

  if a<b:
    parent[b] = a
  else:
    parent[a] = b

V, E = map(int,input().split())

parent = [ i for i in range(V+1)]
edges = []
result = 0

for i in range(E):
  a, b, cost = map(int,input().split())
  edges.append((a,b,cost))
  
edges.sort()

for edge in edges:
  a,b, cost = edge
  if find_parent(a) != find_parent(b):
    union_find(a,b)
    result += cost

print(result)