import time
import unittest
from tpshop_auto_test.tool.HTMLTestRunner import HTMLTestRunner
#定义测试套件
suite=unittest.defaultTestLoader.discover("../scripts",pattern="test_register_email.py")
report_dir="../report/{}.html".format("邮箱注册测试")
with open(report_dir,"wb") as f:
    HTMLTestRunner(stream=f,
                   verbosity=2,
                   title="tpshop电商平台自动化测试报告",
                   description="""
                   操作系统：Windows 10
                   浏览器：Edge
                   Python版本：3.8
                   测试范围：邮箱注册
                   测试时间：{}
                   """.format(time.strftime("%Y-%m-%d %H:%M:%S"))
                   ).run(suite)