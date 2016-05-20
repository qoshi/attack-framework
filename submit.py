import util
import config

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
