# coding=utf-8
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import os
import time

start = time.time()


def get_image(url, pic_name):
    # chromedriver的路径
    chromedriver = r"C:\Users\Admin\chromedriver_win32\chromedriver.exe"
    os.environ["webdriver.chrome.driver"] = chromedriver
    # 设置chrome开启的模式，headless就是无界面模式
    # 一定要使用这个模式，不然截不了全页面，只能截到你电脑的高度
    chrome_options = Options()
    chrome_options.add_argument('headless')
    driver = webdriver.Chrome(chromedriver, chrome_options=chrome_options)
    # 控制浏览器写入并转到链接
    # 这里的url因为我的文件是本地的html所以需要你需要动态的网页你自己编写一下
    driver.get(url)
    # time.sleep(1)
    # 接下来是全屏的关键，用js获取页面的宽高，如果有其他需要用js的部分也可以用这个方法
    width = driver.execute_script("return document.documentElement.scrollWidth")
    height = driver.execute_script("return document.documentElement.scrollHeight")
    print(width, height)
    # 将浏览器的宽高设置成刚刚获取的宽高
    driver.set_window_size(width, height)
    # time.sleep(1)
    # 截图并关掉浏览器
    driver.save_screenshot(pic_name)
    driver.close()


# 你输入的参数
path = os.getcwd()
# 获取所有文件名的列表
filename_list = os.listdir(path)
# 获取所有HTML文件名列表
htmlname_list = [filename for filename in filename_list \
                 if filename.endswith(".html")]
# print(wordname_list)
for htmlname in htmlname_list:
    # 分离html文件名称和后缀，转化为就jpg名称
    jpgname = os.path.splitext(htmlname)[0] + '.jpg'
    # 如果当前html文件对应的jpg文件存在，则不转化
    if jpgname in filename_list:
        continue
    # 拼接 路径和文件名
    htmlPath = os.path.join(path, htmlname)
    # print(htmlPath)
    pdfpath = os.path.join(path, jpgname)
    get_image(htmlPath, jpgname)
print('HTML---->jpg转换完成，花费时间：', time.time() - start)
