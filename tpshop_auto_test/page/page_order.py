from time import sleep

from tpshop_auto_test import page
from tpshop_auto_test.base.base import Base


class PageOrder(Base):
    # 点击我的购物车 .fl
    def page_click_my_car(self):
        self.base_click(page.order_mycar)
        sleep(1)
    # 点击全选选中所有商品 .checkFull
    # def page_click_all(self):
    #     self.base_click(page.order_all)
    # 点击去结算 .paytotal
    def page_click_check_out(self):
        self.base_click(page.order_paytotal)
        sleep(1)
    # 处理错误提示框
    # def page_exit_alert(self):
    #     alert=self.driver.switch_to.alert
    #     alert.accept()
    #     sleep(2)
    # 点击新增收货地址
    def page_click_add_address(self):
        self.base_click(page.order_add_address)
        sleep(1)
    # 填写收货人
    def page_input_recipient(self,recipient):
        self.base_input(page.order_recipient,recipient)
    # 填写手机号
    def page_input_tel(self,tel):
        self.base_input(page.order_tel,tel)
        sleep(1)
    """填写收货地址"""

    # 切换iframe弹窗
    def page_iframe(self):
        self.driver.switch_to.frame(page.order_iframe_id)
    # 重置地址选择（设为默认状态）
    def page_reset_address(self):
        self.base_select_first(page.order_address_Province)
        sleep(1)
    # 切换省
    def page_switch_Province(self,province):
        self.base_select(page.order_address_Province,province)
        sleep(1)
    # 切换市
    def page_switch_city(self,city):
        self.base_select(page.order_address_city,city)
        sleep(1)
    # 切换区
    def page_switch_district(self,district):
        self.base_select(page.order_address_district,district)
    # 填写详细地址
    def page_input_address_detail(self,address_detail):
        self.base_input(page.order_address_detail,address_detail)
    # 填写邮编
    def page_input_postal_code(self,postal_code):
        self.base_input(page.order_postal_code,postal_code)
    # 点击保存
    def page_click_save(self):
        self.base_click(page.order_save)
        sleep(2)
    #切换到默认页面
    def page_return(self):
        self.driver.switch_to.default_content()
    # 点击 提交订单 .checkout-submit
    def page_click_submit(self):
        self.base_click(page.order_submit)
        sleep(4)
    # 判断是否订单提交成功
    def page_submit_success(self):
        return self.base_get_text(page.order_submit_success)
    # 获取异常文本
    def page_get_fail(self):
        try:
            alert = self.driver.switch_to.alert
            alert_text = alert.text
            return alert_text
        except Exception:
            try:
                return self.base_get_text(page.order_operation_fail)
            except Exception:
                return True
    #原生alert点击确认
    def page_alert_sure(self):
        self.driver.switch_to.alert.accept()
    # 点击主页面
    def page_click_home(self):
        self.base_click(page.order_go_home)
    # 给异常弹出框点击确定
    def page_click_sure(self):
        self.base_click(page.order_sure)
        sleep(2)
    #关闭ifram
    def page_close_iframe(self):
        self.base_click(page.order_close_iframe)
    # 组合业务方法
    def page_order(self,recipient,tel,text,address_detail,postal_code):
        # self.page_click_my_car()
        # self.page_click_check_out()
        # self.page_click_add_address()
        self.page_iframe()
        self.page_input_recipient(recipient)
        # 重置地址选择（设为默认状态）
        self.page_reset_address()
        if text and len(text) >=3:
            self.page_switch_Province(text[0])
            self.page_switch_city(text[1])
            self.page_switch_district(text[2])
        self.page_input_address_detail(address_detail)
        self.page_input_postal_code(postal_code)
        self.page_input_tel(tel)
        self.page_click_save()