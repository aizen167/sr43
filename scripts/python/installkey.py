#!/usr/bin/env python
#

"""
This script attempts to ssh to the specified host with the username
and password given below. The script tries to identify timeouts and
other types of ssh failures, as well as authentication failure, to
give useful feedback.

IMPORTANT: This script requires that the pexpect package be installed!

Usage: installkey KEYFILE HOST

"""

import sys
import pexpect
import getopt

opts, args = getopt.getopt(sys.argv[1:], 'u:p:', ['username=', 'password='])

username = 'root'
password = 'redhat'

for o, a in opts:
    if o in ('-u', '--username'):
        username = a
    if o in ('-p', '--password'):
        password = a

try:
    keyfile=args[0]
    host=args[1]
except IndexError:
    print('Usage: installkey [-u|--username=<username>] [-p|--password=<password>] KEYFILE HOST')
    sys.exit(2)

def timeout():
    print('Connection timed out will trying to reach the ssh server.')
    print('Please verify that your ssh service is running and that your')
    print('firewall is not blocking connections to it. Then try running')
    print('this script again.')
    sys.exit(2)

def dumped():
    print('The connection was unexptedly dropped when trying to login to')
    print('your ssh server. Please verify that your ssh server is running')
    print('and try again. If you continue to see this message, ask your')
    print('instructor for assistance.')
    sys.exit(3)
    
def failure():
    print('Failed to login with username "%s" and password "%s"'%(username,password))
    print('Check your authentication settings and try again.')
    sys.exit(1)
    
def success():
    print('Sucessfully installed key on %s.'%(host))
    sys.exit(0)

def check():
    #ssh = pexpect.spawn('/bin/cat %s | /usr/bin/ssh %s@%s "umask 077; test -d .ssh || mkdir .ssh ; cat >> .ssh/authorized_keys"'%(keyfile,username,host))

    # Warning: This will break if there are ssh keys already configured.
    # Either remove the private key or set "PubkeyAuthentication no" in
    # ~/.ssh/config

    ssh = pexpect.spawn('ssh-copy-id -i %s %s@%s'%(keyfile,username,host))
    ssh.logfile = sys.stdout
    i = ssh.expect(["Are you sure you want to continue connecting (yes/no)?",
                    "%s@%s's password: "%(username,host),
                    pexpect.TIMEOUT,
                    pexpect.EOF])
    if i == 0: # first time connecting
        ssh.sendline('yes')
        ssh.expect("%s@%s's password: "%(username,host))
        ssh.sendline(password)
        ssh.expect("Now try logging into ")
    if i == 1: # known_hosts entry exists
        ssh.sendline(password)
        ssh.expect("Now try logging into ")
    if i == 2: # oops, timeout
        timeout()
    if i == 3: # connection refused/dumped
        dumped()
        
def main():
    print('Attempting to login via ssh to %s as %s with password %s...'%(host,username,password))
    check()
    
if __name__ == '__main__':
    main()
