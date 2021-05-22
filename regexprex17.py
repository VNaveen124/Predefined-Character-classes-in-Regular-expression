#regexprex17.py
#program Search for digit only
import re
matinfo=re.finditer("\d"," A#6aB^ 7@H Pa")
print("-----------------------")
for mat in matinfo:
    print("start indx={}\tValue={}".format(mat.start(),mat.group()))
print("-----------------------")
