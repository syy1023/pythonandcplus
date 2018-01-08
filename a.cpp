#include <stdio.h>
extern "C"
{
 int add(int a,int b){
	return a+b;
 }
 void print_sum(unsigned long ulNum){
       while(ulNum!=0){
            printf("the num is:%u\n",ulNum--);
        }
    }

}