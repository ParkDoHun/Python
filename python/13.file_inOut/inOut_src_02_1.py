inFp = None         # 입력 파일
inStr =""           # 읽어 온 문자열

inFp = open("c:/git_study/python/13.file_inOut/test_open.txt", "r", encoding="UTF8")

while True:
    inStr = inFp.readline()
    if inStr == "":
        break;
    print(inStr, end="")

inFp.close()
