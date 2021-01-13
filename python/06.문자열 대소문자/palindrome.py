text = input('문자열을 입력하세요. : ')

origin = text.replace(' ', '')          # 문자열 공백 제거
reverse = str()                         # 역순 문자열 저장 변수

index = len(origin)-1                   # 마지막 색인 추출

while index >= 0:
    reverse += origin[index]
    index -= 1                          # 색인 감소

if origin == reverse:
    print("입력하신 문장은 회문이 맞습니다.")

else:
    print("입력하신 문장은 회문이 아닙니다.")


# replace("찾을 내용", "바꿀 내용", 변경 횟수)
