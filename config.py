noob_ips = [
    "www.baidu.com",
    "www.google.com"
]

flag_ip = "requestb.in/1c82twx1"

req_log_path = "./logs/req.log"
flag_log_path = "./logs/flag.log"
monitor_log_path = ""

listen_port=9922

#log formart
response_fmt = "[log] %s   | %d time | %s | %s | %s | %d | %s\n" #time retry time functioname target method status response
error_fmt    = "[error] %s | %s | %s |~~~ERROR~~| %s\n" #time functioname target error info
flag_fmt = "Rounds %d | %d | %s | %s | %s\n" #round total functionname target flag

#log file
flag_log = None
req_log = None

def init():
    global flag_log
    global req_log
    flag_log = open(flag_log_path,"a")
    req_log = open(req_log_path,"a")

def r_rec(s):
    req_log.write(s)
    print "[INFO]",s[:-1]

def f_rec(s):
    flag_log.write(s)
    print "[FLAG]",s[:-1]
