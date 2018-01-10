def calc(numbers):
    sum = 1
    numbers.pop(0)
    for n in numbers:
        sum = sum * n
    return sum


def add(numbers):
    sum = 0
    for n in numbers:
        sum = sum + n
    return sum


summer = [0, ]
a = 0
while a != -1:
    print('输入选择运算的编号，输入-1为退出')
    print('选项1：累加')
    print('选项2：累乘')
    a = int(input())
    if a == -1:
        exit()
    if a == 1:
        b = 0
        while b != -1:
            print('输入需要相加的数字，以输入-1为终止')
            b = int(input())
            if b != -1:
                summer.append(b)
            if b == -1:
                sum = add(summer)
                print(sum)
                exit()
    elif a == 2:
        c = 0
        while c != -1:
            print('输入需要相乘的数字，以输入-1为终止')
            c = int(input())
            if c != -1:
                summer.append(c)
            if c == -1:
                sum = calc(summer)
                print(sum)
                exit()
