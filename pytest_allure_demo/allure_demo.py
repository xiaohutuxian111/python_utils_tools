"""
@FileName：allure_demo.py
@Author：stone
@Time：2023/4/3 10:01
@Description：
"""
import os

import pytest
import allure


@allure.feature("test_success")
def test_success():
    """this  test success"""
    assert True


@allure.feature("test_fail")
def test_fail():
    """this test fails"""
    assert False


@allure.feature("test skip")
def test_skip():
    """this test is skipped"""
    pytest.skip("for a reason")


@allure.feature("test_broken")
def test_broken():
    raise Exception('oops')


if __name__ == '__main__':
    pytest.main(['-s', '-q','test_allure02.py','--clean-alluredir','--alluredir="./"'])
    os.system(r"allure generate -c -o allure-reports")