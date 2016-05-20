import config

import logging
import time
import datetime

#flag_log = open(config.flag_log_path,"a")
#req_log = open(config.req_log_path,"a")

response_fmt = "[log] %s   | %s | %s | %d | %s" #time functioname target status response
error_fmt    = "[error] %s | %s | %s |~~~ERROR~~| %s" #time functioname target error info

flag_fmt = "%d | %s | %s | %s" #round functionname target flag
ips = config.noob_ips

#get ips
ip_len = len(ips)
rounds = 0

def c_time():
    return datetime.datetime.now()

def run_one_func(func,ip):
    try:
        resp = func(ip)
        print response_fmt%(c_time(),func.__name__,ip,resp["code"],resp["response"])
        return resp
    except Exception as e:
        print error_fmt%(c_time(),func.__name__,ip,e)
    return ""

while 1:
    rounds += 1
    print "round %d begin:"%rounds
    #get attack methods
    reload(attack_method)
    methods = attack_method.methods
    methods_len = len(methods)
    for i in range(0,methods_len):
        method = methods[i]
        for j in range(0,ip_len):
            ip = ips[j]
            run_one_func(method,ip)

    time.sleep(10)
