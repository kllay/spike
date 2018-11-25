import uiautomator2
import time
from config import sina_pkg_code
from secrecy import UserName, Passwd


def login_weibo(d, UserName, Passwd):
    # 启动微博
    d.app_start("com.sina.weibo")

    # 开启电话与存储权限
    d(text=u"		开启		").click()
    d(resourceId="android:id/button1").click()
    d(resourceId="android:id/button1").click()

    # 关闭弹窗
    d(resourceId="com.sina.weibo:id/iv_close").click()

    # 进入登入页面
    d(resourceId="com.sina.weibo:id/titleBack").click()

    #
    d(resourceId="com.sina.weibo:id/tv_login_more_questions").click()

    d(resourceId="com.sina.weibo:id/etLoginUsername").set_text(UserName)

    d(resourceId="com.sina.weibo:id/etPwd").set_text(Passwd)

    d(resourceId="com.sina.weibo:id/bnLogin").click()

    d(text=u"点击按钮进行验证").click()

    # 新用户红包页面
    if d(resourceId="com.sina.weibo:id/iv_close").exists(timeout=3):
        d(resourceId="com.sina.weibo:id/iv_close").click()


def verify():
    pass


def goto_topic():
    # 进入个人页面
    d(resourceId="com.sina.weibo:id/cabWeibo").click()


def auto_top(d):
    time.sleep(3)
    # 个人页面
    d.click(0.886, 0.958)
    # 点击微博详情
    d(resourceId="com.sina.weibo:id/cabWeibo").click()
    # 点击评论
    d(resourceId="com.sina.weibo:id/lyButton", className="android.widget.LinearLayout", instance=1).click()
    # 点击插入表情
    if d(resourceId="com.sina.weibo:id/tvItemCmtContent").exists(timeout=2):
        d(resourceId="com.sina.weibo:id/tvItemCmtContent").long_click()
        d(text=u"删除").click()
        d(text=u"确定").click()
        d.press("back")
        d(resourceId="com.sina.weibo:id/lyButton", className="android.widget.LinearLayout", instance=1).click()

    # 点击一个表情 [心]
    d(resourceId="com.sina.weibo:id/edit_view").set_text('[心]')
    # 点击发送
    d(resourceId="com.sina.weibo:id/tv_send").click()


def post_topic(d, text):
    """ 进入到话题页面 """
    d(text=u"发帖").click()
    # 编辑内容
    d(resourceId="com.sina.weibo:id/edit_view").set_text(text)
    # 点击发送
    d(resourceId="com.sina.weibo:id/titleSave").click()


if __name__ == "__main__":
    # d = uiautomator2.connect("7fb4dc26")
    d = uiautomator2.connect_wifi("192.168.1.101")
    # d.app_clear(sina_pkg_code)
    # login_weibo(d, UserName=UserName, Passwd=Passwd)
    d.app_stop(sina_pkg_code)
    d.app_start(sina_pkg_code)
    auto_top(d=d)
    d.app_clear(sina_pkg_code)
