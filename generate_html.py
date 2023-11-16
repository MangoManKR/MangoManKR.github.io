import requests
import openai
from urllib.parse import quote_plus
from bs4 import BeautifulSoup
from selenium import webdriver
import time

def summerize(words):
    response = openai.ChatCompletion.create(
        model = "gpt-3.5-turbo",
        messages = [{"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": "\n".join(search_list)}],
        temperature = 0.4,
        max_tokens = 1024,
        n = 1,
        stop = None
    )

    chat_response = response.choices[0].message.content
    return chat_response

def html_maker(keyword, words, code):
    return code + f"""<details>
        <summary id="{keyword}_s">{keyword}</summary><p>{words}</p><button id="{keyword}_b"type="button" onclick="location.href='http://namu.wiki/w/{keyword}'">자세히</button></details>
        <script>document.getElementById('{keyword}_s').addEventListener("click", function(event){{gtag('event', 'click', {{'event_category': 'summary', 'event_label': '{keyword}_s'}});}});
        document.getElementById('{keyword}_b').addEventListener("click", function(event){{gtag('event', 'click', {{'event_category': 'button', 'event_label': '{keyword}_b'}});}});
        </script>"""

# type your openai api key
openai.api_key = ''

url = 'https://search.namu.wiki/api/ranking'
response = requests.get(url, headers={"User-Agent": "Mozilla/5.0"})
ranking = response.content.decode('utf-8')
ranking = ranking.strip("[]\"").split("\",\"")
print(ranking)

html_code = """<!DOCTYPE html>
<html>
<head>
<!-- Google tag (gtag.js) -->
<script async src="https://www.googletagmanager.com/gtag/js?id=G-S2FX1J2RE2"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag('js', new Date());

  gtag('config', 'G-S2FX1J2RE2');
</script>
	<meta charset="UTF-8">
	<title>HCI Project 2</title>
    <link rel="stylesheet" href="layout.css">
    <meta name="viewport" content="width=device-width, initial-scale=1">
</head>
<body>
    <header>나무위키 실시간 검색어 요약</header>
    <main>"""

# type your chromedriver path
driver = webdriver.Chrome('')

for keyword in ranking:
    url = 'https://www.google.com/search?q=' + quote_plus(keyword)
    date = '&tbs=qdr:d'

    driver.get(url)
    driver.implicitly_wait(10)

    html = driver.page_source
    soup = BeautifulSoup(html, features="html.parser")

    #r = soup.select('.yuRUbf')
    #r = soup.find_all('div',{'class':'VwiC3b yXK7lf MUxGbd yDYNvb lyLwlc'})
    #r = soup.select('.Z26q7c.UK95Uc')
    r = soup.select('.kvH3mc.BToiNc.UK95Uc')

    search_list = [f"아래 문단은 {keyword}에 대한 구글 검색 결과입니다.\n이 내용들을 요약해서 정리해주세요.\n{keyword}이 무엇인지 설명하고, 최근의 검색 결과에 집중하여 검색이 많아진 이유를 유추하여 정리해주세요.\n".format(keyword)]

    for i in r:
        try:
            #print(i.select_one('.LC20lb.DKV0Md').text) #select 를 안쓰는 이유는 select 를 쓰면 list 로 불러와져서 text 를쓸 수 없다
            #print(i.a.attrs['href']) #a 태그의 href 속성 가져오기
            #print(i.select_one('.VwiC3b.yXK7lf.MUxGbd.yDYNvb.lyLwlc').text)
            search_list.append(i.select_one('.LC20lb.DKV0Md').text + "\n" + i.select_one('.VwiC3b.yXK7lf.MUxGbd.yDYNvb.lyLwlc').text)
        except Exception as e:
            continue
        if len(search_list) >= 4:
            break
    
    driver.get(url + '&tbs=qdr:d')
    driver.implicitly_wait(10)

    html = driver.page_source
    soup = BeautifulSoup(html, features="html.parser")

    r = soup.select('.kvH3mc.BToiNc.UK95Uc')

    for i in r:
        try:
            search_list.append(i.select_one('.LC20lb.DKV0Md').text + "\n" + i.select_one('.VwiC3b.yXK7lf.MUxGbd.yDYNvb.lyLwlc').text)
        except Exception as e:
            continue
    
    html_code = html_maker(keyword, summerize("\n".join(search_list)), html_code)
    time.sleep(20)
    # print("\n".join(search_list))
    # print("="*20, keyword, "="*20)

driver.close()

html_code = html_code + f"""</main>
    
    <footer>
        {time.strftime('%Y-%m-%d %I:%M:%S %p', time.localtime())} 기준. 실시간 검색어 요약은 매일 12시마다 업데이트 됩니다.
    </footer>
    <button type="button" onclick="location.href=''">이전 실검 보기</button>
</body>
</html>"""

with open('', 'w', encoding="UTF-8") as html_file:
    html_file.write(html_code)