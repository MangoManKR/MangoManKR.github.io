HYU CSE ITE3062 인간컴퓨터상호작용 Project 2(~23.06.08)

# TL-DR-for-Wiki-Hot-Topic
Using GPT API, summerize hot news on Korean Wiki sites "나무위키" which serves real-time hot topics.(https://mangomankr.github.io/TL-DR-for-Wiki-Hot-Topic/)

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
# Project Objectives
Now that major search engines (e.g. naver, daum) do not provide real-time search terms. But, 나무위키, one of the sites widely used by the MZ generation, provides real-time search terms. However, due to the properties of Wiki, keywords that are not familiar to the public are often listed in real-time keywords, and even if they are listed in it, the contents of the document are too long to know why it is a hot topic now. Therefore, the goal of this project is to create a web that provides a 3-line summary of real-time search terms of '나무위키' using GPT APIs and web crawling.

# Structure of Project
①	Crawling the real-time search term of ‘나무위키’ and its contents when the site has the most user.  
②	Summarize each article focusing on recently revised contents via GPT.  
③	Post Today’s hot topic summary on Web.  
④	Generate short NEWS via video generate AI (e.g. synthesia). (optional).  

# Expected Effects
There is already a system called TLDR NEWS letter, and I think I can compare it. A huge amount of news is posted around the world every day, and it costs a lot of money and time to select only the news that users want and summarize it using AI (approximately several 100,000 won per month.). By importing data from 나무위키, one of the largest sites that provides real-time search terms in Korea, it will be possible to check the trends of the younger generation by greatly reducing costs and time. In addition, it is expected that after a three-line summary, I plan to add the 'details' button so that it can be moved to the document, and that it will be possible to observe in which topics the 'details' button is pressed more. So we can see what is hard to summarize topic and what is not.


