import os
import sys
import sqlite3
global keywordtext
global baseurl
global lock
global prebaseurl
global homedir
global datadir
global historydir
global origindir
global resultdir
global url
global homeurl
keywordtext = ""
baseurl=""
lock=0
datadir=os.path.expanduser('~') + "/.local/share/webkit/databases/file__0.localstorage"
prebaseurl=""
url=""
#homedir = os.getcwd()
homedir = sys.path[0]
historydir = homedir + "/cache/history.cache"
origindir = homedir + "/cache/origin.html"
resultdir = homedir + "/cache/result.html"
homeurl = "file://" + homedir + "/cache/config.html"
baseurlyoudao="http://dict.youdao.com/search?q="
baseurlicb="http://www.iciba.com/"
