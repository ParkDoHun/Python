Python 3.7.4 (tags/v3.7.4:e09359112e, Jul  8 2019, 19:29:22) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> # 제어문과 데이터 타입 조합
>>> squares = []
>>> for x in range(10):			# 0~9까지 반복문 수행
	squares.append(x**2)		# 숫자의 제곱수를 리스트에 추가

	
>>> squares
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
>>> # 대괄호에 반복문 작성
>>> new_squares = [x**2 for x in range(10)]	# for문과 함께 리스트 선언
>>> new_squares
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
>>> # 제어문 조합
>>> squares = []
>>> for X in range(10):
	squares.append(X**2)

	
>>> new_squares = [X**2 for X in range(10)]
>>> 
>>> # 예시
>>> A = ['blue', 'yellow', 'red']
>>> B = ['red', 'green', 'blue']
>>> pairs = []
>>> for a in A:
	for b in B:
		if a != b:
			pairs.append((a, b))	# 서로 다른 쌍 추가

			
>>> pairs
[('blue', 'red'), ('blue', 'green'), ('yellow', 'red'), ('yellow', 'green'), ('yellow', 'blue'), ('red', 'green'), ('red', 'blue')]
>>> 
>>> new_pairs = [(a, b) for a in A for b in B if a!=b]
>>> new_pairs
[('blue', 'red'), ('blue', 'green'), ('yellow', 'red'), ('yellow', 'green'), ('yellow', 'blue'), ('red', 'green'), ('red', 'blue')]
>>> 
>>> # 리스트 생성 시 대괄호 안에서 튜플을 사용하면 반드시 소괄호로 감싼다.
>>> [x, x**2 for x in range(6)]		# 튜플 소괄호 누락 예시
SyntaxError: invalid syntax
>>> [(x, x**2) for x in range(6)]	# 튜플 소괄호 적용 예시
[(0, 0), (1, 1), (2, 4), (3, 9), (4, 16), (5, 25)]
>>> 
>>> # 세트 타입 만들기
>>> a = {x for x in 'abracadabra' if x not in 'abc'}	# 세트 생성
>>> a
{'r', 'd'}
>>> # (a, b, c 제거)
>>> 
>>> # 딕셔너리 타입 만들기
>>> square_dic = {x: x**2 for x in (2, 4, 6)}		# 딕셔너리 생성
>>> square_dic
{2: 4, 4: 16, 6: 36}
>>> 
>>> 
>>> # 색인과 항목 함께 보여주기
>>> # 리스트 이용
>>> korean_foods = ['kimchi', 'bibimbab', 'tteok-bokki']	# 리스트 생성
>>> korean_foods[0]		# 색인 0의 항목 추출
'kimchi'
>>> 
>>> # 항목 값을 색인과 함께 출력
>>> index = 0 				# 색인을 위한 index 변수 생성 및 초기화
>>> for food in korean_foods:		# 리스트 순회
	print(index, food)		# 색인, 리스트 항목  출력
	index += 1 			# 색인 1 증가

	
0 kimchi
1 bibimbab
2 tteok-bokki
>>> 

>>> # enumerate()를 이용한 색인, 항목 보여주기
>>> korean_foods_enum = enumerate(korean_foods)	# enumerate 생성
>>> type(korean_foods_enum)
<class 'enumerate'>
>>> 
>>> for index, food in korean_foods_enum:	# enumerate 순회
	print(index, food)

	
0 kimchi
1 bibimbab
2 tteok-bokki
>>> # 추가로 만든 index 변수가 for문 안으로 들어가서 소스코드가 깔끔해졌다.
>>> # 그에 따라 컴퓨터의 자원(CPU, 메모리)을 덜 쓰는 구조가 되었다.
>>> 
