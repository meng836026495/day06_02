# 导包
import unittest


# 创建套件对象
from tools.HTMLTestReportCN import HTMLTestRunner

suite = unittest.defaultTestLoader.discover('./scipts')


# 调用run方法
with open('./report/report.html','wb')as f:
    HTMLTestRunner(stream=f).run(suite)