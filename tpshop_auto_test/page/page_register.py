import time

from tpshop_auto_test import page
from tpshop_auto_test.base.base import Base


class PageRegister(Base):
    #点击注册链接
    def page_click_register_link(self):
        self.base_click(page.register_register_link)
    #输入手机号码
    def page_input_tel(self,tel):
        self.base_input(page.register_tel,tel)
    #输入图像验证码
    def page_input_verify_code(self,code):
        self.base_input(page.register_verify_code,code)
    #输入设置密码
    def page_input_set_pwd(self,set_pwd):
        self.base_input(page.register_set_pwd,set_pwd)
    #输入确认密码
    def page_input_confirm_pwd(self,confirm_pwd):
        self.base_input(page.register_confirm_pwd,confirm_pwd)
        time.sleep(0.5)
        # 处理输入密码或确认密码错误数据时点击下一填框出现错误信息
        try:
            self.page_get_register_err_info()
            self.page_close_register_err_info()
        except:
            pass
    #输入推荐人手机号
    def page_input_reference_tel(self,reference_tel):
        self.base_input(page.register_reference_tel,reference_tel)
        time.sleep(0.5)
        # 处理输入密码或确认密码错误数据时点击下一填框出现错误信息
        try:
            self.page_get_register_err_info()
            self.page_close_register_err_info()
        except:
            pass
    # #勾选协议(默认勾选，无需此方法)
    # def page_click_agreement(self):
    #     self.base_click(page.register_agreement)
    #点击同意协议并注册
    def page_click_register_btn(self):
        self.base_click(page.register_register_btn)
    #获取注册成功提示信息
    def page_get_register_success_tip(self):
        return self.base_get_text(page.register_register_success_tip)
    #获取失败提示弹窗信息
    def page_get_register_err_info(self):
        return self.base_get_text(page.register_err_info)
    #关闭失败提示弹窗
    def page_close_register_err_info(self):
        self.base_click(page.register_err_btn_ok)
    #点击邮箱注册
    def page_click_email_register(self):
        self.base_click(page.register_email_register_link)
    #判断是否注册成功，是否有安全退出
    def page_is_register_success(self):
        return self.base_element_is_exist(page.logout)
    #组合注册方法
    def page_register(self,tel,code,set_pwd,confirm_pwd,reference_tel):
        #输入手机号
        self.page_input_tel(tel)
        #输入验证码
        self.page_input_verify_code(code)
        #输入设置密码
        self.page_input_set_pwd(set_pwd)
        #输入确认密码
        self.page_input_confirm_pwd(confirm_pwd)
        #输入推荐人手机号
        self.page_input_reference_tel(reference_tel)
        #点击同意协议并注册
        self.page_click_register_btn()
        time.sleep(0.5)