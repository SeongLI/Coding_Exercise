# 듣고자 하는 N개의 강의 정보가 주어졌을 때, N개의 강의에 대하여 수강하기까지 걸리는 최소 시간을 각각 출력하는 프로그램을 작성하라.
# 이 문제는 위상 정렬 알고리즘의 응용문제이다. 각 노드(강의)에 대하여 인접한 노드를 확인할 때, 인접한 노드에 대하여 현재보다 강의 시간이 더 긴 경우를 찾는다면,
# 더 오랜 시간이 걸리는 경우의 시간 값을 저장하는 방식으로 결과 테이블을 갱신하여 답을 구할 수 있다.
# 따라서 위상 정렬을 수행하면서, 매번 간선 정보를 확인하여 결과 테이블을 갱신한다.

from collections import deque
import copy

# 노드의 개수 입력받기
v = int(input())
# 모든 노드에 대한 진입차수는 0으로 초기화
indegree = [0] * ( v +1 )
# 각 노드에 연결된 간선 정보를 담기 위한 연결 리스트(그래프) 초기화
graph = [[] for i in range( v + 1 )]
# 각 강의 시간을 0으로 초기화
time = [0] * ( v + 1 )

# 방향 그래프의 모든 간선 정보를 입력받기
for i in range(1, v + 1) :
    data = list(map(int, input().split()))
    time[i] = data[0] # 첫 번째 수는 시간 정보를 담고 있음
    for x in data[1:-1]:
        indegree[i] += 1
        graph[x].append(i)

# 위상 정렬 함수
def topology_sort() :
    result = copy.deepcopy(time)    # 알고리즘 수행 결과를 담을 리스트
    q = deque()     # 큐 기능을 위한 deque 라이브러리 사용

    # 처음 시작할 때는 진입차수가 0인 노드를 큐에 삽입
    for i in range(1, v+1) :
        if indegree[i] == 0 :
            q.append(i)

    # 큐가 빌 때까지 반복
    while q :
        # 큐에서 원소 꺼내기
        now = q.popleft()
        # 해당 원소와 연결된 노드들의 진입차수에서 1 빼기
        for i in graph[now] :
            result[i] = max(result[i], result[now] + time[i])
            indegree[i] -= 1
            # 새롭게 진입차수가 0이 되는 노드를 큐에 삽입
            if indegree[i] == 0 :
                q.append(i)

        # 위상 정렬을 수행한 결과 출력
        for i in range(1, v+1) :
            print(result[i])

topology_sort()
