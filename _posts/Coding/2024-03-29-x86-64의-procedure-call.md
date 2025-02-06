---
title: "x86/64의 Procedure Call"
date: 2024-03-29
categories: Coding
---

![](https://blog.kakaocdn.net/dn/bvchgj/btsGd996SNX/qiRPcfToKjcTM7KiXtR8R1/img.png)

**DESCRIPTION.**

1\. PUSH PARAM은 콜링 컨벤션에 따라 스택에 인자를 넣는 작업이다.

2\. CALL 인스트럭션으로 함수를 호출한다. 이 때 CALL은 EIP를 스택에 PUSH (즉, RET 어드레스가 된다.) 하고
DEST(주소값)을 EIP에 넣어 분기한다. (MOV는 실제로 없지만 편의상 넣었다.)

3\. 이전 루틴(프로시져)의 EBP를 스택에 넣는다.

4\. ESP를 EBP에 넣어 스택 프레임 포인터를 생성한다. (이전 스택의 TOP 주소가 EBP 주소가 되면서 새로운 프레임 포인터가
생성된다.)

5~6. 인자와 버퍼를 생성하고 루틴을 처리한다

7\. ebp를 esp에 넣는다. 그럼 스택에 담겨있는 ebp가 된다.

8\. pop ebp로 이전 프로시저의 스택 프레임을 만든다.

9\. 8번을 수행하면 자연스럽게 esp가 감소되고 이전에 넣었던 EIP 주소(return addres)가 되면서 ret(pop eip)을
실행하면

원래의 주소로 돌아간다.

**TIP.**

1\. CALL은 스택에 RET 주소를 넣고 다음 프로시저로 분기하지만 JMP는 그냥 뛴다.

2\. PUSH와 POP을 할 땐 ESP를 꼭 감소 또는 증가시킨다. (스택의 TOP을 가르키므로)

3\. 또한 POP은 DEST(목적 레지스터)에 스택의 값을 넣는다.

4\. x86 어셈블리에선 함수의 리턴값은 EAX를 통해 전달된다.

![](https://blog.kakaocdn.net/dn/cCTA08/btsGeLOlY4S/RKxZTuLlac7ms7H5NnWCcK/img.png)
![](https://blog.kakaocdn.net/dn/MjdEE/btsGcfRdv40/xmjCZ497smQ14wkjTISfEk/img.png)

**참고했던 인스트럭션 자료:**

인텔 64 and IA-32 레퍼런스 Volume 1,2

