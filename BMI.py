name=input
tizhong=float(input('请输入体重'))
shengao=float(input('请输入身高'))
a=tizhong/(shengao*shengao)
if a<13.5:
    print('too thin')
elif a<25:
        print('normal')
elif a<28:
        print('overweight')
elif a<32:
        print('oberity')
   