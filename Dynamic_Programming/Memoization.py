# 메모이제이션 : 이전에 계산된 결과를 일시적으로 기록해 놓는 넓은 개념 ( 하향식 방식 )
# 메모이제이션은 다이나믹 프로그래밍을 구현하는 방법 중 하나.
# 한 번 꼐산한 결과를 메모리 공간에 메모하는 기법
# 값을 기록해 놓는다는 점에서 캐싱(Caching)이라고도 한다.

# 피보나치 수열 : 탑다운 다이나믹 프로그래밍 소스코드
# 피보나치 함수(Fibonacci Function)을 재귀함수로 구현
def fibo(x):
    if x == 1 or x == 2:
        return 1
    return fibo(x -1) + fibo(x-2)

print(fibo(100))


d = [0] * 100       # 한 번 계산된 결과를 메모이제이션(Memoization)하기 위한 리스트 초기화


# # 피보나치 함수(Fibonacci Function)를 재귀 함수로 구현 ( 탑다운 다이나믹 프로그래밍 )
# def fibo(x) :
#     # 종료 조건 ( 1혹은 2일 때, 1을 반환)
#     if x == 1 or x == 2 :
#         return 1
#     # 이미 계산한 적 있는 문제라면 그대로 반환
#     if d[x] != 0:
#         return d[x]
#     # 아직 계산하지 않은 문제라면 점화식에 따라서 피보나치 결과 반환
#     d[x] = fibo(x-1) + fibo(x-2)
#     return d[x]
#
# print(fibo(99))

# # 피보나치 함수(Fibonacci Function) 보텀업 다이나믹 프로그래밍
#
# d = [0] * 100
#
# d[1] = 1
# d[2] = 1
# n = 99
#
# for i in range(3, n+1) :
#     d[i] = d[i-1] + d[i-2]
#
#
# print(d[n]) 
