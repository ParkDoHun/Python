inFp, outFp = None, None
inStr = ""

inFp = open("c:/git_study/python/13.file_inOut/test_open.txt", "r", encoding="UTF8")
outFp = open("c:/git_study/python/13.file_inOut/test_open_copy.txt", "w", encoding="UTF8")

inStr = inFp.readlines()
for i in inStr:
    outFp.writelines(i)

inFp.close()
outFp.close()
print("**복사 성공**")
