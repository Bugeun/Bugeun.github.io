---
layout: post
title: (Algorithm) Find-the-one
categories: Coding
---

<br>
코드프로그래머스: 가까운 1찾기
<br>

```jsx
#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

// arr_len은 배열 arr의 길이입니다.
int solution(int arr[], size_t arr_len, int idx) {
    int answer = 0;
    
    int i, check, temp = 0;
    
    for(i = 0; i <= arr_len; i++){
     
        
        if(i >= idx){
             
             
             if(arr[i] == 1) { 
             
                 answer = i; 
                 break;
             
             }
        }
        
        else{
            
            answer = -1;
            
        }

    }
    
    return answer;
}
```