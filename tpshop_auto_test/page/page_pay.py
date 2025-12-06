from time import sleep

from tpshop_auto_test import page
from tpshop_auto_test.base.base import Base


class PagePay(Base):
    # 点击我的订单
    def page_click_myorder(self):
        self.base_click(page.pay_myorder)
    # 切换到我的订单窗口
    # def page_switch_myorder_window(self):
    #     current_handle=self.driver.current_window_handle
    #     handles=self.driver.window_handles
    #     for h in handles:
    #         if h!=current_handle:
    #             self.driver.switch_to.window()
    # 点击待付款
    def page_clcik_Pending_payment(self):
        self.base_click(page.pay_pending_payment)
    # 点击立即支付
    def page_click_Pay_immediately(self):
        self.base_click(page.pay_pay_immediately)
    # 切换到订单支付窗口
    # def page_switch_order_pay(self):
    # 选择货到付款
    def page_click_cash_on_delivery(self):
        self.base_click(page.pay_cash_on_delivery)
    # 点击 确认支付方式
    def page_click_confirm_the_payment_method(self):
        self.base_click(page.pay_confirm_the_payment_method)
        sleep(2)
    # 返回主页
    def go_home(self):
        self.base_click(page.home)
    # 判断是否支付成功
    def page_is_pay_success(self):
        return self.base_get_text(page.pay_pay_success)
    # 鼠标悬停到我的订单
    def page_mouse_sky(self):
        self.base_mouse_sky(page.pay_mouse_sky)
    # 组合业务方法
    def page_pay(self):
        self.page_click_myorder()
        self.base_switch_window()
        self.page_clcik_Pending_payment()
        self.page_click_Pay_immediately()
        self.base_switch_window()
        self.page_click_cash_on_delivery()
        self.page_click_confirm_the_payment_method()





