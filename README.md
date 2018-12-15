# spike
京东、淘宝、小米商城等一系列的秒杀脚本。

>秒杀脚本是基于自动化测试库 [uiautomator2](https://github.com/openatx/uiautomator2)编写
。

### 自动发言工具使用前提

使用自动化工具控制手机是有姐前提

- 手机
  - 打开开发者模式
  - 允许usb调试、允许安装位置来源的软件
- 安卓模拟器
  - 安卓模拟器还需要使用adb指令连接之后才能进行控制
- 电脑
  - 配置adb到环境变量
  - 安装python环境
  - 安装uiautomator2环境

### 手机配置

1. 打开开发者模式
2. 进入开发者，选择运行usb调试、允许安装未知来源的软件
3. 安卓模拟器同样需要完成上面两点，还需要先在dos窗口下使用adb连接手机之后才能进行使用。
   参考：[mumu模拟器使用adb调试](https://www.jianshu.com/p/6d13c590822f)，[adb连接夜游神模拟器](https://blog.csdn.net/kongxingxing/article/details/53363038)
### 环境搭建

+ 安装adb

	下载 [adb](https://developer.android.com/studio/releases/platform-tools.html) 并且将其配置到环境变量，它是后面的基础。若没有配置好，后面步骤无法进行。

+ 安装uiautomator2安装

	这个是核心驱动器，先使用`pip install --pre uiautomator2`安装uiautomator2，再进行控制手机之前，先需要将打开开发者模式、usb调试的手机连接到电脑，再使用`python -m uiautomator2 init`初始化。这一步会安装一个守护进程（客户端、驱动）到手机，实现使用python控制手机的目的。

+ 安装获取页面控件的可视化工具

	安装：`pip install --pre --upgrade weditor`，

	启动：`python3 -m weditor`。

	启动之后会默认打开`http://atx.open.netease.com/`页面，这里就是一个交互式的手机控制器。这个是东西的一部分功能是实现了安卓原生`uiautomatorviewer`，并且支持点击、获取控件、发送指令的功能，能自动生成代码，大大地加快了开发速度，且功能十分强大。
	

关于环境搭建也可以查看 [这篇文章](https://testerhome.com/topics/11357) 里面已经讲述的十分清楚了.

#### 开发环境：

+ python3.6.5
+ pychram



### 程序优化

本代码在没有优化之前，运行之后比较慢，很难抢到东西。自己可以尝试用 xpath 选择器优化一下代码，加速控件寻找以及点击的速度，这样才能帮助你们抢到心仪的物品。

### 感谢：

[uiautomator2 使用Python测试 Android应用](https://www.cnblogs.com/fnng/p/8486863.html)

https://github.com/openatx/uiautomator2

https://testerhome.com/topics/11357
