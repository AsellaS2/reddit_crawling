from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import pandas as pd
import time

links_df = pd.read_csv('E:/python_project/reddit/1년데이터레딧주소/Harvard_total.csv',encoding='mac_roman')
links = links_df['0'].tolist() #링크로 되어있는 것을 리스트화 시켜주어라.



driver = webdriver.Chrome(executable_path="./chromedriver.exe")
titles = []
bodies = []


for link in links:
      driver.get(link)
      html = driver.page_source
      soup = BeautifulSoup(html, 'html.parser')
      time.sleep(1.0)
      try:
            title = soup.select('._eYtD2XCVieq6emjKBH3m')[0].text
            body = soup.select('._3xX726aBn29LDbsDtzr_6E._1Ap4F5maDtT1E1YuCiaO0r.D3IL3FD0RFy_mkKLPwL4 > div > ._1qeIAgB0cPwnLhDF9XSiJM')
            titles.append(title)
            bodies.append(body)
      except IndexError:
            df = pd.DataFrame({'title': titles, 'contents': bodies}, columns=['title', 'contents'])
            df.to_csv('E:/python_project/reddit/1년데이터레딧본문/Harvard_contents.csv', index=False, encoding='utf-16')
            body = 'Na'




driver.quit()


df = pd.DataFrame({'title':titles,'contents':bodies}, columns=['title','contents'])
df.to_csv('E:/python_project/reddit/1년데이터레딧본문/Harvard_contents_context.csv', index=False, encoding='utf-16')
