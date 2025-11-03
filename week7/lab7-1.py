import my_func
import re
with open('input.txt','r',encoding='utf-8') as file:
    content = file.read()
use = [w for w in re.split(r"[, .;?\-'\n]+", content.strip().lower()) if w]
diccount = {}
for w in use:
    diccount[w] = diccount.get(w, 0) + 1
diccount_list = sorted(diccount.items(), key = lambda kv:(kv[1], kv[0]),reverse=True)
i = 0
j = 1
for ans in range(3):
    print(diccount_list[ans][i],end=" ")
    print(diccount_list[ans][j],end=" ")
print()
my_func.func()