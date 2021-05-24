import unittest
from BeautifulReport import BeautifulReport


def testBeautifulReport(testCase, reportTitle, testMsg):  # 无法发送到邮件
    """
    :param testCase: 测试用例名称
    :param reportTitle:  测试报告标题
    :param testMsg:  测试用例说明
    :param report_dir:  测试报告存放位置
    """

    suite_tests = unittest.defaultTestLoader.discover(".", pattern=testCase, top_level_dir=None)
    BeautifulReport(suite_tests).report(filename=reportTitle, description=testMsg, report_dir='.')

    return


if __name__ == '__main__':
    # 生成测试报告
    testBeautifulReport("nhykt.py", "report", "南海云课堂管理后台回归流程测试")