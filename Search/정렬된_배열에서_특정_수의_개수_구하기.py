# N개의 원소를 포함하고 있는 수열이 오름차순으로 정렬되어 있습니다. 이때 이 수열에서 x가 등장하는 횟수를 계산하세요.

# 시간 복잡도 O(logN)으로 동작하는 알고리즘을 요구하고 있다.
# 일반적인 선형 탐색(Linear Search)로는 시간 초과 판정을 받는다.
# 하지만 데이터가 정렬되어 있기 때문에 이진 탐색을 수행할 수 있다.

from bisect import bisect_right, bisect_left

# 값이 [left_value, right_value]인 데이터의 개수를 반환하는 함수
def count_by_range(array, left_value, right_value) :
    right_index = bisect_right(array, right_value)
    left_index = bisect_left(array, left_value)
    return right_index - left_index

n, x = map(int, input().split())            # 데이터의 개수 N, 찾고자 하는 값 X 입력받기
array = list(map(int, input().split()))     # 전체 데이터 입력받기

# 값이 [x,x] 범위에 있는 데이터의 개수 계산
count = count_by_range(array, x, x)

# 값이 x인 원소가 존재하지 않는다면
if count == 0 :
    print(-1)
# 값이 x인 원소가 존재한다면
else :
    print(count)

