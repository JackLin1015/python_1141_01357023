def func():
    with open('input.txt','r',encoding='utf-8') as file:
        content = file.read()
    use2 = [ch for ch in content.strip().lower() if ch.isalpha()]
    diccount2 = {}
    for w in use2:
        diccount2[w] = diccount2.get(w,0) + 1
    diccount_list2 = sorted(diccount2.items(), key = lambda kv:(kv[1], kv[0]),reverse=True)
    i = 0
    j = 1
    for ans in range(3):
        print(diccount_list2[ans][i],end=" ")
        print(diccount_list2[ans][j],end=" ")