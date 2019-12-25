import re
s = "МИНИМУМ"
result = []
for word in re.split(r' ', s):
    if word:
        fl = word[0]
        word = ''.join(['.' if x == fl else x for x in word[1:]])
        result.append(fl + word)
    else:
        result.append('')
 
print(' '.join(result))