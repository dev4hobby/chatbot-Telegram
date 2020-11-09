import os
import requests
from dotenv import load_dotenv
from bs4 import BeautifulSoup
from fake_useragent import UserAgent

load_dotenv(verbose=True)
AGENT_DSN = os.getenv('AGENT_DSN')

class Crawl():
    def __init__(self):
        self.headers = {'User-Agent': UserAgent().random,
                        'From': AGENT_DSN}

    def get_contents(self, url):
        request = requests.get(url, headers=self.headers)
        content = request.content
        try:
            soup = BeautifulSoup(content, 'html5lib')
        except:
            soup = BeautifulSoup(content, 'html.parser')
        finally:
            pass
        return soup

class Naver(Crawl):
    def __init__(self):
        super().__init__()
        self.main_url = {'news' : 'https://search.naver.com/search.naver',}
        self.soup = None

    def get_newspaper(self, keyword):
        message = str()
        url = '{}?where=news&sm=tab_jum&query={}'.format(self.main_url['news'], keyword)
        self.soup = self.get_contents(url)
        articles = self.soup.select("a.news_tit")
        for article in articles:
            message += (article['title']+'\n')
        return message
