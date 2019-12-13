from pexpect import pxssh
import getpass
import sys

if len(sys.argv) < 4:
  print("rmt ip-addr user-id- passwd")


def get_cpu_info(s):
    s.sendline('lscpu')
    s.prompt()
    line = s.before
    print(line)
    
def get_no_of

ip = sys.argv[1]
uid = sys.argv[2]
pasw = sys.argv[3]

try:
    s = pxssh.pxssh()    
    s.login(ip, uid, pasw)
    s.sendline('uptime')
    s.prompt()
    line = s.before
    print(line)

except pxssh.ExceptionPxssh as e:
    print("pxssh failed to login")
    print(e)

get_cpu_info(s)
