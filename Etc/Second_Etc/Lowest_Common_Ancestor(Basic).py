# 최소 공통 조상(LCA) : 두 노드의 공통된 조상 중에서 가장 가까운 조상을 찾는 문제
# 1. 모든 노드에 대한 깊이를 계산한다.
# 2. 최소 공통 조상을 찾을 두 노드를 확인한다.
#   1) 먼저 두 노드의 깊이가 동일하도록 거슬러 올라간다.
#   2) 이후에 부모가 같아질 때까지 반복적으로 두 노드의 부모 방향으로 거슬러 올라간다.
# 3. 모든 LCA(a,b) 연산에 대하여 2번의 과정을 반복한다.

import sys
sys.setrecursionlimit(int(1e5))     # 런타임 오류를 피하기
n = int(input())

parent = [0] * (n+1)    # 부모 노드 정보
d = [0] * ( n + 1 )     # 각 노드까지의 깊이
c = [0] * ( n + 1 )     # 각 노드의 깊이가 계산되었는지 여부
graph = [[] for _ in range(n + 1)]  # 그래프(graph)정보

for _ in range(n - 1) :
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

# 루트 노드부터 시작하여 깊이(depth)를 구하는 함수
def dfs(x, depth) :
    c[x] = True
    d[x] = depth
    for y in graph[x]:
        if c[y] :   # 이미 깊이를 구했다면 넘기기
            continue
        parent[y] = x
        dfs(y, depth + 1)

# A와 B의 최소 공통 조상을 찾는 함수
def lca(a, b):
    # 먼저 깊이(depth)가 동일하도록
    while d[a] != d[b]:
        if d[a] > d[b] :
            a = parent[a]
        else:
            b = parent[b]
    # 노드가 같아지도록
    while a != b :
        a = parent[a]
        b = parent[b]
    return a

dfs(1, 0)   # 루트 노드는 1번 노드

m = int(input())

for i in range(m):
    a, b = map(int, input().split())
    print(lca(a,b))


