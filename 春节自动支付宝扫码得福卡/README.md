春节自动支付宝扫码得福卡
============
设计思路
-----
从前些天微信跳一跳自动辅助想起，自己可以做一个自动扫描福字获得支付宝福卡的小脚本。

仿照跳一跳辅助的思路，先用ADB工具获取当前手机屏幕的截图，然后判断是否获得福卡，再
决定点击的位置。相对于跳一跳辅助，这个脚本没有了摁压时间等的判断，比较容易实现。

![](https://github.com/h1997l1997/learn-python/blob/master/%E6%98%A5%E8%8A%82%E8%87%AA%E5%8A%A8%E6%94%AF%E4%BB%98%E5%AE%9D%E6%89%AB%E7%A0%81%E5%BE%97%E7%A6%8F%E5%8D%A1/%E8%AE%AD%E7%BB%83%E5%AE%9E%E4%BE%8B/%E5%BE%AE%E4%BF%A1%E5%9B%BE%E7%89%87_20180207152555.png)
![](https://github.com/h1997l1997/learn-python/blob/master/%E6%98%A5%E8%8A%82%E8%87%AA%E5%8A%A8%E6%94%AF%E4%BB%98%E5%AE%9D%E6%89%AB%E7%A0%81%E5%BE%97%E7%A6%8F%E5%8D%A1/%E8%AE%AD%E7%BB%83%E5%AE%9E%E4%BE%8B/%E5%BE%AE%E4%BF%A1%E5%9B%BE%E7%89%87_20180207152603.png)
![](https://github.com/h1997l1997/learn-python/blob/master/%E6%98%A5%E8%8A%82%E8%87%AA%E5%8A%A8%E6%94%AF%E4%BB%98%E5%AE%9D%E6%89%AB%E7%A0%81%E5%BE%97%E7%A6%8F%E5%8D%A1/%E8%AE%AD%E7%BB%83%E5%AE%9E%E4%BE%8B/%E5%BE%AE%E4%BF%A1%E5%9B%BE%E7%89%87_20180207152608.png)

通过关键像素点的颜色，来判断是否获得福卡

![](https://github.com/h1997l1997/learn-python/blob/master/%E6%98%A5%E8%8A%82%E8%87%AA%E5%8A%A8%E6%94%AF%E4%BB%98%E5%AE%9D%E6%89%AB%E7%A0%81%E5%BE%97%E7%A6%8F%E5%8D%A1/%E8%AE%AD%E7%BB%83%E5%AE%9E%E4%BE%8B/%E5%BE%AE%E4%BF%A1%E5%9B%BE%E7%89%87_20180207152605.png)

模拟点击的位置

运行环境
------
本次运行在win10和小米6上，不同品牌的手机会有不同

主要是屏幕大小和分辨率的问题

只要和小米6手机分辨率一样大小，皆可使用

运行方法和照片
-----
先安装ADB工具，可以参考[Android 和 iOS 操作步骤](https://github.com/wangshub/wechat_jump_game/wiki/Android-%E5%92%8C-iOS-%E6%93%8D%E4%BD%9C%E6%AD%A5%E9%AA%A4)
![](https://github.com/h1997l1997/learn-python/blob/master/%E6%98%A5%E8%8A%82%E8%87%AA%E5%8A%A8%E6%94%AF%E4%BB%98%E5%AE%9D%E6%89%AB%E7%A0%81%E5%BE%97%E7%A6%8F%E5%8D%A1/%E8%AE%AD%E7%BB%83%E5%AE%9E%E4%BE%8B/651715388252697823.jpg)

连接手机到电脑，将手机固定好对准福字，保持在此界面对准福字即可

![](https://github.com/h1997l1997/learn-python/blob/master/%E6%98%A5%E8%8A%82%E8%87%AA%E5%8A%A8%E6%94%AF%E4%BB%98%E5%AE%9D%E6%89%AB%E7%A0%81%E5%BE%97%E7%A6%8F%E5%8D%A1/%E8%AE%AD%E7%BB%83%E5%AE%9E%E4%BE%8B/1517991218(1).jpg)


看到这里你就以为可以每天扫码月入百万了吗？？？
======
不可能的！
===
![](https://github.com/h1997l1997/learn-python/blob/master/%E6%98%A5%E8%8A%82%E8%87%AA%E5%8A%A8%E6%94%AF%E4%BB%98%E5%AE%9D%E6%89%AB%E7%A0%81%E5%BE%97%E7%A6%8F%E5%8D%A1/%E8%AE%AD%E7%BB%83%E5%AE%9E%E4%BE%8B/631981034644834707.jpg)
原来支付宝扫福字每天是有限制的！
=========
![](http://pic.cr173.com/up/2016-4/2016421114346718.jpg)


欢迎star本项目，同时follow本账户
---
欢迎访问[我的博客](http://www.h1997l1997.cn/) 
---
