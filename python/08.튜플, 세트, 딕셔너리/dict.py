Python 3.7.4 (tags/v3.7.4:e09359112e, Jul  8 2019, 19:29:22) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> # 딕셔너리 (키와 값의 쌍으로 구성된 데이터 모음)
>>> programmer_dict = {'Python':5, 'C':2, 'C++':3, 'Java':4}		# 딕셔너리 선언
>>> programmer_dict
{'Python': 5, 'C': 2, 'C++': 3, 'Java': 4}
>>> type(programmer_dict)
<class 'dict'>
>>> programmer_dict['Python']						# 'Python'값 확인
5
>>> 
>>> 
>>> programmer_dict['Python'] = 7 					# 특정 항목 값 변경
>>> programmer_dict
{'Python': 7, 'C': 2, 'C++': 3, 'Java': 4}
>>> programmer_dict['Ruby'] = 1 					# 항목 추가
>>> programmer_dict
{'Python': 7, 'C': 2, 'C++': 3, 'Java': 4, 'Ruby': 1}
>>> 
>>> len(programmer_dict)						# 항목 개수 확인(lenght)
5
>>> 
>>> 
>>> programmer_dict.keys()						# 전체 키 반환
dict_keys(['Python', 'C', 'C++', 'Java', 'Ruby'])
>>> # dict_keys 타입으로 반환
>>> list(programmer_dict)						# 전체 키 리스트 반환
['Python', 'C', 'C++', 'Java', 'Ruby']
>>> list(programmer_dict.values())					# 값만 출력
[7, 2, 3, 4, 1]
>>> 
>>> # 해당 값 확인
>>> 'Pyhjon' in programmer_dict
False
>>> 'Python' in programmer_dict						# 'Python'이 키로 존재하는지 확인
True
>>> 'Swift' in programmer_dict
False
>>> 'R' not in programmer_dict						# 'R'이 키로 존재하지 않는지 확인
True
>>> 
>>> # 특정 항목 삭제
>>> programmer_dict
{'Python': 7, 'C': 2, 'C++': 3, 'Java': 4, 'Ruby': 1}
>>> del programmer_dict['Ruby']						# 'Ruby'항목 삭제
>>> programmer_dict
{'Python': 7, 'C': 2, 'C++': 3, 'Java': 4}
>>> programmer_dict.clear						# 전체 항목 삭제
<built-in method clear of dict object at 0x039EA390>
>>> programmer_dict.clear()						# 전체 항목 삭제
>>> programmer_dict
{}
>>> 
>>> # 튜플을 딕셔너리로 바꾸기
>>> programmer_list = [('Python', 7), ('java', 2)]			# 리스트 생성
>>> programmer_list
[('Python', 7), ('java', 2)]
>>> programmer_dict = dict(programmer_list)				# 딕셔너리로 변환
>>> type(programmer_dict)
<class 'dict'>
>>> programmer_dict
{'Python': 7, 'java': 2}
>>> 
>>> programmer_dict['Python']
7
>>> programmer_dict['Java']
Traceback (most recent call last):
  File "<pyshell#42>", line 1, in <module>
    programmer_dict['Java']
KeyError: 'Java'
>>> programmer_dict['java']
2
>>> 
