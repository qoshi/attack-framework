import thread
import attack
import listen
import config

def fk(aa):
    print aa

config.init()
thread.start_new_thread( attack.attack,() )
thread.start_new_thread( listen.listen, () )
while 1:
    pass
