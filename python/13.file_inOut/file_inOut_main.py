Python 3.9.1 (tags/v3.9.1:1e5d33e, Dec  7 2020, 17:08:21) [MSC v.1927 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
========== RESTART: C:\git_study\python\13.file_inOut\inOut_src_02.py ==========
Traceback (most recent call last):
  File "C:\git_study\python\13.file_inOut\inOut_src_02.py", line 1, in <module>
    f = open("C:/git_study/python/13.파일 입출력/test_open.txt", "r")
FileNotFoundError: [Errno 2] No such file or directory: 'C:/git_study/python/13.파일 입출력/test_open.txt'
>>> 
========== RESTART: C:\git_study\python\13.file_inOut\inOut_src_02.py ==========
Traceback (most recent call last):
  File "C:\git_study\python\13.file_inOut\inOut_src_02.py", line 2, in <module>
    print(f.readline())
UnicodeDecodeError: 'cp949' codec can't decode byte 0xeb in position 10: illegal multibyte sequence
>>> 
========== RESTART: C:\git_study\python\13.file_inOut\inOut_src_02.py ==========
Traceback (most recent call last):
  File "C:\git_study\python\13.file_inOut\inOut_src_02.py", line 2, in <module>
    print(f.readline())
UnicodeDecodeError: 'cp949' codec can't decode byte 0xeb in position 10: illegal multibyte sequence
>>> 
========== RESTART: C:\git_study\python\13.file_inOut\inOut_src_02.py ==========
testOpen, 낙타표기법(카멜표기법)
>>> print("loaded text: %s" & txt)
Traceback (most recent call last):
  File "<pyshell#0>", line 1, in <module>
    print("loaded text: %s" & txt)
NameError: name 'txt' is not defined
>>> print("loaded text: %s" % txt)
Traceback (most recent call last):
  File "<pyshell#1>", line 1, in <module>
    print("loaded text: %s" % txt)
NameError: name 'txt' is not defined
>>> 