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
df.to_csv('E:/python_project/reddit/1년데이터레딧본문/Harvard_contents(test).csv', index=False, encoding='utf-16')


#data = pd.read_csv('E:/python_project/reddit/1년데이터레딧본문/dartmouth_contents.csv', encoding='utf-16')

#data.to_csv('E:/python_project/reddit/1년데이터레딧본문/dartmouth_contents.csv',encoding='utf-8',index=False)

#
# titles = []
# bodies = []
#
# try
#       for link in links['0']:
#             print(link)
#             # driver = webdriver.Chrome(executable_path="E:/python_project/correlation/chromedriver.exe")
#             # driver.get(link)
#             # html = driver.page_source
#             # soup = BeautifulSoup(html, 'html.parser')
#             # title = soup.select('._eYtD2XCVieq6emjKBH3m')[0].text
#             # titles.append(title)
#             # body = soup.select('._1qeIAgB0cPwnLhDF9XSiJM')[1].text
#             # bodies.append(body)
#             # driver.quit()
# except IndexError :
#       pass
#
# all_titles = pd.DataFrame(titles, columns=['title'])
# all_bodies = pd.DataFrame(bodies, columns=['body'])
#
#
# harvard_contnents = all_titles.merge(all_bodies,left_on='title',right_on='body')
# print(harvard_contnents)

# harvard_contnents.to_csv('./harvard_contnents.csv',index=False, encoding='utf-8')

# from selenium import webdriver as wd
# import time
# import selenium.webdriver.common.keys
# import keys
# from bs4 import BeautifulSoup
# import pandas as pd
#
# from bs4 import BeautifulSoup
#
# import pandas as pd
#
# import requests
#
# links = pd.read_csv(r'C:/Users/dfgry/OneDrive/바탕 화면/reddit_url/레딧코드/해외대학주소/harvard_url.csv')
#
#
# for link in links['0']:
#     driver = webdriver.Chrom(excutable_path='./chromedriver.exe')
#     driver.get(link)
#
#     html = driver.page_source
#     soup = BeautifulSoup(html, 'html.parser')
#     title = soup.select('._eYtD2XCVieq6emjKBH3m')[0].text
#     body = soup.select('._3xX726aBn29LDbsDtzr_6E _1Ap4F5maDtT1E1YuCiaO0r D3IL3FD0RFy_mkKLPwL4')[0].text
#
#     print(title,body)
#     driver.quit()


 # url = requests.get(link)
 #    html = url.text
   # title = soup.select('div._y8HYJ-y_lTUHkQIc1mdCq _2INHSNB8V5eaWp4P0rY_mE')
   # title = soup.find(class_='_eYtD2XCVieq6emjKBH3m')
   # print(title)

   # body = soup.select('div > div > ._1qeIAgB0cPwnLhDF9XSiJM')
   # all = str(title) + str(body)
   # all.append(all)
   # print(all)

# for i in link:
#     url = requests.get(url=link[i])
#     html = open(url,'rt',encoding='utf-8')
#     html = html.read()
#     soup = BeautifulSoup(html, 'lxml', from_encoding='utf-8')
#
#     title = soup.select('div > div > title')
#     body = soup.select('div > div > ._1qeIAgB0cPwnLhDF9XSiJM')
#     all = str(title) + str(body)
#     all.append(all)
#     print(all)
