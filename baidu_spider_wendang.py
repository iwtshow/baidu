#!/usr/bin/env python
# -*- coding: utf-8 -*-

from selenium import webdriver#驱动服务器
from selenium.webdriver.common.keys import Keys
import time
from lxml import etree#解析文本
import re#正则

def main():
    browser = webdriver.Firefox()#选择驱动的浏览器
    browser.get('https://wenku.baidu.com/view/fbdc423a3968011ca30091f0.html')
    browser.set_window_size(1024, 6000)#浏览器窗口大小
    #继续阅读，继续加载
    elem = browser.find_element_by_xpath("/html/body/div[6]/div[2]/div/div/div[2]/div[1]/div/div[2]/div[2]/div[1]/div[6]/div[2]/div[1]/span")
    elem.click()#点击继续加载按钮
    f = open("pid_data.txt", "w", encoding="utf-8")#如果用with  效果可能更好
    #with  open  打开文件  省去了我们关闭文件的操作
    for i in range(2, 83):
            print(i)
            elem = browser.find_elements_by_css_selector("input.page-input")#页码输入框
            elem[0].clear()#清零
            elem[0].send_keys(str(i), Keys.RETURN)#输入当前页
            time.sleep(10)#等待10  模拟人为操作
            page = str(browser.page_source)
            root = etree.HTML(page)#规范H5元素
            p_list = root.xpath("//div[@id='pageNo-%d']//p" % i)
            cnt = 1

            for p in p_list:
                if len(p.text) == 1 or len(p.text) == 2:
                    continue

                if "，" in p.text:
                    continue

                if re.match("\d{6}", p.text):
                    p.text = p.text[0:6]

                if re.fullmatch("\d{6}", p.text) == None and "省" not in p.text and "市" not in p.text and "区" not in p.text and "县" not in p.text:
                    continue

                print(p.text)

                if cnt % 2 != 0:#前面面写的是区域编码，后面写的是地区名字
                    f.write(p.text)
                else:
                    f.write(" " + p.text + "\n")
                cnt += 1
                f.flush()#刷新当前网页
    f.close()#关闭文件
    # with open("test.html", "w", encoding="utf-8") as f:
    #     f.write(page)
    # page = browser.find_elements_by_css_selector("#pageNo-2")
if __name__ == '__main__':
    main()
