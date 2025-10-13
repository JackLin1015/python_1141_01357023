def operationcount(sum,operation,carry,count):
    for i in range(count):
        if(carry+sum[i] >= 10):
            operation += 1
            carry = 1
        else:
            carry = 0 
    return operation  
list1 = list(map(int, input().split()))
list1_0 = []
list1_1 = []
count = 0
tool1 = 1
operation = 0
while(list1[0] / tool1 != 0):
    list1_0.append(list1[0] // tool1  % 10)
    list1_1.append(list1[1] // tool1  % 10)
    count += 1
    tool1 *= 10
sum = list(map(lambda x,y: x+y,list1_0,list1_1))
carry = 0
result = operationcount(sum,operation,carry,count)
if(result > 1):
    print(f"{result} carry operations")
elif (result == 1):
    print("1 carry operation")
else:
    print("No carry operation")