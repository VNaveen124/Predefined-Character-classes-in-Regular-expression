#regexprex21.py
#program search for all characters
import re
matinfo=re.finditer("."," A#6aB^ 7@H Pa")
print("-----------------------")
for mat in matinfo:
    print("start indx={}\tValue={}".format(mat.start(),mat.group()))
print("-----------------------")
