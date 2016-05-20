import config
import attack_method
import util

import logging
import time
import datetime

flag_pool = {}

ips = config.noob_ips

count = 0
rounds = 0
total = 0

#get ips
ip_len = len(ips)

def c_time():
    return datetime.datetime.now()

def run_one_func(func,ip):
    times = 0
    while times < 3:
        try:
            resp = func(ip)
            resp_str = config.response_fmt%(c_time(),times,func.__name__,resp["url"],resp["method"],resp["code"],resp["response"])
            config.r_rec(resp_str)
            return resp["response"]
        except Exception as e:
            err_str = config.error_fmt%(c_time(),func.__name__,ip,e)
            config.r_rec(resp_str)
            time += 1
    return ""

def submit_flag(flag):
    times = 0
    while times < 3:
        try:
            util.post_s("http://"+config.flag_ip,{"flag":flag})
            return True
        except Exception as e:
            s = config.error_fmt%(c_time(),"submit error",config.flag_ip,e)
            config.r_rec(s)
            times += 1
    return False

def attack():
    global rounds
    global total
    while 1:
        rounds += 1
        global count
        config.r_rec("round %d begin:\n"%rounds)
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
                        total += 1
                        flag_str = config.flag_fmt%(rounds,total,method.__name__,ip,flag)
                        config.f_rec(flag_str)
        time.sleep(30)
        config.r_rec("round %d finished, %d flag get, %d total\n"%(rounds,count,total))
        count = 0


