import math
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

V = int(input())

parent = [ i for i in range(V+1)]
stars = []
edges = []
result = 0

for _ in range(V):
  x, y = map(float,input().split())
  stars.append((x,y))

for i in range(V-1):
  for j in range(i+1,V):
    edges.append((math.sqrt((stars[i][0] - stars[j][0])**2 + (stars[i][1] - stars[j][1]) ** 2),i,j))
  
edges.sort()
for edge in edges:
  cost, a, b = edge
  if find_parent(a) != find_parent(b):
    union_find(a,b)
    result += cost
print(round(result,2))