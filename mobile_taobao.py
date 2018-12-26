# -*- coding:utf-8 -*-
"""
@Time   :2018/12/26 13:54
@Author :派森

本代码是使用xpath定位控件然后进行点击
速度理论上会比直接选择会快上许多
"""
import uiautomator2
import time

d = uiautomator2.connect_usb('7fb4dc26')

# 当前时间
now_time = time.localtime()

# 目标时间
target_time = time.strptime("2018-12-26 16:12:00", "%Y-%m-%d %H:%M:%S")

# 目标时间 减去当前时间 就是我们需要等待的时间
diff = (target_time.tm_hour - now_time.tm_hour) * 60 * 60 + (target_time.tm_min - now_time.tm_min) * 60 + (target_time.tm_sec - now_time.tm_sec)

time.sleep(diff)

# 点击物品
# d(resourceId="com.taobao.taobao:id/tqg_goods_name").click()
d.xpath("//android.widget.TextView[@text='年货巧克力大礼包零食一整箱']").click()

# 点击立即购买
# d(resourceId="com.taobao.taobao:id/detail_main_sys_button", text=u"立即购买").click()
d.xpath("//android.widget.TextView[@text='立即购买']").click()

# 点击商品属性
# d(resourceId="com.taobao.taobao:id/tv_property_desc").click()
d.xpath("//android.widget.TextView[@text='A款：805g巧克力大礼包（ 分享装）']").click()

# 确定
# d(resourceId="com.taobao.taobao:id/confirm_text").click()
d.xpath("//android.widget.TextView[@text='确定']").click()

# 提交订单
# d(resourceId="com.taobao.taobao:id/btn_confirm").click()
# d.xpath("//android.widget.Button[@text='提交订单']").click()

