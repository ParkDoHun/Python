#### 환율 계산기 ####
# 환전 금액 입력
exchange_in = int(input('환전 금액을 입력하세요. : '))

# 각국의 환율(2017년 08월 19일 기준)
print('\n\n======각국의 환율======')
print('- 미국 :1,141.50원/USD')
print('- 호주 : 905.15원/AUD')
print('- 뉴질랜드 : 836.15원/NZD')

print('\n======변환된 환율======')

# 각 변수에 연산값 저장
usd = round(exchange_in / 1141.50,2)
aud = round(exchange_in / 905.15, 2)
nzd = round(exchange_in / 836.15, 2)

# 환울 변환 출력
print('미국 :', float(usd), 'USD')
print('호주 :', float(aud), 'AUD')
print('뉴질랜드', float(nzd), 'NZD')


