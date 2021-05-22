#regexprex18.py
#programSearch for all except Digit
import re
matinfo=re.finditer("\D"," A#6aB^ 7@H Pa")
print("-----------------------")
for mat in matinfo:
    print("start indx={}\tValue={}".format(mat.start(),mat.group()))
print("-----------------------")
