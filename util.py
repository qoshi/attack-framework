import urllib2
import urllib
import logging

#simple get request
def get_s(url):
    req = urllib2.urlopen(url)
    return {
        "code" : req.getcode(),
        "response" : req.read()
    }

# headers should be like this: [('User-agent', 'Mozilla/5.0'),('key':'value')]
def get_h(url,headers):
    opener = urllib2.build_opener()
    opener.addheaders = headers
    req = opener.open(url)
    return {
        "code" : req.getcode(),
        "response" : req.read()
    }

#querys should be like this{"key":"value","key":"value"}
def get_q(url,querys):
    query_string = urllib.urlencode(querys,True)
    url = url + "?" + query_string
    return get_s(url)

# data should be liek this: {"key":"val1","key2":"val2"}
def post_s(url,data):
    dat = urllib.urlencode(data)
    req = urllib2.urlopen(urllib2.Request(url,dat))
    return {
        "code" : req.getcode(),
        "response" : req.read()
    }



