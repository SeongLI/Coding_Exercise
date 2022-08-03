# 이진 탐색 : 정렬되어 있는 리스트에서 탐색 범위를 절반씩 좁혀가며 데이터를 탐색하는 방법
# 시작점, 끝점, 중간점을 이용하여 탐색 범위를 설정한다. ( 중간점 : 소수점 이하 제거 )
# 이진 탐색의 연산 횟수는 log2N에 비례 / 시간 복잡도는 O(logN)을 보장

# 이진 탐색 소스코드 ( 재귀 함수 )
def binary_serch(array, target, start, end) :
    if start > end :
        return None
    mid = (start + end) // 2
    # 찾은 경우 중간점 인덱스 반환
    if array[mid] == target :
        return mid
    # 중간점의 값보다 찾고자 하는 값이 작은 경우 왼쪽 확인
    elif array[mid] > target :
        return binary_serch(array, target, start, mid-1)
    else :
        return binary_serch(array, target, mid +1, end)

print("n(원소의 개수)과 target(찾고자 하는 값)을 입력하세요.")
n, target = list(map(int, input().split()))
print("전체 원소 입력하세요")
array = list(map(int, input().split()))

# 이진 탐색 수행 결과 출력
result = binary_serch(array, target, 0, n-1)
if result == None :
    print("원소가 존재하지 않습니다.")
else :
    print(result + 1)

# 중복 값이 존재한다면, 우선 발견된 인덱스를 출력