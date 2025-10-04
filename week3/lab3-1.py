f_num = list(map(int,input().split()))
n = set(map(int,input().split()))
m = set(map(int,input().split()))
intersection = n & m
print(len(intersection))
intersection = sorted(list(intersection)) 
if(intersection == []):
    print()
else:
    intersection = ' '.join(str(i)for i in intersection)
    print(intersection)
