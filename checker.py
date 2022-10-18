from lib2to3.pgen2 import driver
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
import time

browser = webdriver.Chrome('./chromedriver')
print('----------Start---------')

#赤坂ーーーーーーーーーーーーーーーーーーーーーー
store = 'エスパス赤坂見附: '

browser.get('https://daidata.goraggio.com/100952/accept')
browser.find_element(By.XPATH, '//*[@id="Result-Column"]/div/nav/ul/li[2]/form/span/button').click()
browser.find_element(By.XPATH, '//*[@id="gn_interstitial_close_icon"]').click()

#大海４SPーーーーーーーーーーーーーーーーーーーーーーーーー
try:
    kishu = '大海4SP: '
    browser.find_element(By.XPATH, '//*[@id="Prime-Column"]/nav[2]/form[1]/dl/dt/input').send_keys('大海物語4SP')
    browser.find_element(By.XPATH, '//*[@id="Prime-Column"]/nav[2]/form[1]/dl/dd/button').click()
    browser.find_element(By.XPATH, '//*[@id="Prime-Column"]/article/section/ul/li/a').click()
except NoSuchElementException: 
    nothing = 'nothing'

try:
    for i in range (1, 999):
        xp1 = '//*[@id="Prime-Column"]/article/table/tbody/tr['+str(i)+']/td[2]'
        n1 = browser.find_element(By.XPATH, xp1).text
        xp2 = '//*[@id="Prime-Column"]/article/table/tbody/tr['+ str(i) +']/td[10]'
        k1 = browser.find_element(By.XPATH, xp2).text

        if int(k1) > 630:
            print(store+kishu+n1+': '+k1)
        i = i + 1
except NoSuchElementException:
    nothing = 'nothing'


#乃木坂ーーーーーーーーーーーーーーーーーーーーーーーーー
try:
    kishu = '乃木坂: '
    browser.find_element(By.XPATH, '//*[@id="Second-Column"]/nav[3]/form[1]/dl/dt/input').send_keys('乃木坂')
    browser.find_element(By.XPATH, '//*[@id="Second-Column"]/nav[3]/form[1]/dl/dd/button').click()
    browser.find_element(By.XPATH, '//*[@id="Prime-Column"]/article/section/ul/li/a').click()
except NoSuchElementException: 
    nothing = 'nothing'
    
try:
    for i in range (1, 999):
        xp1 = '//*[@id="Prime-Column"]/article/table/tbody/tr['+str(i)+']/td[2]'
        n1 = browser.find_element(By.XPATH, xp1).text
        xp2 = '//*[@id="Prime-Column"]/article/table/tbody/tr['+ str(i) +']/td[10]'
        k1 = browser.find_element(By.XPATH, xp2).text

        if int(k1) > 370:
            print(store+kishu+n1+': '+k1)
        i = i + 1
except NoSuchElementException:
    nothing = 'nothing'


#禁書ミドルーーーーーーーーーーーーーーーーーーーーーーーーー
try:
    kishu = '禁書ミドル: '
    browser.find_element(By.XPATH, '//*[@id="Second-Column"]/nav[3]/form[1]/dl/dt/input').send_keys('JUA')
    browser.find_element(By.XPATH, '//*[@id="Second-Column"]/nav[3]/form[1]/dl/dd/button').click()
    browser.find_element(By.XPATH, '//*[@id="Prime-Column"]/article/section/ul/li/a').click()
except NoSuchElementException: 
    nothing = 'nothing'
    
try:
    for i in range (1, 999):
        xp1 = '//*[@id="Prime-Column"]/article/table/tbody/tr['+str(i)+']/td[2]'
        n1 = browser.find_element(By.XPATH, xp1).text
        xp2 = '//*[@id="Prime-Column"]/article/table/tbody/tr['+ str(i) +']/td[10]'
        k1 = browser.find_element(By.XPATH, xp2).text

        if int(k1) > 480:
            print(store+kishu+n1+': '+k1)
        i = i + 1
except NoSuchElementException:
    nothing = 'nothing'


#禁書ライトーーーーーーーーーーーーーーーーーーーーーーーーー
try:
    kishu = '禁書ライト: '
    browser.find_element(By.XPATH, '//*[@id="Second-Column"]/nav[3]/form[1]/dl/dt/input').send_keys('JRB')
    browser.find_element(By.XPATH, '//*[@id="Second-Column"]/nav[3]/form[1]/dl/dd/button').click()
    browser.find_element(By.XPATH, '//*[@id="Prime-Column"]/article/section/ul/li/a').click()
except NoSuchElementException: 
    nothing = 'nothing'
    
try:
    for i in range (1, 999):
        xp1 = '//*[@id="Prime-Column"]/article/table/tbody/tr['+str(i)+']/td[2]'
        n1 = browser.find_element(By.XPATH, xp1).text
        xp2 = '//*[@id="Prime-Column"]/article/table/tbody/tr['+ str(i) +']/td[10]'
        k1 = browser.find_element(By.XPATH, xp2).text

        if int(k1) > 240:
            print(store+kishu+n1+': '+k1)
        i = i + 1
