import unittest
from time import sleep

from parameterized import parameterized

from tpshop_auto_test.base.base import Base
from tpshop_auto_test.base.get_driver import GetDriver
from tpshop_auto_test.base.get_logger import GetLogger
from tpshop_auto_test.page.page_login import PageLogin
from tpshop_auto_test.tool.read_json import read_json

log=GetLogger.get_logger()
def get_data():
    data_list=[]
    # JSON是列表，直接遍历
    for data in read_json("login.json"):
        data_list.append([
            data.get("username"),
            data.get("pwd"),
            data.get("code"),
            data.get("expect_result"),
            data.get("success")
        ])
    return data_list

# 新建测试类 并 继承
class Test01_Login(unittest.TestCase):
    login=None
    Base=None
    # setup
    @classmethod
    def setUpClass(cls):
            cls.login=PageLogin(GetDriver().get_driver())
            cls.Base=Base(GetDriver().get_driver())
            #点击登录链接
            cls.login.page_click_login_link()
    # tearDown
    @classmethod
    def tearDownClass(cls):
        pass
        # 关闭 driver驱动对象
        cls.login.driver.quit()
    # 登录测试方法
    @parameterized.expand(get_data())
    def test_login(self,username,pwd,code,expect_result,success):
        try:
            # 调用登录方法
            self.login.page_login(username,pwd,code)
            if success:
                #判断是否登录成功
                msg=self.login.page_is_login_success()
                print(f"断言前：msg={msg},expect_result={expect_result}")
                self.assertEqual(msg,expect_result)
                #安全退出
                self.Base.base_click_logout()
                #判断是否退出成功
                if not self.login.page_is_logout_success():
                    self.Base.base_get_image()
                    raise AssertionError("安全退出失败")
                #重新进入登录页
                self.login.page_click_login_link()
            else:
                #等待弹窗加载完成
                sleep(1)
                #获取异常提示信息
                msg=self.login.page_get_error_info()
                print(f"断言前：msg={msg},expect_result={expect_result}")
                self.assertEqual(msg,expect_result)
                #点击异常信息框 确定
                self.login.page_click_err_btn_ok()
        except Exception as e:
            log.error(e)
            self.Base.base_get_image()
            #分支恢复操作
            self.login.page_click_err_btn_ok()
            raise


