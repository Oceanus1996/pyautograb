import random

import driver
import pyautogui
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.wait import WebDriverWait


#模拟登录
def logIn(driver):
    # 等待
    time.sleep(random.uniform(2, 5))
    # 点击log in
    login_button = driver.find_element(By.CSS_SELECTOR, "button[data-testid='login-button']")
    login_button.click()
    # 进入登录2界面，输入账号
    time.sleep(random.uniform(2, 5))
    # username = driver.find_element(By.ID, "username")
    # username.send_keys('857863394@qq.com')

#获取位置
def detect():
    time.sleep(5)
    return pyautogui.position()

if __name__=="__main__":
    # #增加访问
    # options = Options()
    # options.add_argument('--disable-blink-features=AutomationControlled')
    # driver = webdriver.Chrome(options=options)
    #
    # # 显时等待
    # # WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.ID, "myElement")))
    #
    # #禁用自动化标志
    # options.add_experimental_option("excludeSwitches", ["enable-automation"])
    # options.add_experimental_option('useAutomationExtension', False)
    # # 这次尝试打开 chat主页
    # # 这次尝试打开 chat主页
    # #headless
    # options.add_argument('--headless')
    #
    # from selenium import webdriver
    #
    # # 创建 WebDriver 实例
    # driver = webdriver.Chrome()
    # driver.get("https://chat.openai.com/")  # 访问 ChatGPT
    #
    # # 添加 Cookie
    # driver.add_cookie({
    #     'name': '__Host-next-auth.csrf-token',
    #     'value': '2577e97a1d896e848bb01635cd3bc32b76dacfff2e0214199503e215c6762893%7Cb0a42872172ddd9cdf4f350164d5484f4893105ab53a219b4c0a1d9f10672ee9',
    #     'domain': 'chat.openai.com',
    #     'path': '/',
    #     'secure': True,
    #     'httpOnly': True  # 根据实际情况设置
    # })
    # # 根据您的其他 Cookie 重复以上步骤
    #
    # # 重新加载网站以应用 Cookie
    # driver.get("https://chat.openai.com/")
    #
    # # driver.get("https://www.google.co.uk/")
    # # driver.get("https://chat.openai.com/")
    # # # driver.get('https://www.csdn.net/?spm=1018.2226.3001.4476&ydreferer=aHR0cHM6Ly9zby5jc2RuLm5ldC9zby9zZWFyY2g%2FcT0lRTUlOEYlOEQlRTclODglQUMlRTglOTklQUImdD0mdT0mdXJ3PQ%3D%3D')
    # # input("登录好了再继续")
    # # print("登录好了")

    # time.sleep(5)
    # print(pyautogui.position(),'plugins button1')
    # pyautogui.moveTo(558,141)
    # pyautogui.click()
    # time.sleep(2)
    # pyautogui.moveTo(555,182)
    # pyautogui.click()
    # time.sleep(2)
    for i in range(8):
        print(i,detect())






