lines = ['123', 'test', 'text']

f = open("c:/git_study/python/13.file_inOut/test_open.txt", "w", encoding="UTF8")

f.writelines(lines)
f.close()
