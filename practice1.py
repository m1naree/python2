import requests
from bs4 import BeautifulSoup
from datetime import datetime


url="https://music.bugs.co.kr/chart"
response= requests.get(url)

soup = BeautifulSoup(response.text, 'html.parser')
rank=1


result= soup.findAll('p','title')
search_rank_file = open("practice1.txt","w",encoding="utf=8")

print(datetime.today().strftime("%Y년 %m월 %d일의 실시간 음원순위입니다. \n"))

for result in result:
    search_rank_file.write(str(rank)+"위:"+result.get_text()+"\n")
    print(rank,"위 : ",result.get_text(),"\n")
    rank += 1