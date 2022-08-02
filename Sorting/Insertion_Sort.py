# 삽입 정렬 : 처리되지 않은 데이터를 하나씩 골라 적절한 위치에 삽입한다.

array = [7,5,9,0,3,1,6,2,4,8]

for i in range(1, len(array)) :
    for j in range(i, 0, -1) :
        if array[j] < array[j - 1] :
            array[j], array[j - 1] = array[j - 1], array[j]     #스왚
        else :  # 자기보다 작은 데이터를 만나면 그 위치에서 멈춤
            break
print(array)

# 삽입 정렬의 시간 복잡도, 빅오 표기법 : O( N^2 )
# 현재 리스트의 데이터가 거의 정렬되어 있는 상태라면 매우 빠르게 동작한다.
