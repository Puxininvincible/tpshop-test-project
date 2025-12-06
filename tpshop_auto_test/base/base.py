import time

from selenium.webdriver import ActionChains
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

from tpshop_auto_test import page
from tpshop_auto_test.base.get_logger import GetLogger

log=GetLogger.get_logger()
class Base:
    def __init__(self,driver):
        log.info("初始化driver{}".format(driver))
        self.driver=driver

    # 查找元素方法 封装
    def base_find(self,loc,timeout=4,poll=0.5):
        log.info("正在查找元素：{}".format(loc))
        #使用显示等待 查找元素
        return WebDriverWait(self.driver,
                             timeout=timeout,
                            poll_frequency=poll).until(lambda x:x.find_element(*loc))

    # 点击元素 方法封装
    def base_click(self,loc):
        log.info("正在点击元素：{}".format(loc))
        self.base_find(loc).click()

    # 输入元素 方法封装
    def base_input(self,loc,value):
        log.info("正在给元素{}输入内容：{}".format(loc, value))
        # 获取元素
        el=self.base_find(loc)
        # 清空
        el.clear()
        log.info("正在给元素：{}清空".format(loc))
        # 输入
        el.send_keys(value)
        log.info("正在给元素：{}输入内容".format(value))

    # 获取文本信息 方法封装
    def base_get_text(self,loc):
        log.info("正在获取元素：{}文本".format(loc))
        return self.base_find(loc).text
    # 截图 方法封装
    def base_get_image(self):
        self.driver.get_screenshot_as_file("../image/{}.png".format(time.strftime("%Y_%m_%d %H_%M_%S")))

    # 判断元素是否存在 方法封装
    def base_element_is_exist(self,loc):
        try:
            self.base_find(loc,timeout=2)
            return True #代表元素存在
        except:
            # 没找到元素
            log.info("判断元素：{} 不存在!".format(loc))
            return False #代表元素不存在
    # 选择框
    def base_select(self,loc,text):
        Select(self.base_find(loc)).select_by_visible_text(text)

    # 选择下拉框的第一个选项
    def base_select_first(self, loc):
        Select(self.base_find(loc)).select_by_index(0)

    # 切换新窗口
    def base_switch_window(self):
        all_handles = self.driver.window_handles
        self.driver.switch_to.window(all_handles[-1])

    # 鼠标悬停
    def base_mouse_sky(self,loc):
        action = ActionChains(self.driver)
        action.move_to_element(self.driver.find_element(*loc)).perform()
    # 点击 安全退出
    def base_click_logout(self):
        self.base_click(page.logout)