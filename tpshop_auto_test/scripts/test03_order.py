import unittest

from tpshop_auto_test.base.get_driver import GetDriver
from tpshop_auto_test.base.get_logger import GetLogger
from tpshop_auto_test.page.page_login import PageLogin
from tpshop_auto_test.page.page_order import PageOrder
from tpshop_auto_test.page.page_search import PageSearch
from parameterized import parameterized

from tpshop_auto_test.tool.read_json import read_json

log=GetLogger.get_logger()
def get_data():
    arrs = []
    for data in read_json("order.json").values():
        arrs.append((data.get("recipient"),
                     data.get("tel"),
                     data.get("text"),
                     data.get("address_detail"),
                     data.get("postal_code"),
                     data.get("success"),
                     data.get("expect_result")))
    return arrs
# uspwd=[{"username":"13800138006","pwd":"123456","code":"8888"}]
# product="iphone 6"
class Test03_Order(unittest.TestCase):
    login = None
    search = None
    order=None

    @classmethod
    def setUpClass(cls):
        cls.order=PageOrder(GetDriver().get_driver())
        cls.login = PageLogin(GetDriver().get_driver())
        cls.search=PageSearch(GetDriver().get_driver())
        # cls.login.page_click_login_link()
        # cls.login_with_test()
        # cls.search.go_home()
        # 添加购物车
        # cls.find_product()
        # cls.search.page_click_product_details()
        # cls.search.page_add_car()
        # # 退出弹框
        # cls.search.page_addcar_close()
        # 点击我的购物车 点击去结算 点击新增收货地址
        cls.order.page_click_my_car()
        cls.order.page_click_check_out()
        cls.order.page_click_add_address()

    # 前置条件
    # 登录
    # @classmethod
    # def login_with_test(cls):
    #     test = uspwd[0]
    #     cls.login.page_login(
    #         username=test["username"],
    #         pwd=test["pwd"],
    #         code=test["code"]
    #     )
    # # 查找商品并添加购物车
    # @classmethod
    # def find_product(cls):
    #    cls.search.page_search(product)

    @classmethod
    def tearDownClass(cls):
        pass
        # GetDriver.quit_driver()
    @parameterized.expand(get_data())
    def test_order(self, recipient, tel, text, address_detail, postal_code,success,expect_result):
        self.order.page_order(recipient,tel,text,address_detail,postal_code)
        if success:
            try:
                self.order.page_return()
                print("开始执行成功场景：点击提交订单")
                self.order.page_click_submit()
                print("开始获取提交成功信息")
                msg=self.order.page_submit_success()
                print("msg:", msg)
                self.assertEqual(msg,expect_result)
                self.order.page_click_home()
                # 添加购物车
                self.search.page_search("iphone")
                self.search.page_click_product_details()
                self.search.page_add_car()
                # 退出弹框
                self.search.page_addcar_close()
                # 点击我的购物车 点击去结算 点击新增收货地址
                self.order.page_click_my_car()
                self.order.page_click_check_out()
                self.order.page_click_add_address()
            except Exception as e:
                print(f"test_order_5执行失败：{str(e)}")
                self.login.page_get_screenshot()
        else:
            msg=self.order.page_get_fail()
            print("msg:",msg)
            try:
                self.assertEqual(msg,expect_result)
                try:
                    print("尝试关闭原生 alert 弹窗")#优先
                    self.order.page_alert_sure()
                except Exception:
                    print("尝试关闭iframe弹窗")
                    self.order.page_click_sure()
                self.order.page_return()
            except AssertionError:
                self.login.page_get_screenshot()




