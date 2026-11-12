import os
from urllib.request import urlopen, Request
from urllib.parse import urljoin
from bs4 import BeautifulSoup
import re
import sys
def make_soup(url):
    try:
        req = Request(url, headers={'User-Agent': 'WebScraperDemo/1.0 (educational crawler)'})
        html = urlopen(req, timeout=20).read()
        return BeautifulSoup(html, "html.parser"), html
    except Exception:
        return None, None
def search_words(words, soup):
    count = 0
    try:
        text = soup.get_text().lower()
    except Exception:
        return False
    for i in words:
        if count > 1:
            return True
        if i.lower() in text:
            count += 1
        if count > 1:
            return True
    return False
def save_web(soup, html, icount):
    title = str(soup.title.string) if soup.title and soup.title.string else 'untitled'
    title = re.sub(r'[^A-Za-z0-9 _.-]', '_', title)[:80]
    foo = open(str(icount)+' '+title+'.html', 'wb')
    foo.write(html)
    foo.close()
def extract_links(soup, url, urls, visited):
    for link in soup.find_all('a'):
        if link.get('href') != None and ((urljoin(url, '/')+link.get('href').strip('/')) not in visited) and ("#" not in link.get('href')):
            urls.append(urljoin(url, '/')+link.get('href').strip('/'))

def run():
    startUrl = ['https://en.wikipedia.org/wiki/Nintendo_64', 'https://en.wikipedia.org/wiki/Home_video_game_console']
    print('Crawler Settings: \nUp to 500 sites.\nStarting sites:\nhttps://en.wikipedia.org/wiki/Nintendo_64\nhttps://en.wikipedia.org/wiki/Home_video_game_console\n')
    urls = startUrl
    visited = []
    saved = []
    words = ['xbox', 'playstation', 'nintendo', 'atari', 'odyssey', 'steam', 'handheld', 'console', 'gameboy', 'japan' ]
    visitedlog = open('visited.txt', 'w')
    savedlog = open('saved.txt', 'w')
    icount = 0
    while len(urls) != 0 and len(saved) < 500:
        url = urls.pop(0)
        if url in visited:
            continue
        icount+=1
        print('Progress: '+ str(len(saved))+'/500')
        print(url)
        soup, html = make_soup(url)
        ##logfile =open('debug.log', 'w')
        if search_words(words, soup):
            save_web(soup, html, icount)
            extract_links(soup, url, urls, visited)
            saved.append(url)
            ##logfile.write(' **Success**\n'+str(url)+'\n')
            print(' **Success!**\n')
        else:
            print(' **Failed!**\n')
            ##logfile.write(' **Failed!**\n'+str(url)+'\n')
        ##logfile.close()
        visited.append(url)
    for i in visited:
        visitedlog.write(i+'\n')
    for i in saved:
        savedlog.write(i+'\n')
    visitedlog.close()
    savedlog.close()

if __name__ == "__main__":
    run()
    if sys.platform.startswith("win"):
        os.system("pause")





