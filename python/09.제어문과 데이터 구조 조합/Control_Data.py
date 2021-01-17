Python 3.7.4 (tags/v3.7.4:e09359112e, Jul  8 2019, 19:29:22) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> # 데이터 정렬
>>> nums = 4, 2, 5, 7, 1, 3 			# 숫자로 이루어진 튜플 생
>>> sorted(nums)				# 튜플 항목들을 오름차순으로 정렬
[1, 2, 3, 4, 5, 7]
>>> sorted(nums, reverse = True)		# 튜플 항목들을 내림차순으로 정렬
[7, 5, 4, 3, 2, 1]
>>> nums
(4, 2, 5, 7, 1, 3)
>>> # sorted 함수를 사용해 인수에 연속 데이터가 있는 데이터 구조 타입만 포함되면 무조건 정렬
>>> # reverse는 역으로 정렬하는 것이며, 기본값은 False다
>>> 
>>> programmer_dict = {'Python':5, 'C':2, 'C++':3, 'Java':4, 'Ruby':1}
>>> sorred(programmer_dict.keys())		# 키 정렬하여 리스트로 반환하기
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    sorred(programmer_dict.keys())		# 키 정렬하여 리스트로 반환하기
NameError: name 'sorred' is not defined
>>> sorted(programmer_dict.kry())		# 키 정렬하여 리스트로 반환하기
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    sorted(programmer_dict.kry())		# 키 정렬하여 리스트로 반환하기
AttributeError: 'dict' object has no attribute 'kry'
>>> sorted(programmer_dict.keys())		# 키 정렬하여 리스트로 반환하기
['C', 'C++', 'Java', 'Python', 'Ruby']
>>> sorted(programmer_dict.keys(), reverse = True)	# 역순 정렬
['Ruby', 'Python', 'Java', 'C++', 'C']
>>> 
>>> # 열거 데이터 반환 : range() 함수
>>> nums = 0, 1, 2, 3, 4 			# 숫자 0~4를 열거한 튜플
>>> for num in nums:				# 튜플 순회
	print(num)

0
1
2
3
4
>>> 
>>> for num in range(5)				# range()함수를 사용한 for문
SyntaxError: invalid syntax
>>> for num in range(5):			# range()함수를 사용한 for문
	print(num)

	
0
1
2
3
4
>>> # range함수가 숫가 0~5보다 작은 4까지의 숫자를 1씩 증가시켜 반환하는 것
>>> 
>>> for num in range(1, 6):			# 1이상 6미만의 숫자 순회
	print(num)				# 각 항목 숫자 출력

	
1
2
3
4
5
>>> for num in range(2, 11, 2):			# 10 이하 짝수 출력
	print(num)

	
2
4
6
8
10
>>> 
>>> for num in range(1, 11, 2):			# 10 이하 홀수 출력
	print(num)

	
1
3
5
7
9
>>> # range함수를 활용하면, 순차적으로 증가하는 숫자 타입 리스트를 만들 수 있으며 for문과 조합하여 여러 용도로 사용 가능
>>> 
>>> # 색인을 만 앞에 출력
>>> langs = 'python', 'java', 'C++'			# 세 가지 프로그래밍 언어를 튜플로 저장
>>> for index in range(len(langs)):			# range()함수로 langs 길이만큼 선회
	print(index, langs[index])			# 튜플 색인 및 값 출력

	
0 python
1 java
2 C++
>>> 
