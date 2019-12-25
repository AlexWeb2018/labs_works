import re
print(min([len(i) for i in re.findall(r"[\w']+", input())]))