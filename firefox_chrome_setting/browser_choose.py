"""
@FileName：browser_choose.py
@Author：stone
@Time：2023/4/1 11:22
@Description：
"""
from selenium import webdriver


def firefox_setting():
    options = webdriver.FirefoxOptions()
    profile = webdriver.FirefoxProfile()
    # ua = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36'
    # profile.set_preference("network.proxy.type", 4) #自动检测代理设置
    profile.set_preference("dom.webdriver.enabled", False)  # 设置非driver驱动
    profile.set_preference('useAutomationExtension', False)  # 关闭自动化提示
    profile.update_preferences()  # 更新设置
    driver = webdriver.Firefox(firefox_options=options, firefox_profile=profile)
    driver.maximize_window()
    return driver


def chrome_setting():
    # 加启动配置
    chrome_options = webdriver.ChromeOptions()
    # 此步骤很重要，设置为开发者模式，防止被各大网站识别出来使用了Selenium
    chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])  # 禁止打印日志
    chrome_options.add_experimental_option('excludeSwitches', ['enable-automation'])  # 实现了规避监测
    # chrome_options.add_experimental_option("excludeSwitches",['enable-automation','enable-logging'])#上面两个可以同时设置
    # chrome_options.add_argument('--headless')  # 无头模式
    # 关闭日志输出
    chrome_options.add_argument('--disable-gpu')  # 上面代码就是为了将Chrome不弹出界面
    chrome_options.add_argument('--start-maximized')  # 最大化
    # chrome_options.add_argument('--incognito')  # 无痕隐身模式
    # chrome_options.add_argument("disable-cache")  # 禁用缓存
    chrome_options.add_argument('disable-infobars')
    # chrome_options.add_argument('log-level=3')  # INFO = 0 WARNING = 1 LOG_ERROR = 2 LOG_FATAL = 3 default is 0
    driver = webdriver.Chrome(chrome_options=chrome_options)

    return driver


def select_browser(browser_name="firefox"):
    if browser_name == "firefox":
        return firefox_setting()
    else:
        return chrome_setting()

if __name__ == '__main__':
    pass
