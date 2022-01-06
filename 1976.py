# exit()함수를 알고, 구현 방식을 어떻게 하면 효율적인지 다시한번 생각해볼 수 있게 하는 문제.

#      0 1 2
#  0
#  1
#  2
 
#  인 경우 0,1 0,2 1,2 만 확인 하면 되므로
#  for i in range(n):
# 	 for j in range(i,n):만 작성하면 된다.
# 그리고 경로 상의 1개만 parent노드를 찾고
# 그 노드와 나머지 경로 상의 값들을 비교하면 된다.


import sys
sys.setrecursionlimit(10**5)
input = sys.stdin.readline

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

n = int(input())
m = int(input())
parent = [i for i in range(n+1)]
graph = [list(map(int,input().split())) for i in range(n)]
routh = list(map(int,input().split()))

for i in range(n):
  for j in range(i,n):
    if graph[i][j] == 1:
      union_find(i+1,j+1)

prnt = find_parent(routh[0])

for a in range(m):
  if find_parent(routh[a]) != prnt:
    print("NO")
    exit()

print("YES")

