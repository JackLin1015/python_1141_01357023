s = input()
stack = []
for ch in s:
    if ch != ')':
        stack.append(ch)
    else:
        segment = ""
        while stack and stack[-1] != '(':
            segment = stack.pop() + segment
        stack.pop()   
        num = ""
        while stack and stack[-1].isdigit():
            num = stack.pop() + num
        num = int(num)
        stack.append(segment * num)
print("".join(stack))