except NoSuchElementException:
    nothing = 'nothing'

#デビルマンライトーーーーーーーーーーーーーーーーーーーーーーーーー
try:
    kishu = 'デビルマンライト: '
    browser.find_element(By.XPATH, '//*[@id="Second-Column"]/nav[3]/form[1]/dl/dt/input').send_keys('デビルマン N2-X1')
    browser.find_element(By.XPATH, '//*[@id="Second-Column"]/nav[3]/form[1]/dl/dd/button').click()
    browser.find_element(By.XPATH, '//*[@id="Prime-Column"]/article/section/ul/li/a').click()
except NoSuchElementException: 
    nothing = 'nothing'
    
try:
    for i in range (1, 999):
        xp1 = '//*[@id="Prime-Column"]/article/table/tbody/tr['+str(i)+']/td[2]'
        n1 = browser.find_element(By.XPATH, xp1).text
        xp2 = '//*[@id="Prime-Column"]/article/table/tbody/tr['+ str(i) +']/td[10]'
        k1 = browser.find_element(By.XPATH, xp2).text

        if int(k1) > 360:
            print(store+kishu+n1+': '+k1)
        i = i + 1
except NoSuchElementException:
    nothing = 'nothing'


#シンフォ２　７７ーーーーーーーーーーーーーーーーーーーーーーーーー
try:
    kishu = 'シンフォ2 77: '
    browser.find_element(By.XPATH, '//*[@id="Second-Column"]/nav[3]/form[1]/dl/dt/input').send_keys('2 yr')
    browser.find_element(By.XPATH, '//*[@id="Second-Column"]/nav[3]/form[1]/dl/dd/button').click()
    browser.find_element(By.XPATH, '//*[@id="Prime-Column"]/article/section/ul/li/a').click()
except NoSuchElementException: 
    nothing = 'nothing'
    
try:
    for i in range (1, 999):
        xp1 = '//*[@id="Prime-Column"]/article/table/tbody/tr['+str(i)+']/td[2]'
        n1 = browser.find_element(By.XPATH, xp1).text
        xp2 = '//*[@id="Prime-Column"]/article/table/tbody/tr['+ str(i) +']/td[10]'
        k1 = browser.find_element(By.XPATH, xp2).text

        if int(k1) > 150:
            print(store+kishu+n1+': '+k1)
        i = i + 1
except NoSuchElementException:
    nothing = 'nothing'

#せかつよーーーーーーーーーーーーーーーーーーーーーーーーー
try:
    kishu = 'せかつよ: '
    browser.find_element(By.XPATH, '//*[@id="Second-Column"]/nav[3]/form[1]/dl/dt/input').send_keys('RHY')
    browser.find_element(By.XPATH, '//*[@id="Second-Column"]/nav[3]/form[1]/dl/dd/button').click()
    browser.find_element(By.XPATH, '//*[@id="Prime-Column"]/article/section/ul/li/a').click()
except NoSuchElementException: 
    nothing = 'nothing'
    
try:
    for i in range (1, 999):
        xp1 = '//*[@id="Prime-Column"]/article/table/tbody/tr['+str(i)+']/td[2]'
        n1 = browser.find_element(By.XPATH, xp1).text
        xp2 = '//*[@id="Prime-Column"]/article/table/tbody/tr['+ str(i) +']/td[10]'
        k1 = browser.find_element(By.XPATH, xp2).text

        if int(k1) > 300:
            print(store+kishu+n1+': '+k1)
        i = i + 1
except NoSuchElementException:
    nothing = 'nothing'


#アリア　ライトーーーーーーーーーーーーーーーーーーーーーーーーー
try:
    kishu = 'アリア　ライト: '
    browser.find_element(By.XPATH, '//*[@id="Second-Column"]/nav[3]/form[1]/dl/dt/input').send_keys('FVA')
    browser.find_element(By.XPATH, '//*[@id="Second-Column"]/nav[3]/form[1]/dl/dd/button').click()
    browser.find_element(By.XPATH, '//*[@id="Prime-Column"]/article/section/ul/li/a').click()
except NoSuchElementException: 
    nothing = 'nothing'
    
try:
    for i in range (1, 999):
        xp1 = '//*[@id="Prime-Column"]/article/table/tbody/tr['+str(i)+']/td[2]'
        n1 = browser.find_element(By.XPATH, xp1).text
        xp2 = '//*[@id="Prime-Column"]/article/table/tbody/tr['+ str(i) +']/td[10]'
        k1 = browser.find_element(By.XPATH, xp2).text

        if int(k1) > 300:
            print(store+kishu+n1+': '+k1)
        i = i + 1
except NoSuchElementException:
    nothing = 'nothing'



print('-----------End----------')
