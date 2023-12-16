#!/usr/bin/env python3

import config as cfg


from bs4 import BeautifulSoup
import subprocess
import re

class Engine:

    def __init__(self) -> None:
        if cfg.Engine.webengine == 'curl':
            self.get = Engine.get_curl


    def get_curl(cmd, decode='UTF-8', arg=''):
        arg += cfg.Engine.webengine_args + ' '
        result = subprocess.Popen("curl "+arg+" '"+cmd+"'", shell=True, stdout=subprocess.PIPE).stdout.read()
        if len(decode)>0:
            return result.decode(decode)
        else: 
            return result
        

