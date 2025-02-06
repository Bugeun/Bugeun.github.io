---
title: "[어셈블리] 2Byte Opcode 공부하다가 끄적.."
date: 2024-03-22
categories: Coding
---

인텔 아키텍처 x86의 기계어 구성방식은 아래 사진과 같이 이루어진다.

1 Byte의 prefixes는 x86에서 가변길이를 정한다. 그 다음 1,2,3바이트의 Opcode가 담긴다.

예로들어 REX prefixes는 64비트 오퍼랜드를 나타내거나 Extended control 레지스터를 나타내기도 한다.

ModR/M은 Operand의 모드를 지정하거나 때론 특정 opcode의 정보를 담고 있기도 한다.

(1바이트)

SIB는 32비트 주소에서 Mod R/M이 사용한다. 이 경우 오퍼랜드의 위치에 따라 결정된다.

immediate는 operand가 상수일 경우 표현된다. 1,2,4바이트로 나뉜다

![](https://blog.kakaocdn.net/dn/ca16jy/btsF18b8HKs/A9AKRnhPKtEEWcgb9oO5e1/img.png)

우리는 특정 Byte Stream을 볼 때

인텔에서 제공되는 레퍼런스에 있는

intel Opcode Table를 보며 이를 해석한다.

(<https://software.intel.com/content/dam/develop/external/us/en/documents-
tps/325383-sdm-vol-2abcd.pdf>)

![](https://blog.kakaocdn.net/dn/b5uR0B/btsFZVMdBxX/NCEY1t5wUTAZn7s1k9mdEK/img.png)
![](https://blog.kakaocdn.net/dn/bqriHT/btsF14HyD6H/8pIJUbuBhKELrLh49D7Tn0/img.png)

근데 어떤 글에서 Prefixs를 참조되는 바이트 스트림인 경우 2바이트 Opcode라고 하는 경우를 보아서

의문이 들어 알아보았는데, 그렇지 않았다.

(<https://modoocode.com/316>)

아래의 글을 보면 그 이유를 알 수 있다.

![](https://blog.kakaocdn.net/dn/3rPxi/btsF3fn7RRa/kQ2EdR4I1fCvzLkK68fYyK/img.png)

2바이트 이상의 Opcode는 첫 번째 바이트에 Escape(0x0F)가 온다.

실제로 아래 링크에서 제공되는 표를 보면 확실히 알 수 있다.

<http://ref.x86asm.net/coder32.html>

[ coder32 edition | X86 Opcode and Instruction Reference 1.12 ref.x86asm.net ](http://ref.x86asm.net/coder32.html)

![](https://blog.kakaocdn.net/dn/cu6572/btsF1MmVAP3/KiTbSk6gbJApKDsFJgdj8K/img.png)

실제로 레퍼런스에서도 Two bytes Map부터는 0x0F가 처음에 붙는다고 적혀있다.

![](https://blog.kakaocdn.net/dn/btiedz/btsF0G17mRZ/llSzbjzHoZMTeqe1EI2qz1/img.png)

