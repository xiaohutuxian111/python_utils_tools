"""
@FileName：pytest特性.py
@Author：stone
@Time：2023/4/3 11:05
@Description：Allure报告支持的一些常见Pytest特性，包括xfails、fixture和finalizers、marks、条件跳过和参数化。
"""

import allure
import pytest


@allure.feature('test_xfail_expected_failure')
@pytest.mark.xfail(reason='该功能尚未尚未实现')
def test_xfail_expected_failure():
    print("该功能尚未实现")
    assert False




@allure.feature("test_xfail_unexpected_pass")
@pytest.mark.xfail(reason='该bug尚未修复')
def  test_xfail_unexpected_pass():
    print("该bug尚未修复")
    assert True



if __name__ == '__main__':
    pytest.main(['-s', '-q','pytest特性.py','--clean-alluredir','--alluredir=allure-results'])
    os.system(r"allure generate -c -o allure-report")
