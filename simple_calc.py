print('Simple calculator...')
print('Enter math phrase like \"1 + 2\": ')
MATH_OPS = ['+', '-', '*', '/']
i = 0
res = 0
num1 = input()
for op in MATH_OPS:
    if len(num1.split(op)) > 1:
        if i == 0:
            res = int(num1.split(op)[0]) + int(num1.split(op)[1])
        elif i == 1:
            res = int(num1.split(op)[0]) - int(num1.split(op)[1])
        elif i == 2:
            res = int(num1.split(op)[0]) * int(num1.split(op)[1])
        else:
            res = int(num1.split(op)[0]) / int(num1.split(op)[1])
    i += 1
print(res)
