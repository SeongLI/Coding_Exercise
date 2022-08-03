from bisect import bisect_left, bisect_right

# 값이 [left_value, right_value]인 데이터의 개수를 반환하는 함수
def count_by_range(a, left_value, right_value) :
    right_index = bisect_right(a, right_value)
    left_index = bisect_left(a, left_value)
    return right_index - left_index

# # 배열 선언
# a = [1, 2, 3, 3, 3, 3, 4, 4, 4, 8, 9]

print("전체 원소 입력하세요")
a = list(map(int, input().split()))

print("개수를 알고싶은 정수를 입력하세요.")
n = int(input())

if count_by_range(a, n, n) == 0:
    print('값이 존재하지 않습니다.')
else:
    print("값이", n, "인 데이터 개수 =", count_by_range(a, n, n))

print( "값이 [-1, 3] 범위에 있는 데이터 개수 =", count_by_range(a, -1, 3))
