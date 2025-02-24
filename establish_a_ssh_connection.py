# import required modules/packages/library
import pexpect

# define variables
ip_address = '192.168.56.101'
username = 'prne'
password = 'cisco123!'
password_enable = 'class123!'

# create the SSH session
session = pexpect.spawn ('ssh ' + username + '@' + ip_address, encoding='utf-8', timeout=20)
result = session.expect (['Password:', pexpect.TIMEOUT, pexpect.EOF])

# check for error, if exists then display error and exit
if result != 0:
    print('--- FAILURE! creating session for: ', ip_address)
    exit()

# session expecting password, enter details
session.sendline(password)
result = session.expect (['>', pexpect.TIMEOUT, pexpect.EOF])

# check for error, if exists then display error and exit
if result != 0:
    print('--- FAILURE! entering password: ', password)
    exit()

# enter enable mode
session.sendline('enable')
result = session.expect(['Password:', pexpect.TIMEOUT, pexpect.EOF])

# check for error, if exists then display error and exit
if result != 0:
    print('--- Failure! entering enable mode')
    exit()

# send enable password details
session.sendline(password_enable)
result = session.expect (['#', pexpect.TIMEOUT, pexpect.EOF])

# check for error, if exists then display error and exit
if result != 0:
    print ('--- Failure! entering enable mode after sending password')
    exit()

# enter config mode
session.sendline('configure terminal')
result = session.expect ([r'.\(config\)#', pexpect.TIMEOUT, pexpect.EOF])

# check for error, if exists then display error and exit
if result != 0:
    print('--- Failure! entering config mode')
    exit()

# change hostname to R1
session.sendline('hostname R1')
result = session.expect([r'R1\(config\)#', pexpect.TIMEOUT, pexpect.EOF])

# check for error, if exists then display error and exit
if result != 0:
    print('--- Failure! setting hostname')

# exit config mode
session.sendline('exit')

# exit enable mode
session.sendline('exit')

# display success message if it works
print ('------------------------------------------------------')
print ('')
print ('--- success! connecting to: ', ip_address) 
print ('---                Username: ', username)
print ('---                Password: ', password)
print ('')
print ('------------------------------------------------------')

# terminate SSH session
session.close()
