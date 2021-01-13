Python 3.9.1 (tags/v3.9.1:1e5d33e, Dec  7 2020, 17:08:21) [MSC v.1927 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> cards = [3, 1, 5, 2]
>>> cards
[3, 1, 5, 2]
>>> type(cards)
<class 'list'>
>>> cards[0]
3
>>> cards[1]
1
>>> cards[-1]
2
>>> cards[2]
5
>>> cards[4]		# 잘못된 색인으로 인한 에러
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    cards[4]		# 잘못된 색인으로 인한 에러
IndexError: list index out of range
>>> 
>>> cards
[3, 1, 5, 2]
>>> cards[1] = 8 	# 2번째 값 변경
>>> cards
[3, 8, 5, 2]
>>> cards.append(7)	# 특정 값 추가하기
>>> cards
[3, 8, 5, 2, 7]
>>> cards.remove(5)	# 특정 값 제거하기
>>> cards
[3, 8, 2, 7]
>>> cards.insert(1, 9)	# 두 번째 항목(색인1)에 9 삽입
>>> cards
[3, 9, 8, 2, 7]
>>> cards.pop(3) 	# 네 번째 항목 값 반환 후 제거
2
>>> cards
[3, 9, 8, 7]
>>> 
>>> # 리스트 자르기와 복제하기
>>> cards[1:3]		# cards[1]부터 cards[2]까지 자르기
[9, 8]
>>> cards
[3, 9, 8, 7]
>>> cards[:2]		# 처음부터 cards[1]까지 자르기
[3, 9]
>>> cards[1:]		# cards[1]부터 끝까지 자르기
[9, 8, 7]
>>> cards		# 리스트 재확인
[3, 9, 8, 7]
>>> 
>>> sub_cards = cards[1:3]		# 자른 리스트를 sub_cards에 저장
>>> sub_cards
[9, 8]
>>> cards
[3, 9, 8, 7]
>>> new_cards = cards			# 새로운 변수에 기존 리스트 저장
>>> new_cards.append(2)			# 새로운 변수에 항목 추가
>>> new_cards
[3, 9, 8, 7, 2]
>>> cards
[3, 9, 8, 7, 2]
>>> # 메모리 주소를 넘겨준 것이므로 같은 데이터를 가진다.
>>> 
>>> # 리스트 자르기를 활용하면 해결.
>>> new_cards = cards[:]		# 새로운 변수에 기존 리스트의 복제본을 저장
>>> new_cards.append(5)
>>> new_cards
[3, 9, 8, 7, 2, 5]
>>> cards
[3, 9, 8, 7, 2]
>>> 