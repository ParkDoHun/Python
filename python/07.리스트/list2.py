Python 3.9.1 (tags/v3.9.1:1e5d33e, Dec  7 2020, 17:08:21) [MSC v.1927 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> a = [1, 2]		# a 리스트 생성
>>> b = [3, 4]		# b 리스트 생성
>>> c = a + b 		# c 리스트 생성
>>> a
[1, 2]
>>> b
[3, 4]
>>> c
[1, 2, 3, 4]
>>> 
>>> a.extend(b)		# a 리스트 확장
>>> a
[1, 2, 3, 4]
>>> # 위의 c 리스트 같은 새로운 리스트를 생성할 필요가 없는 상황이면, a리스트를 확장하는 것이 메모리를 효율적으로 사용하는 방법 중 하나입니다.
>>> ㅁ
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    ㅁ
NameError: name 'ᄆ' is not defined
>>> a
[1, 2, 3, 4]
>>> del a[0]		# 리스트 첫 번째 값 삭제
>>> a
[2, 3, 4]
>>> del a[:]		# 리스트 전체 값 삭제(빈 리스트 만들기)
>>> a
[]
>>> # 리스트가 더 이상 사용되지 않는다면, 변수 자체를 삭제할 수도 있습니다.
>>> del a 		# 변수 삭제
>>> a
Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    a
NameError: name 'a' is not defined
>>> 
>>> matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]		# 2차원 행렬 선언
>>> matrix
[[1, 2, 3], [4, 5, 6], [7, 8, 9]]
>>> matrix[0]						# matrix 첫 번째 항목 값 확인
[1, 2, 3]
>>> matrix[1]						# matrix 두 번째 항목 값 확인
[4, 5, 6]
>>> matrix[1][1]					# matrix 두 번째 항목의 두 번째 값 확인
5
>>> matrix[2][2]					# matrix 세 번째 항목의 세 번째 값 확인
9
>>> 
>>> # 빈 리스트 만들기
>>> dice = [1, 2, 3, 4, 5, 6]			# 리스트 생성
>>> type(dice)					# dice 변수 타입 확인
<class 'list'>
>>> empty_list = []				# 빈 리스트 생성
>>> empty_list
[]
>>> type(empty_list)
<class 'list'>
>>> 
>>> # 기본 내장 함수 list()를 이용해 빈 리스트 생성
>>> empty_list2 = list()			# 빈 리스트 생성
>>> empty_list2
[]
>>> type(empty_list2)
<class 'list'>
>>> 