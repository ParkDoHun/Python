# 반복문 수행 유무 플래그
repeat = True

# repear이 True인 경우 while문 블록 반복 수행
while repeat:
    

    # 값 입력
    flag = input('마음에 드는 옷을 찾았나요? (예/아니오) : ')

    # 조건 분기
    if flag == '예':                 # 입력 받은 값이'예'인 경우
        print(':) 축하합니다!!')     # 축하 메시지 출력
        repeat = False               # while문 탈출을 위한 flag값 변경
            
    else:
        print(':( 아쉽군요.')               # 경우에 따른 메시지 출력
        print('다른 매장에서 골라보세요!')  # 다른 매장 방문 유도 메시지 출력

    
