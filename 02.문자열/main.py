Python 3.9.1 (tags/v3.9.1:1e5d33e, Dec  7 2020, 17:08:21) [MSC v.1927 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> guide = '모두 작은 따옴표(\')로 감싸도 된다.')
SyntaxError: unmatched ')'
>>> guide = '모두 작은 따옴표(\')로 감싸도 된다.'
>>> print(guide)
모두 작은 따옴표(')로 감싸도 된다.
>>> # 가능하면 이 방법은 사용하지 않는게 좋다.
>>> # 여러 줄인 문자열
>>> # 파이선은 여러 줄의 문자열을 인식하기 위하여 작은따옴표 3개 또는 큰따옴표 3개를 문자열의 시작과 끝에 붙이는 문법을 제공하고 있다.
>>> text = '''실패하는 것보다 도전하지 않는 것을 두려워하라.'''
>>> print
<built-in function print>
>>> print(text)
실패하는 것보다 도전하지 않는 것을 두려워하라.
>>> text = '''실패하는 것보다
도전하지 않는 것을
두려워하라.'''
>>> print(text)
실패하는 것보다
도전하지 않는 것을
두려워하라.
>>> # 위의 방법은 소스코드를 읽을때 가독성이 떨어지는 주범이된다.
>>> print('실패하는 것보다\n'
      '도전하지 않는 것을\n'
      '두려워하라.')
실패하는 것보다
도전하지 않는 것을
두려워하라.
>>> # 어떤 방법을 사용하든 문법에 문제가 없더라도 최대한 읽기 좋은 소스코드를 작성하기 위해서 좋은 코딩 습관을 들이는 것은 중요.
>>> #### 연산자로 문자열 연결 ####
>>> 
>>> name = input('이름을 입력하세요. : ')
이름을 입력하세요. : ParkDoHun
>>> welcome = name + '님, 반갑습니다.'
>>> print(welcome)
ParkDoHun님, 반갑습니다.
>>> # 위의 코드는 +연산자를 사용해 문자를 연결 -> 이름이 저장된 name변수에 문자열을 붙여서 출력
>>> 
>>> # *연산자를 사용한 출력
>>> cheer = 'fighting!' * 3
>>> print(cheer)
fighting!fighting!fighting!
>>> 
>>> # 문자열의 길이 확인 : len() 함수
>>> len('파이선 프로그래밍 테스트.')
14
>>> text = '쉬운 파이선 프로그래밍!'
>>> len(text)
13
>>> 
>>> # 문자열 메소드
>>> word = 'Python'
>>> word.upper();
'PYTHON'
>>> # 대문자로 출력
>>> word.lower();
'python'
>>> # 소문자로 출력
>>> '-'.join(word)
'P-y-t-h-o-n'
>>> # 문자 사이에 '-' 삽입
>>> print(word)
Python
>>> # 원본 문자 출력
>>> 
>>> text = ("그가 말했다. \"이제 WHAT은 결정되었으니, 'HOW'에 대해서 이야기해보자.")
>>> print(text)
그가 말했다. "이제 WHAT은 결정되었으니, 'HOW'에 대해서 이야기해보자.
>>> text = ("그가 말했다. \"이제 'WHAT'은 결정되었으니, 'HOW'에 대해서 이야기해보자.\"")
>>> print(text)
그가 말했다. "이제 'WHAT'은 결정되었으니, 'HOW'에 대해서 이야기해보자."
>>> print('Don\'t be afraid to fail.\n'
      '실패하는 것을 두려워하지 말아라.\n'
      'Be afraid not to try.\n'
      '시도조차 하지 않는 것을 두려워하라.)
      
SyntaxError: EOL while scanning string literal
>>> print('Don\'t be afraid to fail.\n'
      '실패하는 것을 두려워하지 말아라.\n'
      'Be afraid not to try.\n'
      '시도조차 하지 않는 것을 두려워하라.')
Don't be afraid to fail.
실패하는 것을 두려워하지 말아라.
Be afraid not to try.
시도조차 하지 않는 것을 두려워하라.
>>> a = '파이선'
>>> b = '이야기'
>>> print(a +' ' +b)
파이선 이야기
>>> a = 'text_no1'
>>> print(a * 3)
text_no1text_no1text_no1
>>> 
>>> # 학습 일기 작성
>>> diary = """
*날짜 : 2021년 01월 04일(월)
*제목 : 파이선 문자열 타입
*내용 :
	- 문자열은 작은따옴표(')혹은 큰따옴표(")를 사용하여 나타낸다.
	- 둘 다 사용이 가능하지만 일반적으로 작은따옴표(')를 사용한다.
	- 하지만 중요한 것은 작은따옴표나 큰따옴표 한 가지를 일괄적으로 사용하는 것이다."""
>>> print(diary)

*날짜 : 2021년 01월 04일(월)
*제목 : 파이선 문자열 타입
*내용 :
	- 문자열은 작은따옴표(')혹은 큰따옴표(")를 사용하여 나타낸다.
	- 둘 다 사용이 가능하지만 일반적으로 작은따옴표(')를 사용한다.
	- 하지만 중요한 것은 작은따옴표나 큰따옴표 한 가지를 일괄적으로 사용하는 것이다.
>>>  # 숫자타입과 연산자


