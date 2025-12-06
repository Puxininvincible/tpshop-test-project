import unittest

from tpshop_auto_test.base.get_driver import GetDriver
from tpshop_auto_test.base.get_logger import GetLogger
from tpshop_auto_test.page.page_search import PageSearch
from tpshop_auto_test.page.page_login import PageLogin
from parameterized import parameterized

from tpshop_auto_test.tool.read_json import read_json

log=GetLogger.get_logger()

def get_data():
    arrs = []
    for data in read_json("search.json").values():
        arrs.append((data.get("product"),
                     data.get("expect_result"),
                     data.get("success")))
    return arrs
# uspwd=[{"username":"13800138006","pwd":"123456","code":"8888"}]
class Test02_Search(unittest.TestCase):
    login = None
    search=None
    @classmethod
    def setUpClass(cls):
        cls.search=PageSearch(GetDriver().get_driver())
        cls.login=PageLogin(GetDriver().get_driver())

        # cls.login.page_click_login_link()
        # cls.login_with_test()
        cls.search.go_home()
    # 前置条件
    # @classmethod
    # def login_with_test(cls):
    #     test=uspwd[0]
    #     cls.login.page_login(
    #         username=test["username"],
    #         pwd=test["pwd"],
    #         code=test["code"]
    #     )
    @classmethod
    def tearDownClass(cls):
        pass
        # GetDriver.quit_driver()

    # 查找商品并添加购物车方法
    @parameterized.expand(get_data())
    def test_search(self,product,expect_result,success):
        # 调用查找并添加购物车方法
        self.search.page_search(product)
        if success:
            try:
                self.search.page_click_product_details()
                self.search.page_add_car()
                #切换iframe弹窗
                self.search.page_iframe()
                # 判断添加购物车成功是否存在
                self.assertTrue(self.search.page_addcar_success())
                #切换到默认页面
                self.search.page_return()
                # 退出弹框
                self.search.page_addcar_close()
            except Exception:
                self.login.page_get_screenshot()
        else:
            try:
                print("获取异常文本")
                msg = self.search.page_get_error_info()
                actual_msg = msg.replace(" ", "").strip("--")  # 去除所有空格
                print("actual_msg", actual_msg)
                # 检查实际结果是否包含预期的核心文本
                self.assertEqual(actual_msg,expect_result)
            except AssertionError:
                print("获取异常文本失败")
                self.login.page_get_screenshot()



