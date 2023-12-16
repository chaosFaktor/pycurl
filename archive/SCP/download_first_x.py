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


#url = sys.argv[1]


for i in range(100, 3000):
    
    url = "https://scp-wiki.wikidot.com/scp-"+str(i) 
    html = webengine.get(url)
    soup = BeautifulSoup(html, "html.parser")
#soup = soup.find("div", id="body")

    soup = soup.find("div", id="main-content")
    open('out/'+url.replace("https://scp-wiki.wikidot.com/", ""), 'w+').write(soup.prettify() + style)




