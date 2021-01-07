# 시험 점수 계산기
print('====시험 점수를 차례대로 입력하시오.====\n')
test_lang = eval(input('국어 :'))
test_en = eval(input ('영어 :'))
test_math = eval(input('수학 :'))
print('===================\n')
print('= 시험 점수 결과 =\n')
print('===================\n\n')

print('* 국어 점수 :', test_lang, '\n')
print('* 영어 점수 :', test_en, '\n')
print('* 수학 점수 :', test_math, '\n')

# 시험 점수 평균
test_avg = (test_lang + test_en + test_math) / 3

# 시험 점수 합계 및 평균 출력
print('===================\n')
print('* 총 합계 점수 :', test_lang + test_en + test_math, '\n')
print('* 평균 점수 :', round(test_avg, 2))
print('===================')
