def partition(arr, low, high):
    n = len(arr)
    pivot = arr[high]
    i = low-1
    for j in range(low,high):
        if arr[j] < pivot:
            i += 1
            arr[i],arr[j] = arr[j],arr[i]
            if(i != j):
                print(arr)
    arr[i+1],arr[high] = arr[high],arr[i+1] 
    if(i+1 != high):
        print(arr)
    return i+1

def quick_sort(arr, low, high):
   if low < high:
       pi = partition(arr, low, high)
       quick_sort(arr, low, pi - 1)
       quick_sort(arr, pi + 1, high)
arr = list(map(int,input().split()))
count = 0
print(arr)
quick_sort(arr,0,len(arr)-1)