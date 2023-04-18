"""
@FileName：web_filter.py
@Author：stone
@Time：2023/4/5 8:06
@Description:
"""
import requests


from lxml import etree
from selenium import webdriver


def red_txt():
    file_path = './website.txt'
    try:
        f = open(file_path, encoding='utf-8')
    except  Exception as e:
        return None
    else:
        lis = f.readlines()
        f.close()
        return lis



def  open_web_and_get_source(url):
    driver =  webdriver.Firefox()
    page = driver.get(url)
    print(driver.page_source)












if __name__ == '__main__':
    # print(red_txt())
    open_web_and_get_source('http://www.baidu..com/')
