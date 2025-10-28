def quicksort(list1):
    n = len(list1)
    if n <= 1:
        return list1
    left = []
    right = []
    pivot = list1[0]
    for i in range(1,n):
        if list1[i] < pivot:
            left.append(list1[i])
        else:
            right.append(list1[i])
    return quicksort(left) + [pivot] + quicksort(right)   

list1 = list(map(int, input().split()))
list2 = quicksort(list1)
list2 = ' '.join(str(i)for i in list2)
print(list2)
