from time import sleep

from tpshop_auto_test import page
from tpshop_auto_test.base.base import Base


class PageSearch(Base):
    # 输入商品
    def page_input_product(self,product):
        self.base_input(page.search_input_box,product)
    # 点击搜索按键
    def page_click_search(self):
        self.base_click(page.search_search)
        sleep(2)
    # 点击商品详情页
    def page_click_product_details(self):
        self.base_click(page.search_Product_details)
    # 添加购物车
    def page_add_car(self):
        self.base_click(page.search_add_car)
        sleep(1)
    # 关闭弹窗
    def page_addcar_close(self):
        self.base_click(page.search_addcar_close)
        sleep(1)
    # 判断商品是否找到
    def page_search_success(self):
        return self.base_element_is_exist(page.search_Price_filter)
    # 判断是否添加购物车成功
    def page_addcar_success(self):
        try:
            # print("开始获取添加成功文本...")
            success_text = self.base_get_text(page.search_addcar_success)
            # print(f"实际获取到的文本: '{success_text}'")
            result = "添加成功" in success_text
            # print(f"判断结果: {result}")
            return result
        except Exception as e:
            # print(f"获取文本时出现异常: {e}")
            return False
    #获取异常提示信息
    def page_get_error_info(self):
        try:
            return self.base_get_text(page.search_err2)
        except Exception:
            try:
                return self.base_get_text(page.search_err)
            except Exception:
                return ""
    # #截图
    # def page_get_screenshot(self):
    #     self.base_get_image()
    # 返回主页
    def go_home(self):
        self.base_click(page.home)
    #切换iframe弹窗
    def page_iframe(self):
        self.driver.switch_to.frame(page.search_iframe_id)
    #切换到默认页面
    def page_return(self):
        self.driver.switch_to.default_content()
    #组合业务方法
    def page_search(self,product):
        self.page_input_product(product)
        self.page_click_search()

