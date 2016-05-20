import config
import attack_method
import util

import logging
import time
import datetime

flag_pool = {}
flag_log = open(config.flag_log_path,"a")
req_log = open(config.req_log_path,"a")

response_fmt = "[log] %s   | %d time | %s | %s | %s | %d | %s\n" #time retry time functioname target method status response
error_fmt    = "[error] %s | %s | %s |~~~ERROR~~| %s\n" #time functioname target error info

flag_fmt = "%d | %s | %s | %s\n" #round functionname target flag
ips = config.noob_ips

#get ips
ip_len = len(ips)

def c_time():
    return datetime.datetime.now()

def run_one_func(func,ip):
    times = 0
    while times < 3:
        try:
            resp = func(ip)
            resp_str = response_fmt%(c_time(),times,func.__name__,resp["url"],resp["method"],resp["code"],resp["response"])
            req_log.write(resp_str)
            return resp["response"]
        except Exception as e:
            err_str = error_fmt%(c_time(),func.__name__,ip,e)
            req_log.write(resp_str)
            time += 1
    return ""

def submit_flag(flag):
    times = 0
    while times < 3:
        try:
            util.post_s("http://"+config.flag_ip,{"flag":flag})
            return True
        except Exception as e:
            s = error_fmt%(c_time(),"submit error",config.flag_ip,e)
            req_log.write(s)
            times += 1
    return False

def attack():
    rounds = 0
    while 1:
        rounds += 1
        count = 0
        req_log.write("round %d begin:\n"%rounds)
        #get attack methods
        reload(attack_method)
        methods = attack_method.methods
        methods_len = len(methods)
        for i in range(0,methods_len):
            method = methods[i]
            for j in range(0,ip_len):
                ip = ips[j]
                flag = run_one_func(method,ip)
                if len(flag) > 0 and (flag not in flag_pool):
                    flag_pool[flag] = True
                    if submit_flag(flag):
                        count += 1
                        flag_str = flag_fmt%(rounds,method.__name__,ip,flag)
                        flag_log.write(flag_str)
        req_log.write("round %d finished, %D flag get:\n"%(rounds,count))
        time.sleep(30)

