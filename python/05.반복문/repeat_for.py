Python 3.9.1 (tags/v3.9.1:1e5d33e, Dec  7 2020, 17:08:21) [MSC v.1927 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> cards = [3, 1, 5, 2]
>>> cards
[3, 1, 5, 2]
>>> type(cards)
<class 'list'>
>>> 
>>> # 특정값 호출
>>> cards[0]
3
>>> cards[3]
2
>>> cards[-1]
2
>>> 
>>> # 리스트 길이
>>> len(cards)
4
>>> 
>>> # 반복문 for
>>> colors = ['black', 'blue', 'yellow', 'red']		# 리스트 선언
>>> 
>>> for color in colors:				# for문 실행
	print(color, len(colors))			#

black 4
blue 4
yellow 4
red 4
>>> 
================== RESTART: C:/git_study/python/05.반복문/for.py ==================
black 5
blue 4
yellow 6
red 3
>>> 
>>> # 이중 for
>>> # 가위-바위-보 리스트 선언
>>> all = ['가위', '바위', '보']
>>> 
>>> # 바깥쪽 for문
>>> for user_a in all:

	# 안쪽 for문
	for user_b in all:

		# 결과 출력
		print(user_a, 'vs', user_b)

		
가위 vs 가위
가위 vs 바위
가위 vs 보
바위 vs 가위
바위 vs 바위
바위 vs 보
보 vs 가위
보 vs 바위
보 vs 보
>>> 
================ RESTART: C:/git_study/python/05.반복문/for_for.py ================
가위 vs 가위
가위 vs 바위
가위 vs 보
바위 vs 가위
바위 vs 바위
바위 vs 보
보 vs 가위
보 vs 바위
보 vs 보
>>> 