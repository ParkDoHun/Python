# 디폴트 파라미터 예제1
def func1(a, b = 5, c =10):
    return a + b + c

func1(1, 2, 3)  # 1 + 2 + 3
func1(1, 2) # 1 + 2 + 10
func1(1) # 1 + 5 + 10
# func1() error, a의 디폴트 파라미터가 없다.


# 디폴트 파라미터 예제2
def func2(a = 10, b = 20):
    return a + b


func2(1, 2) # 1 + 2
func2(1) # 1 + 20
func2() # 10 + 20


# 아래는 잘못된 디폴트 파라미터
# 디폴트 파라미터는 뒤에서 부터 해야한다.
# 그래야 인수가 비었을때 판단이 가능하다.
def func3(a = 10, b, c):    # error
    return a + b + c

func3(1, 2)     # 1이 a이고 2가 b에 들어간다. error
func3(, 1, 2)   # 파라미터 기본값을 제외하고 값을 넣었지만 error

