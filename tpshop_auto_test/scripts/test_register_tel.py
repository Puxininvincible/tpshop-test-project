import unittest

from parameterized import parameterized

from tpshop_auto_test.base.base import Base, log
from tpshop_auto_test.base.get_driver import GetDriver
from tpshop_auto_test.config import PUBLIC_TELS
from tpshop_auto_test.page.page_register import PageRegister
from tpshop_auto_test.tool.db_utils import TPshopDB
from tpshop_auto_test.tool.read_json import read_json


def get_data():
    data_list=[]
    # JSON是列表，直接遍历
    for data in read_json("register_tel.json"):
        data_list.append([
            data.get("tel"),
            data.get("code"),
            data.get("set_pwd"),
            data.get("confirm_pwd"),
            data.get("reference_tel"),
            data.get("expect_result"),
            data.get("success")
        ])
    return data_list

class Test_Register(unittest.TestCase):
    driver=None
    register=None
    Base=None
    db=None
    @classmethod
    def setUpClass(cls):
        #初始化driver
        cls.driver=GetDriver.get_driver()
        #实例化获取页面对像
        cls.Base=Base(cls.driver)
        cls.register=PageRegister(cls.driver)
        #点击注册链接
        cls.register.page_click_register_link()
        #初始话数据库工具
        cls.db=TPshopDB()
    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
    @parameterized.expand(get_data())
    def test_register(self,tel,code,set_pwd,confirm_pwd,reference_tel,expect_result,success):
        try:
            # 执行注册操作
            self.register.page_register(tel,code,set_pwd,confirm_pwd,reference_tel)
            # 成功分支处理
            if success:
                msg=self.register.page_get_register_success_tip()
                print(f"断言前：msg={msg},expect_result={expect_result}")
                self.assertEqual(msg,expect_result)
                # 安全退出
                self.Base.base_click_logout()
                # 重新进入注册页
                self.register.page_click_register_link()
            # 失败分支处理
            else:
                msg=self.register.page_get_register_err_info()
                print(f"断言前：msg={msg},expect_result={expect_result}")
                self.assertEqual(msg,expect_result)
                self.register.page_close_register_err_info()
        except Exception as e:
            log.error(e)
            self.Base.base_get_image()
            #分支恢复操作
            if success:
                self.register.page_close_register_err_info()
            else:
                #判断安全退出是否存在
                if self.register.page_is_register_success():
                    # 安全退出
                    self.Base.base_click_logout()
                    # 重新进入注册页
                    self.register.page_click_register_link()
                else:
                    self.register.page_close_register_err_info()
            raise
        finally:
            if tel not in PUBLIC_TELS:
                self.db.delete_user_by_tel(tel)
            else:
                log.info(f"[保留] 公共手机号{tel}，不执行删除")










