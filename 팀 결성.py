def parent_find(parent, x):
  if parent[x] != x:
    parent[x] = parent_find(parent,parent[x])
  return parent[x]

def union_find(parent,a,b):
  a = parent_find(parent, a)
  b = parent_find(parent, b)

  if a<b :
    parent[b] = a
  else:
    parent[a] = b

n, m = map(int,input().split())

parent = [i for i in range(n+1)]

for i in range(m):
  cost, a, b = map(int,input().split())
  if cost == 0:
    union_find(parent,a,b)
  else:
    if parent_find(parent,a) != parent_find(parent,b):
      print("NO")
    else:
      print("YES")
