import time
from selenium import webdriver
from selenium.webdriver.ie.options import Options
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup

def start_crawring():
# chromedriver
    options = webdriver.ChromeOptions()
    # options.add_argument('headless')
    options.add_argument('window-size=1920x1080')
    # options.add_argument("disable-gpu")
    driver = webdriver.Chrome(options=options)

    # url = 'https://www.patent.go.kr/smart/jsp/kiponet/ma/mamarkapply/infomodifypatent/ReadMyPatApplInfo.do'
    url = 'https://m.khan.co.kr/english/articles'
    driver.get(url)
    driver.implicitly_wait(2)
    
    #bs4 초기화
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    news_list = soup.select('div.content div.latest_list_type > ul.list > li > div.cont')
    
    result = ''
    for news in news_list:
        name = news.select_one('a.tit').text.strip()
        # datetime = news.select_one('span.datetime').text.strip()        
        result += name

    driver.close()

    return result