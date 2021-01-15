Python 3.7.4 (tags/v3.7.4:e09359112e, Jul  8 2019, 19:29:22) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> text = '파이선 문자열'
>>> text[0]
'파'
>>> text[-1]
'열'
>>> # 문자열 비교
>>> 
>>> text[-1] = '다'
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    text[-1] = '다'
TypeError: 'str' object does not support item assignment
>>> # 문자열 객체는 항목 값을 바꿀 수 없다.
>>> # 객체 : 데이터 타입에 의해서 메모리에 생성된 실체
>>> 
>>> #튜플 타입 선언 및 사용하기
>>> card = 'red', 4, '다이아몬드', True		# 튜플 생성
>>> card
('red', 4, '다이아몬드', True)
>>> card[-1] = False				# 튜플 마지막 값 변경 시도
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    card[-1] = False				# 튜플 마지막 값 변경 시도
TypeError: 'tuple' object does not support item assignment
>>> 
>>> # 1행 : card 변수에 튜플을 생성하기 위해 항목 값들을 열거하여 대입
>>> 
>>> # 2~3행 : card 변수의 값을 확인해보니 소괄호 기호(())로 감싸여 있는 것을 확일 할 수 있습니다.
>>> 
>>> # 4행 : 마지막 항목의 값을 변경시도했지만, 앞서 살펴본 문자열 항목 변경 시도시 확인한 에러 메시지와 비슷한 메시지가 출력되는 것을 확인할 수 있습니다.
>>> 
>>> # 타입 에러 : 튜플 객체는 항목 값을 바꿀 수 없다.
>>> 
>>> 
>>> card[2]		# 세 번째 항목 값 확인
'다이아몬드'
>>> card[:2]		# 첫 ~ 두 번째 항목 자르기
('red', 4)
>>> card[2:]		# 세 번째 ~ 마지막 항목 자르기
('다이아몬드', True)
>>> card[:]		# 전체 튜플 복사
('red', 4, '다이아몬드', True)
>>> 
>>> 
>>> # 빈 튜플 만들기
>>> empty_tuple_1 = ()
>>> empty_tuple_1
()
>>> empty_tuple_2 = tuple()
>>> empty_tuple_2
()
>>> 
>>> # 하나의 항목이 있는 튜플 생성
>>> one = ('하나')		# 항목이 하나인 튜플 생성
>>> type(one)			# 타입 확인
<class 'str'>
>>> one
'하나'
>>> one_item = '하나',		# 항목이 하나인 튜플을 올바르게 생성
>>> type(one_item)		# 타입 확인(튜플)
<class 'tuple'>
>>> one_item
('하나',)
>>> 

>>> card
('red', 4, '다이아몬드', True)
>>> # 언패킹
>>> a, b, c, d = card		# 튜플 항목 개별 할당(언패킹)
>>> a
'red'
>>> b
4
>>> c
'다이아몬드'
>>> d
True
>>> 
>>> 
a, b, c = card			# 변수 개수가 적은 경우
Traceback (most recent call last):
  File "<pyshell#51>", line 2, in <module>
    a, b, c = card			# 변수 개수가 적은 경우
ValueError: too many values to unpack (expected 3)
>>> # 변수의 개수가 많거나 적으면 에러 발생
>>> 
>>> # 튜플을 리스트로 바꾸기
>>> card_list = list(card)		# 튜플 -> 리스트 타입 변환
>>> type(card_list)
<class 'list'>
>>> card_list
['red', 4, '다이아몬드', True]
>>> card_tuple = tuple(card_list)	# 리스트 -> 튜플 타입 변환
>>> type(card_tuple)
<class 'tuple'>
>>> card_tuple
('red', 4, '다이아몬드', True)
>>> 
