#!/usr/bin/python                                                                                                                        

import pexpect
user="ppriyank"
host="csecourses.cse.iitk.ac.in"
passwd = "******"

child1 = pexpect.spawn("nautilus sftp://ppriyank@csecourses3.cse.iitk.ac.in/users/btech/ppriyank/cs330assignment1/nachos/code")

child = pexpect.spawn('ssh ppriyank@csecourses3.cse.iitk.ac.in')
child.expect('ppriyank@webhome.cc.iitk.ac.in\'s password: ')
child.sendline(passwd)
child.expect('ppriyank@csecourses3.cse.iitk.ac.in\'s password: ')
child.sendline(passwd)
child.sendline("cd cs330assignment1/nachos/code/")


# child1.sendline(passwd)
# child1 = pexpect.spawn("nautilus sftp://ppriyank@vyom.cc.iitk.ac.in/users/ee/bt/ppriyank")
# child1.sendline("nautilus sftp://ppriyank@vyom.cc.iitk.ac.in/users/ee/bt/ppriyank") 
# child1.expect('Enter password for ppriyank on vyom.cc.iitk.ac.in')
# child1.sendline(passwd)
child.interact()


