#!/usr/bin/env python3
import engine
import config as cfg

from bs4 import BeautifulSoup
import sys



style = """
<style>
    * {
        font-family: Impact, Haettenschweiler, 'Arial Narrow Bold', sans-serif;
    }
    .header_left {
        display: none
    } 
    .top_blob {
        display: none
    }
    .right_col {
        display: none
    }
    .left_col {
        display: none
    }
    .hidden_col {
        display: none
    }
    .main_content {
        display: none
    }


</style>
"""

i = 0

webengine = engine.Engine()


url = 'https://www.theregister.com/2022/08/26/bofh_2022_episode_16/'
url = sys.argv[1]
html = webengine.get(url)
soup = BeautifulSoup(html, "html.parser")
#soup = soup.find("div", id="body")

soup = soup.find("article")
open('out/'+url[:-1].replace('https://', '').replace('.html', '').replace('/', '_') + '.html', 'w+').write(soup.prettify() + style)




