# HTTP 메서드
# GET    :   특정한 데이터의 조회를 요청한다.     ; 특정페이지 접속, 정보 검색
# POST   :   특정한 데이터의 생성을 요청한다.     ; 회원가입, 글쓰기
# PUT    :   특정한 데이터의 수정을 요청한다.     ; 회원 정보 수정
# DELETE :  특정한 데이터의 삭제를 요청한다.      ; 회원 정보 삭제

# import requests
#
# target = 'http://google.com'
# response = requests.get(url=target)
# print(response.text)

# API(Application Programming Interface) : 프로그램이 상호작용하기 위한 인터페이스를 의미한다.
# REST API : REST 아키텍처를 따르는 API
# REST API 호출 : REST 방식을 따르고 있는 서버에 특정한 요청을 전송하는 것.

# JSON(JavaScript Object Notation) : 데이터를 주고받는 데 사용하는 경량의 데이터 형식 ; 키와 값의 쌍으로 이루어진 데이터 객첵를 저장한다.

import json

# 사전 자료형(dict) 데이터 선언
user = {
    "id" : "eunseong",
    "password" : "lee",
    "age" : 26,
    "hobby" : ['football', 'programming']
}
print(user)
# 파이썬 변수를 JSON 객체로 변환
json_data = json.dumps(user, indent= 4)
print(json_data)

# JSON 데이터로 변환하여 파일로 저장
with open('user.json', 'w', encoding='utf-8') as file :      # w : 쓰기 권한
    json_data = json.dump(user, file, indent= 4)


# 목킹(Mocking) : 어떠한 기능이 있는 것처럼 흉내내어 구현한 것을 의미한다.
# REST API 연습 사이트 : http://jsonplaceholder.typicode.com/