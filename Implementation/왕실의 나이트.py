# 행복 왕국의 왕실 정원은 체스판과 같은 8 x 8 좌표 평면입니다. 왕실 정원의 특정한 한 칸에 나이트가 서있습니다.
# 나이트는 말을 타고 있기 때문에 이동을 할 때는 L자 형태로만 이동할 수 있으며 정원 밖으로는 나갈 수 없습니다.
# 나이트는 특정 위치에서 다음과 같은 2가지 경우로 이동할 수 있습니다.
# 1. 수평으로 두 칸 이동한 뒤에 수직으로 한 칸 이동하기 / 2. 수직으로 두 칸 이동한 뒤에 수평으로 한 칸 이동하기

# Q. 8 X 8 좌표 평면상에서 나이트의 위치가 주어졌을 때 나이트가 이동할 수 있는 경우의 수를 출력하는 프로그램을 작성하세요.
# 단, 행 위치를 표현할 때는 1부터 8로 표현하며, 열 위치를 표현할 때는 a부터 h로 표현합니다.

import time

# 현재 나이트의 위치 입력받기
input_data = input()
start_time = time.time()
row = int(input_data[1])
column = int(ord(input_data[0])) - int(ord('a')) + 1

# 나이트가 이동할 수 있는 8가지 방향 정의
steps = [(-2,-1), (-1,-2), (1,-2), (2,-1), (2,1), (1,2), (-1,2), (-2,1)]

# 8가지 방향에 대하여 각 위치로 이동이 가능한지 확인
result = 0
for step in steps :
    # 이동하고자 하는 위치 확인
    next_row = row + step[0]
    next_column = column + step[1]
    # 해당 위치로 이동이 가능하다면 카운트 증가
    if next_row >= 1 and next_row <= 8 and next_column >= 1 and next_column <= 8 :
        result += 1

print(result)

end_time = time.time()
print("수행 시간 : ", end_time - start_time)