---
layout: post
title: Baseball game
categories: Coding
---
<br>

```jsx
#include <iostream>
#include <time.h>

using namespace std;

int main() {

	string s;
	srand((unsigned int)time(0));
	string com;
	com.resize(4);

	for (int i = 0; i < com.size(); i++) {

		int num = rand() % 10;
		com[i] = '0' + num;

	}

	while (1) {

		int ball = 0;
		int strike = 0;
		int out = 0;

		cout << "0~9까지 4자리의 숫자를 입력해주세요." << endl;
		cin >> s;

		if (s.compare(com) == 0) {

			cout << "정답" << endl;
			return 0;
		}

		if (s.size() != 4) {
			cout << "4자리의 숫자만 가능합니다." << endl;
			continue;
		}

		for (int i = 0; i < 4; i++) {
			
			if (s[i] < '0' || s[i] > '9') {
				break;
			}

		cout << i << "번째 입력값 : " << s[i] << endl;

			if (com[i] == s[i]) {

				strike++;
			}

			for (int n = 0; n < 4; n++) {

				if (com[i] != s[i] && com[i] == s[n]) {
					ball++; 
				}

			} 

			
		}

		if (strike == 0 && ball == 0) {
			out = 1;
		}

		
		cout << "스트라이크 : " << strike << endl;
		cout << "볼 : " << ball << endl; 
		cout << "아웃 : " << out << endl; 

	}

}
```