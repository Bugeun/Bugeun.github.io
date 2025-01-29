---
layout: post
title: (Algorithm) Selection_Sort
categories: Coding
---
<br>
https://www.acmicpc.net/problem/23881
<br>


```jsx
#include <stdio.h> 
#include <stdlib.h>
#include <string.h> 

int main(){ 

int input1, input2, max, temp, idx;  

int count = 0; 
char pr[20] = "input two number";
char str[20] = "input size";

printf("%s\n", pr); 
scanf("%d %d",&input1, &input2);

getchar();
char *arr = (char *)malloc(input1 * sizeof(char)); 

fgets(arr, input1+10, stdin);
char *token = strtok(arr, " "); 
while(token != NULL && count <= input1) {
						
			arr[count++] = atoi(token); 
			token = strtok(NULL, " "); 

} 

temp = input1;
count = input2;

for(int i = 0; i <= input1; i++) {

    		
    //finding the max number
    for(int a = 0; a <= (input1 - 1); a++){

        if(arr[a] == temp){

            max = a;
            
        }

    }

 
    //sort
	for(int j = input1; j >= 0; j--){ 

        if(arr[j] < arr[max]){
            
            arr[max] = arr[j]; 
            arr[j] = max;
            
        }
        
    }

temp--;

}

    //print result
    for(int f = 0; f <= input1-1; f++){

        printf("res %d\n", arr[f]);
    }



}
```