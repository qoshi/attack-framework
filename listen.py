from BaseHTTPServer import BaseHTTPRequestHandler,HTTPServer
import attack
import config

flag_callback = None

#This class will handles any incoming request from
#the browser
class myHandler(BaseHTTPRequestHandler):
    global flag_callback
    def do_GET(self):
        self.send_response(200)
        flag = self.path[1:]
        if len(flag) > 0 and (flag not in attack.flag_pool):
            attack.flag_pool[flag] = True
            if attack.submit_flag(flag):
                attack.count += 1
                attack.total += 1
                flag_str = config.flag_fmt%(attack.rounds,attack.total,"listener","",flag)
                config.f_rec(flag_str)
        return

def listen():
    server=HTTPServer(('',config.listen_port),myHandler)
    server.serve_forever()
