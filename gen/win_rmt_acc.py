import sys
import wexpect

prompt = 'amd@epyc'
perm_str = 'Permission denied, please try again'

def get_cpu_id(ch):
    prompt = 'amd@epyc'
    ch.sendline('lscpu')
    ch.expect(prompt)

if len(sys.argv) < 4:
    print("USage:rmt_acc ip-addr user-id passwd")
    sys.exit(0)
ip = sys.argv[1]
uid = sys.argv[2]
pasw = sys.argv[3]
print("args ip-%s uid-%s pasw-%s" % (ip, uid, pasw))

cmd = 'ssh %s@%s'%(uid, ip)
print(cmd)
ch = wexpect.spawn(cmd)
val = ch.expect(['password:', 'you want to continue', 'amd@epyc', perm_str])
print(val)
print("1 before", ch.before)
print("1 after", ch.after)
if val == 0:
    ch.sendline(pasw)
elif val == 1:
    ch.sendline('Yes')
elif val == 2:
    ch.sendline('pwd')
elif val == 3:
    ch.sendline(pasw)

val = ch.expect(['password:', 'you want to continue', 'amd@epyc', perm_str])
print(val)
print("2 before", ch.before)
print("2 after", ch.after)

if val == 0:
    ch.sendline(pasw)
elif val == 1:
    ch.sendline('Yes')
elif val == 2:
    ch.sendline('pwd')
elif val == 3:
    ch.sendline(pasw)

print("3 before", ch.before)
print("3 after", ch.after)
val = ch.expect(['password:', 'you want to continue', 'amd@epyc'])
print(val)
if val == 0:
    ch.sendline(pasw)
elif val == 1:
    ch.sendline('Yes')
elif val == 2:
    ch.sendline('pwd')
    print("Ready to prcoess commands \n")
    print(ch.before)
elif val == 3:
    ch.sendline(pasw)
else:
    print("Somthing is not right\n")

print("4 before", ch.before)
print("4 after", ch.after)
val = ch.expect(['password:', 'you want to continue', 'amd@epyc'])
print(val)
if val == 0:
    ch.sendline(pasw)
elif val == 1:
    ch.sendline('Yes')
elif val == 2:
    ch.sendline('pwd')
    print("Ready to prcoess commands \n")
    print(ch.before)
elif val == 3:
    ch.sendline(pasw)
else:
    print("Somthing is not right\n")
ch.close()

