from pexpect import pxssh
import getpass
import sys

if len(sys.argv) < 4:
  print("rmt ip-addr user-id- passwd")

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
