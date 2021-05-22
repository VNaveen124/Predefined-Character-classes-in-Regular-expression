#regexprex19.py
#program Search for word Character [A-Za-z0-9] (except special symbols)
import re
matinfo=re.finditer("\w"," A#6aB^ 7@H Pa")
print("-----------------------")
for mat in matinfo:
    print("start indx={}\tValue={}".format(mat.start(),mat.group()))
print("-----------------------")
