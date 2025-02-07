---
title: "[시스템 프로그래밍] File I/O Basic"
date: 2023-12-22
categories: Coding
---


    int read_f(int fd){
    
    
            read(fd, buf, sizeof(buf));
    
            printf("%s\n",buf);
            if( fd == -1){ perror("write error"); return -1;}
    
    }
    
    
    
    int main() {
    
    int sel_num = 0;
    int fd = 0;
    char* pName = "/user/clang/fileio.txt";
    
    puts("Welecome to file I/O\n");
    puts("Select number:");
    puts("write: 1 , open: 2 ");
    scanf("%d", &sel_num);
    
    
    
    
    switch(sel_num){
    
    
            case 1 :
    
                    fd = open_f(pName);
                    if(fd != -1){
    
                    write_f(fd);
    
                    break;
                    }
    
            case 2 :
    
                    fd = open_f(pName);
                    if(fd != -1){
    
                    read_f(fd);
                    break;
    
                    }
    
            default :
    
                    puts("Out of bound!");
                    break;
    
    
    }
    
    }

