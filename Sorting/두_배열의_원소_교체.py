
# 배열 A와 B를 가지고, N개의 원소로 구성되었다.
# Q. N, K, 배열A, 배열B의 정보가 주어졌을 때, 최대 K번의 바꿔치기 연산을 수행하여 만들 수 있는 배열 A의 모든 원소의 합의 최댓값을 출력하는 프로그램을 작성하라.

# 핵심 아이디어 : 매번 배열 A에서 가장 작은 원소를 골라서, 배열 B에서 가장 큰 원소와 교체한다.

n, k = map(int, input().split())        # N과 K를 입력 받기
a = list(map(int, input().split()))     # 배열 A의 모든 원소를 입력 받기
b = list(map(int, input().split()))     # 배열 B의 모든 원소를 입력 받기

a.sort()                # 배열 A는 오름차순 정렬 수행
b.sort(reverse=True)    # 배열 B는 내림차순 정렬 수행

# 첫 번째 인덱스부터 확인하며, 두 배열의 원소를 최대 K번 비교
for i in range(k) :
    # A의 원소가 B의 원소보다 작은 경우
    if a[i] < b[i] :
        # 두 원소를 교체
        a[i], b[i] = b[i], a[i]
    else :      # A의 원소가 B의 원소보다 크거나 같을 때, 반복문을 탈출
        break

print(sum(a))