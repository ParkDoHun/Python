# 게임 제목 출력
print('## 안나와 신후의 가위, 바위, 보 게임 ##')

# 값 입력
Ana = input('안나를 위한 가위, 바위, 보를 입력하세요 : ')
Shinfu = input('신후를 위한 가위, 바위, 보를 입력하세요 : ')

# 조건문
if(Ana == '가위' and Shinfu == '가위'):
    print('무승부')
    
elif (Ana == '가위' and Shinfu == '바위'):
    print('신후 승리')
    
elif (Ana == '가위' and Shinfu == '보'):
    print('안나 승리')
    
elif (Ana == '바위' and Shinfu == '가위'):
    print('안나 승리')
    
elif ( Ana == '바위' and Shinfu == '바위'):
    print('무승부')
    
elif ( Ana == '바위' and Shinfu == '보'):
    print('신후 승리')
    
elif (Ana == '보' and Shinfu == '가위'):
    print('신후 승리')
    
elif (Ana == '보' and Shinfu == '바위'):
    print('안나 승리')
    
elif (Ana == '보' and Shinfu == '보'):
    print('무승부')

# 입력 값이 다르면
else:
    print("'가위', '바위', '보'중 하나 입력하시오.")
    
    
