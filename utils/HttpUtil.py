#coding:utf-8
import urllib2
import sys


def request(url):
    send_headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 6.2; rv:16.0) Gecko/20100101 Firefox/16.0',
    'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Connection':'keep-alive'
    }
    req = urllib2.Request(url,headers=send_headers)
    r  = urllib2.urlopen(req)

    html = r.read()                       #返回网页内容


    # sys.getfilesystemencoding()
    return html



