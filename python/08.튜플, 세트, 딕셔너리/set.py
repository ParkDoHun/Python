Python 3.7.4 (tags/v3.7.4:e09359112e, Jul  8 2019, 19:29:22) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> # 세트 타입 선언 및 사용하기
>>> languages = {'C++', 'Python', 'C', 'C++', 'Python'}		# 세트 생성
>>> languages
{'C++', 'Python', 'C'}
>>> 'Pytyon' in languages					# 항목 존재 유무 확인
False
>>> 'Python' in languages
True
>>> 
>>> # 빈 세트 타입은 반드시 set()함수를 사용해야 생성할 수 있다.
>>> try_empty_set = {}
>>> type(try_empty_set)
<class 'dict'>
>>> real_empty_set = set()		# 올바른 빈 세트 데이터 생성
>>> type(real_empty_set)
<class 'set'>
>>> 
>>> 
>>> # 집합
>>> 
>>> a = set('abracadabra')		# 세트 타입 변환을 통한 중복 문자 제거
>>> b = set('alacazam')
>>> a
{'d', 'a', 'c', 'b', 'r'}
>>> a - b 				# a에만 존재하는 문자(차집합)
{'d', 'b', 'r'}
>>> a | b 				# a와 b의 합집합
{'z', 'd', 'a', 'l', 'c', 'b', 'm', 'r'}
>>> a & b 				# a와 b의 교집합
{'c', 'a'}
>>> a ^ b 				# a와 b의 여집합(합집합 - 교집합)
{'z', 'm', 'd', 'l', 'b', 'r'}
>>> 
