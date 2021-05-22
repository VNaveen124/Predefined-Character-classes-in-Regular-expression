#regexprex16.py
#program Search for all except space character
import re
matinfo=re.finditer("\S"," A#6aB^ 7@H Pa")
print("-----------------------")
for mat in matinfo:
    print("start indx={}\tValue={}".format(mat.start(),mat.group()))
print("-----------------------")
