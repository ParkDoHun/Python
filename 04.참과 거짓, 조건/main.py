Python 3.9.1 (tags/v3.9.1:1e5d33e, Dec  7 2020, 17:08:21) [MSC v.1927 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> # 논리 타입의 개념
>>> 100 < 200 # 100이 200보다 작은가?
True
>>> 100 > 200 # 100이 200보다 큰가?
False
>>> 100 == 200 # 100이 200과 같은가?
False
>>> 100 != 200 # 100은 200과 같지 않은가? (!는 부정문)
True
>>> 
>>> # 논리 연산자
>>> 100 > 200 or 400 > 300 # 참 혹은 거짓인 경우
True
>>> 100 > 200 and 400 > 300 # 참 그리고 거짓인 경우
False
>>> not 100 > 200 # 거짓의 반대인 경우
True
>>> 
>>> # 논리 타입을 숫자로 바꾸기
>>> int(True) # 참 데이터를 숫자로 바꾸기
1
>>> int(False) # 거짓 데이터를 숫자로 바꾸기
0
>>> 
======== RESTART: C:/Users/bee64/Desktop/python/04.참과 거짓, 조건/if_else.py ========
마음에 드는 옷을 찾았나요? (예/아니오) : 예
:) 축하합니다!!
>>> 
======== RESTART: C:/Users/bee64/Desktop/python/04.참과 거짓, 조건/if_else.py ========
마음에 드는 옷을 찾았나요? (예/아니오) : 아니오
:( 아쉽군요.
>>> 
>>> 
==== RESTART: C:/Users/bee64/Desktop/python/04.참과 거짓, 조건/if_else_upglade.py ====
마음에 드는 옷을 찾았나요? (예/아니오) : 예
:) 축하합니다!!
>>> 
==== RESTART: C:/Users/bee64/Desktop/python/04.참과 거짓, 조건/if_else_upglade.py ====
마음에 드는 옷을 찾았나요? (예/아니오) : 아니오
'예' 또는 '아니요'로만 입력하세요.
>>> 
>>> # 수정
>>> 
==== RESTART: C:/Users/bee64/Desktop/python/04.참과 거짓, 조건/if_else_upglade.py ====
마음에 드는 옷을 찾았나요? (예/아니오) : 예
:) 축하합니다!!
>>> 
==== RESTART: C:/Users/bee64/Desktop/python/04.참과 거짓, 조건/if_else_upglade.py ====
마음에 드는 옷을 찾았나요? (예/아니오) : 아니오
:( 아쉽군요.
>>> 
==== RESTART: C:/Users/bee64/Desktop/python/04.참과 거짓, 조건/if_else_upglade.py ====
마음에 드는 옷을 찾았나요? (예/아니오) : 아니요
'예' 또는 '아니오'로만 입력하세요.
>>> 
==== RESTART: C:/Users/bee64/Desktop/python/04.참과 거짓, 조건/if_else_upglade.py ====
마음에 드는 옷을 찾았나요? (예/아니오) : Y
'예' 또는 '아니오'로만 입력하세요.
>>> 
>>> # 중첩 분기문
>>> 
==== RESTART: C:/Users/bee64/Desktop/python/04.참과 거짓, 조건/if_else_upglade2.py ===
마음에 드는 옷을 찾았나여? (예/아니오) : 예
:) 축하합니다!!
가격이 얼마인가요? 90000
:) 구매합니다.
>>> 
==== RESTART: C:/Users/bee64/Desktop/python/04.참과 거짓, 조건/if_else_upglade2.py ===
마음에 드는 옷을 찾았나여? (예/아니오) : 예
:) 축하합니다!!
가격이 얼마인가요? 100000
:) 구매합니다.
>>> 
==== RESTART: C:/Users/bee64/Desktop/python/04.참과 거짓, 조건/if_else_upglade2.py ===
마음에 드는 옷을 찾았나여? (예/아니오) : 예
:) 축하합니다!!
가격이 얼마인가요?
Traceback (most recent call last):
  File "C:/Users/bee64/Desktop/python/04.참과 거짓, 조건/if_else_upglade2.py", line 12, in <module>
    if int(price) <= 100000:            # 입력 받은 가격이 10만원 이하인 경우
ValueError: invalid literal for int() with base 10: ''
>>> 
==== RESTART: C:/Users/bee64/Desktop/python/04.참과 거짓, 조건/if_else_upglade2.py ===
마음에 드는 옷을 찾았나여? (예/아니오) : 예
:) 축하합니다!!
가격이 얼마인가요? 110000
:( 포기합니다.
>>> 