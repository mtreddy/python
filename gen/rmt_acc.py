from pexpect import pxssh
import getpass
import sys


class rmt_acc:
    def __init__(self):
        print("Initializing")	
    def get_cpu_info(s):
        s.sendline('lscpu')
        s.prompt()
        line = s.before
        print(line)
    
    def get_no_of(self):
        s.sendline('lscpu| grep cpu')
        s.prompt()
        line = s.before
        print(line)

    def ssh_conn(self, ip, uid, pasw):        
        try:
           s = pxssh.pxssh()    
           s.login(ip, uid, pasw)
        except pxssh.ExceptionPxssh as e:
           print("pxssh failed to login")
           print(e)
        return s

if len(sys.argv) < 4:
 print("rmt ip-addr user-id- passwd")
ip = sys.argv[1]
uid = sys.argv[2]
pasw = sys.argv[3]

rmt = rmt_acc()
rmt = get_cpu_info(s)
