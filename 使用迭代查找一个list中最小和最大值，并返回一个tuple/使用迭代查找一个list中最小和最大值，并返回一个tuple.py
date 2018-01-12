def search_max(L=[]):
    a = L[0]
    for x in L:
        if x > a:
            a = x
    return a


def search_min(L=[]):
    b = L[0]
    for x in L:
        if x < b:
            b = x
    return b


List = []
number = int(input('请输入数组值，以-1为结束符'))
while number != -1:
    if number != -1:
        List.append(number)
        number = int(input('请输入数组值，以-1为结束符'))
max = int(search_max(List))
min = int(search_min(List))
t = (max, min)
print('最大值为%s   最小值为%s' % (max, min))
