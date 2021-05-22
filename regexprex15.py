#regexprex15.py
#program Search for space character only
import re
matinfo=re.finditer("\s"," A#6aB^ 7@H Pa")
print("------------")
for mat in matinfo:
    print("start indx={}\tValue={}".format(mat.start(),mat.group()))
print("------------")
