inFp = None
inList = ""

inFp = open("c:/git_study/python/13.file_inOut/test_open.txt", "r", encoding="UTF8")

inList = inFp.readlines(54)
print(inList)

inFp.close()
