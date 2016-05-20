import util

def demo1(ip):
    return util.get_s("http://"+ip)

def demo2(ip):
    return util.get_s("http://"+ip)

methods = [demo1,demo2]
