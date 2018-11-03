from  selenium import webdriver
from  selenium.webdriver.common.by import By
from  selenium.webdriver.common.keys import Keys
from selenium.webdriver.support  import expected_conditions as   EC
from selenium.webdriver.support.wait import WebDriverWait
import time
browser = webdriver.Firefox()
browser.get('https://movie.douban.com/top250')
browser.find_element_by_xpath('//*[@id="inp-query"]').send_keys("刘德华")
browser.find_element_by_xpath('/html/body/div[2]/div[1]/div/div[2]/form/fieldset/div[2]/input').click()
url = browser.current_url
n= 1
m = 0
for i in range(1,17):
        # url ='https://movie.douban.com/subject_search?search_text=%E5%88%98%E5%BE%B7%E5%8D%8E&cat=1002&start='+str(i*15)
    browser.get(url+"&start="+str(i*15))
    for  i in range(3,18):
        try:
            x='/ html / body / div[3] / div[1] / div / div[2] / div[1] / div[1] / div['+str(i)+'] / div[1] / div / div[1] / a'
            # / html / body / div[3] / div[1] / div / div[2] / div[1] / div[1] / div[17] / div / div / div[1] / a
            print('第'+str(n)+'部电影 : '+browser.find_element_by_xpath(x).text)
            n +=1
        except:
      
            print("------------------------------------------------------------")
            m+=1
    time.sleep(3)
browser.close()
print("m=%d"%m)
# /html/body/div[3]/div[1]/div/div[2]/div[1]/div[1]/div[17]/div/div/div[1]/a
