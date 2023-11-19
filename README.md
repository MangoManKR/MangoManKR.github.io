HYU CSE ITE3062 인간컴퓨터상호작용 Project 2

# TL-DR-for-Wiki-Hot-Topic
Using GPT API, summerize hot news on Korean Wiki sites "나무위키" which serves real-time hot topics.(https://mangomankr.github.io/)

## generate_html.py
You can generate your own summerized website.
### Requirement
* Google Chrome
* Python
* Selenium ```pip install selenium```
* Webdriber Manager ```pip install webdriver -manager```
* Chrome Driver ```https://sites.google.com/a/chromium.org/chromedriver/downloads```  

```
import openai
openai.api_key = '<Your API>'
```

```
from selenium import webdriver
driver = webdriver.Chrome('<Your chromedriver path>')
```
