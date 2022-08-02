# '재귀 함수를 호출'이라는 문자열을 무한히 출력한다.
# 어느 정도 출력하다가 최대 재귀 깊이 초과 메시지가 출력된다.
# RecursionError: maximum recursion depth exceeded while calling a Python object

# def recursive_function():
#     print('재귀 함수를 호출')
#     recursive_function()
#
# recursive_function()


# 재귀 함수를 문제 풀이에서 사용할 때는 재귀 함수의 종료 조건을 반드시 명시해야 한다.

def recursive_function(i):
    # 100번째 호출을 했을 때 종료되도록 종료 조건 명시
    if i == 100 :
        return
    print(i, '번째 재귀함수에서', i+1, '번째 재귀함수를 호출합니다.')
    recursive_function(i+1)
    print(i, '번째 재귀함수를 종료합니다.')

recursive_function(1)