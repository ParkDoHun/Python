import turtle

n = 60

turtle.shape('turtle')
turtle.speed(10)    # 속도 : 'fastest': 0/ 'fast': 10/ 'normal': 6/ 'slow': 3/ 'slowest': 1

for i in range(n):
    turtle.circle(120)
    turtle.right(360 / n)

turtle.done()
