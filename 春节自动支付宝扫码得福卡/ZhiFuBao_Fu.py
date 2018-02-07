''''''''''
支付宝自动扫描福字
运行环境：win10＋小米6
版本：0.1
2018-2-7
'''''''''''

import os
import time
from PIL import Image
from optparse import OptionParser


def option():
    # 获取脚本所在当前目录
    current_dir = os.path.dirname(__file__)
    # 根据截图时间生成默认文件名：20170722142831.png
    file_name = "%s.png" % time.strftime("%Y%m%d%H%M%S", time.localtime())

    usage = "screencap.py [-d <directory> -f <filename>]"
    description = "Automatic screenshots for android, After in PC display ."

    p = OptionParser(usage=usage, description=description)

    p.add_option("-d", "--dir",
                 dest="directory", default=current_dir,
                 help="directory of save the address")

    p.add_option("-f", "--filename",
                 dest="filename", default=file_name,
                 help="filename of screen shots file name")
    return p.parse_args()


def screen(options):
    # 截图
    os.popen("adb shell screencap /sdcard/{filename}".format(filename=options.filename)).read()

    # 截图导出
    os.popen(r"adb pull /sdcard/{filename} {dir}".format(filename=options.filename, dir=options.directory)).read()
    # 打开截图
    #print(os.popen(r"start {filename}".format(filename=options.filename)).read())
    # 删除截图
    os.popen("adb shell rm /sdcard/{filename}".format(filename=options.filename))


def open(filename):
    # 判断是否获得福卡
    im = Image.open(filename)
    sign = 0
    for n in range(289, 332):
        no1 = im.getpixel((289, 299))
        no2 = im.getpixel((n, 299))
        if no2 != no1:
            sign = 1
    return sign


def touch(sign):
    # 模拟点击
    if sign == 1:
        print(os.system("adb shell input tap 540 1633"))
        print("已成功处理点击，没有获得福卡，程序继续")
    if sign == 0:
        print(os.system("adb shell input tap 539 1470"))
        print("已成功处理点击,成功获得福卡，程序继续")
    time.sleep(5)


if __name__ == '__main__':
    yn=input("请确定手机已连接电脑，并且电脑已安装ADB(y/n)")
    if yn=='y':
        while 1==1 :
            options, args = option()
            screen(options)
            sign = open(options.filename)
            touch(sign)
            os.remove(options.filename)
    else:
        exit()
