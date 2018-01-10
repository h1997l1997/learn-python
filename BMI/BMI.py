name = input('输入你的姓名')
tizhong = float(input('请输入体重(千克）'))
shengao = float(input('请输入身高(米)'))
a = tizhong / (shengao * shengao)
print('%s 你好\n你的BMI指数为' % name)
if a < 13.5:
    print('过轻')
elif a < 25:
    print('正常')
elif a < 28:
    print('过重')
elif a < 32:
    print('肥胖')
elif a < 35:
    print('严重肥胖')
