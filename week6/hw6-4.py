def b_next(pat):
    next = [0]
    prefix_len = 0
    i = 1
    while i < len(pat):
        if pat[prefix_len] == pat[i]:
            prefix_len += 1
            next.append(prefix_len)
            i += 1
        else:
            prefix_len = next[prefix_len - 1]
            if prefix_len == 0:
                next.append(0)
                i += 1
    return next

ans = []
def kmp_search(string,pat):
    nextb = b_next(pat)
    i = 0
    j = 0
    while i < len(string):
        if string[i] == pat[j]:
            i += 1
            j += 1
        elif j > 0:
            j = nextb[j-1]
        else:
            i += 1
        if j == len(pat):
            ans.append(i - j)
            j = nextb[j-1]

main = input()
pattern = input()
b_next(pattern)
kmp_search(main,pattern)
for i in ans:
    print(i,end=" ")
if ans == []:
    print()