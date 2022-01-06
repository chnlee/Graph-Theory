import sys
sys.setrecursionlimit(10**5)
input = sys.stdin.readline

# def find_parent(x):
#   if parent[x] != x:
#     return find_parent(parent[x])
#   return x

def find_parent(x):
  if parent[x] != x:
    parent[x] = find_parent(parent[x])
  return parent[x]

def union_find(a,b):
  a = find_parent(a)
  b = find_parent(b)
  if a < b:
    parent[b] = a
  else:
    parent[a] = b

n, m = map(int,input().split())
parent = [ i for i in range(n+1)]

for _ in range(m):
  cost, a, b = map(int,input().split())
  if cost == 0:
    union_find(a,b)
  else:
    if find_parent(a) != find_parent(b):
      print("NO")
    else: 
      print("YES")


  
