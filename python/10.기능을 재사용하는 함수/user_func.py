Python 3.7.4 (tags/v3.7.4:e09359112e, Jul  8 2019, 19:29:22) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> # 사용자 지정 함수 만들기
>>> def hello():				# 함수 선언
	name = input('이름을 입력하세요! ')	# 이름 입력
	print('안녕하세요!', name)		# 이름 출력

	
>>> hello()					# 함수 호출
이름을 입력하세요! 박도훈
안녕하세요! 박도훈
>>> 
>>> # 2개의 숫자를 인수로 넣어 합한 값을 표준 출력하는 예시
>>> def sum(a, b)	# 인수 2개인 함수 선언
SyntaxError: invalid syntax
>>> def sum(a, b):	# 인수 2개인 함수 선언
	print(a+b)	# 인수 2개를 더한 값 출력

	
>>> sum(1, 4)		# 함수 실행
5
>>> sum(7, 3)
10
>>> 
>>> # 반환 값 추가하기
>>> my_name = input('이름을 입력하세요! ')		# 이름 입력
이름을 입력하세요! 안나
>>> hello(my_name)
Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    hello(my_name)
TypeError: hello() takes 0 positional arguments but 1 was given
>>> # 반환 값 추가하기
>>> 
======= RESTART: C:/Users/bee64/Desktop/10.기능을 재사용하는 함수/user_func1.py =======
이름을 입력하세요! 박도훈
>>> hello(my_name)
Traceback (most recent call last):
  File "<pyshell#19>", line 1, in <module>
    hello(my_name)
NameError: name 'hello' is not defined
>>> # 반환 값 추가하기
>>> def chang_name(name):		# 함수 선언
	return name + '님'		# '님'을 뒤에 붙여서 반환

>>> change_name('도훈')
Traceback (most recent call last):
  File "<pyshell#24>", line 1, in <module>
    change_name('도훈')
NameError: name 'change_name' is not defined
>>> 
======= RESTART: C:/Users/bee64/Desktop/10.기능을 재사용하는 함수/user_func1.py =======
이름을 입력하세요! 박도훈
Traceback (most recent call last):
  File "C:/Users/bee64/Desktop/10.기능을 재사용하는 함수/user_func1.py", line 9, in <module>
    change_name('도훈')
NameError: name 'change_name' is not defined
>>> 
======= RESTART: C:/Users/bee64/Desktop/10.기능을 재사용하는 함수/user_func1.py =======
Traceback (most recent call last):
  File "C:/Users/bee64/Desktop/10.기능을 재사용하는 함수/user_func1.py", line 4, in <module>
    my_name = input('이름을 입력하세요! ', name)		# 이름 입력
NameError: name 'name' is not defined
>>> def change_name(name):
	return name + '님'

>>> change_name('도훈')
'도훈님'
>>> 
>>> # 변수의 유효 범위 정하기
>>> def my_func(param):			# 함수 정의, 매개 변수 param
	param = '함수 내부에서 생성' 	# param 값 변경(실은 지역 변수 생성)
	print(param)

	
>>> param = '함수 밖에서 생성'		# 외부 param 변수 생성 및 초기화
>>> my_func(param)
함수 내부에서 생성
>>> print(param)
함수 밖에서 생성
>>> 
>>> 
>>> # 전역 변수
>>> del param				# 기존 param 변수 삭제
>>> def my_func():			# 함수 정의, 매개 변수 없음
	global param 			# 전역 변수 param 호출
	param = '함수 내부에서 변경'	# param 값 변경
	print(param)

	
>>> param = '함수 밖에서 생성'		# 외부 param 변수 생성 및 초기화
>>> my_func()
함수 내부에서 변경
>>> print(param)
함수 내부에서 변경
>>> 
