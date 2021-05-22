#regexprex20.py
#program Search for all except word Character (except [A-Za-z0-9] )
import re
matinfo=re.finditer("\W"," A#6aB^ 7@H Pa")
print("-----------------------")
for mat in matinfo:
    print("start indx={}\tValue={}".format(mat.start(),mat.group()))
print("-----------------------")
