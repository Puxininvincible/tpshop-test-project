import unittest
from tpshop_auto_test.base.get_driver import GetDriver
from tpshop_auto_test.base.get_logger import GetLogger
from tpshop_auto_test.page.page_login import PageLogin
from tpshop_auto_test.page.page_order import PageOrder
from tpshop_auto_test.page.page_pay import PagePay
from parameterized import parameterized

from tpshop_auto_test.page.page_search import PageSearch
from tpshop_auto_test.tool.read_json import read_json

log=GetLogger.get_logger()

def get_data():
    arrs = []
    for data in read_json("pay.json").values():
        arrs.append((data.get("success"),
                    data.get("expect_result")))
    return arrs

# uspwd=[{"username":"13800138006","pwd":"123456","code":"8888"}]
# product="iphone 6"
# address=[("彭于晏","15270614173",["江西省","南昌市","市辖区"],"江西交通职业技术学院","330000")]
class Test04_Pay(unittest.TestCase):
    login = None
    search=None
    order=None
    pay=None
    @classmethod
    def setUpClass(cls):
        #实例化页面对象
        cls.login = PageLogin(GetDriver().get_driver())
        cls.search = PageSearch(GetDriver().get_driver())
        cls.order=PageOrder(GetDriver().get_driver())
        cls.pay=PagePay(GetDriver().get_driver())
        # """前置条件"""
        # #登录
        # cls.login.page_click_login_link()
        # cls.login_with_test()
        # #查找商品并添加购物车
        # cls.pay.go_home()
        # cls.find_product()
        # cls.search.page_click_product_details()
        # cls.search.page_add_car()
        # cls.search.page_addcar_close()
        # # 点击我的购物车 点击去结算 点击新增收货地址
        # cls.order.page_click_my_car()
        # cls.order.page_click_check_out()
        # cls.order.page_click_add_address()
        # cls.order_with_test()
        # 直接关闭弹窗切换到操作页面
        cls.order.page_close_iframe()
        cls.pay.page_mouse_sky()
    # @classmethod
    # def find_product(cls):
    #    cls.search.page_search(product)
    # @classmethod
    # def login_with_test(cls):
    #     test = uspwd[0]
    #     cls.login.page_login(
    #         username=test["username"],
    #         pwd=test["pwd"],
    #         code=test["code"]
    #     )

    # @classmethod
    # def order_with_test(cls):
    #     test=address[0]
    #     cls.order.page_order(
    #         recipient=test[0],  # 索引0：收件人
    #         tel=test[1],  # 索引1：电话
    #         text=test[2],  # 索引2：省市区（列表类型，符合参数要求）
    #         address_detail=test[3],  # 索引3：详细地址
    #         postal_code=test[4],  # 索引4：邮编
    #     )



    @classmethod
    def tearDownClass(cls):
        GetDriver.quit_driver()

    @parameterized.expand(get_data())
    def test_pay(self,success,expect_result):
        self.pay.page_pay()
        if success:
            try:
                print("开始获取支付成功信息")
                msg=self.pay.page_is_pay_success()
                print("msg:",msg)
                self.assertEqual(msg,expect_result)
            except Exception as e:
                print(f"获取支付信息失败！异常原因：{str(e)}")
                self.login.page_get_screenshot()
        else:
            self.login.page_get_screenshot()
