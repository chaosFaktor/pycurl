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


webengine = engine.Engine()


#url = sys.argv[1]

c = 0
for i in range(0, 80):
    
    url = "https://www.druckspezialist.eu/detail/" + str(i) + "/"
    print(url)
    html = webengine.get(url)
    soup = BeautifulSoup(html, "html.parser")
#soup = soup.find("div", id="body")

    soup = soup.find("div", id="content")
    open('newout/'+str(c), 'w+').write(soup.prettify())
    c+=1


