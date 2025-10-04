m = int(input())
for i in range(m):
    s = input()
    my_list = list(s)
    n = []       
    num = []    
    for ch in my_list:
        if ch not in n:   
            n.append(ch)
            num.append(my_list.count(ch))
    max_c = num[0]
    for j in range(len(num)):
        if(num[j] > max_c):
            max_c = num[j]
    max_index = num.index(max_c)
    print(n[max_index])
