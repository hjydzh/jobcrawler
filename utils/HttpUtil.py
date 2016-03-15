#coding:utf-8
import urllib2
import sys
import urllib
import cookielib

def request(url):
    send_headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 6.2; rv:16.0) Gecko/20100101 Firefox/16.0',
    'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Connection':'keep-alive'
    }
    req = urllib2.Request(url,headers=send_headers)
    return urllib2.urlopen(req).read()


def init_opener():
    return urllib2.build_opener(urllib2.HTTPCookieProcessor(cookielib.CookieJar()))

def opener_request(url, opener):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/31.0.1650.57 Safari/537.36'}
    post_data=urllib.urlencode({})
    req=urllib2.Request(url,post_data,headers)
    return opener.open(req).read()




