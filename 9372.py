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

T = int(input())
for i in range(T):
  edges = []
  result = 0
  n, m = map(int,input().split())
  parent = [i for i in range(n+1)]
  for j in range(m):
    a, b = map(int,input().split())
    edges.append((a,b))
  edges.sort()
  for edge in edges:
    a,b = edge
    if find_parent(a) != find_parent(b):
      union_find(a,b)
      result += 1
  print(result)
