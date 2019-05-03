from pexpect import pxssh
import getpass


try:
    s = pxssh.pxssh()    
    s.login('10.111.128.58', 'root', 'caveo123')
    s.sendline('uptime')
    s.prompt()
    line = s.before
    print(line)

except pxssh.ExceptionPxssh as e:
    print("pxssh failed to login")
    print(e)
