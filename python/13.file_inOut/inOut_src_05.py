inFp = None
inList, inStr = [], ""

inFp = open("c:/git_study/python/13.file_inOut/test_open.txt", "r", encoding="UTF8")

inList = inFp.readlines(55)
for inStr in inList:
    print(inStr, end="")

inFp.close()
