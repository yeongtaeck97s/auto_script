# main.py

import sys
import os
import time
from selenium.webdriver.common.keys import Keys

import chromedriver

# Headless
headless = False


# PATH = 'C:/Users/82105/Desktop/Data_Analysis/Python/Develop_Code'
# PROJECT_DIR = str(os.path.dirname(os.path.abspath(PATH)))
# DOWNLOAD_DIR = f'{PROJECT_DIR}/download'
# driver_path = f'{PROJECT_DIR}/lib/webDriver/'
PROJECT_DIR = os.getcwd()
DOWNLOAD_DIR = os.path.join(PROJECT_DIR,'download')
driver_path = os.path.join(PROJECT_DIR, 'lib/webDriver')


platform = sys.platform
if platform == 'darwin':
    print('System platform : Darwin')
    driver_path += 'chromedriver_mac'
elif platform == 'linux':
    print('System platform : Linux')
    driver_path += 'chromedriver_linux'
elif platform == 'win32':
    print('System platform : Window')
    driver_path = os.path.join(driver_path,'chromedriver_win.exe')
else:
    print(f'[{sys.platform}] not supported. Check your system platform.')
    raise Exception()

# 크롬 드라이버 인스턴스 생성
chrome = chromedriver.generate_chrome(
    driver_path=driver_path,
    headless=headless,
    download_path=DOWNLOAD_DIR)

# 페이지 요청
url = 'http://edu.kisti.re.kr/index.asp?beurl='
chrome.get(url)
chrome.implicitly_wait(30)
elm = chrome.find_element_by_id('login_id')
elm.send_keys('A202001789')
elm = chrome.find_element_by_id('login_pw')
elm.send_keys('505065')
time.sleep(2)
elm.send_keys(Keys.RETURN)

chrome.implicitly_wait(15)



while True:
    if int(time.strftime('%H%M', time.localtime(time.time()))) >= 1805:
        elm = chrome.find_element_by_xpath('//*[@id="content"]/div/div[2]/div[1]/div/div[2]/div/div/div[2]/a[2]')
        elm.click()
        time.sleep(5)
        break
    else:

        chrome.refresh()
        # main = chrome.window_handles
        # for handle in main:
        #     if handle != main[0]:
        #         chrome.switch_to_window(handle)
        #         chrome.close()
        # chrome.switch_to_window(chrome.window_handles[0])
        time.sleep(180)

# Login
# elm = chrome.find_element_by_id('login_field')
# elm.send_keys('ljkk1542@naver.com')
# elm = chrome.find_element_by_id('password')
# elm.send_keys('maroon3169!@')
# elm.send_keys(Keys.RETURN)
# time.sleep(3)
#
# # download
# url = 'https://github.com/yeongtaeck97s/auto_script'
# chrome.get(url)
# time.sleep(3)
#
# elm = chrome.find_element_by_xpath('//*[@id="js-repo-pjax-container"]/div[2]/div/div[2]/div[1]/div[2]/span/get-repo/details')
# elm.click()
#
# elm = chrome.find_element_by_xpath('//*[@id="js-repo-pjax-container"]/div[2]/div/div[2]/div[1]/div[2]/span/get-repo/details/div/div/div[1]/ul/li[2]')
# elm.click()
# time.sleep(15)
