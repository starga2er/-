layer = input()

back = 0
stack = 0
num = 0
for i in layer:
    if i == '(':
        if back == '(':
            stack +=1
        back = '('
    else:
        if back == '(':
            num += stack
        else :
            stack -=1
            num += 1
        back = ')'

print(num)