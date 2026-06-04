#include <stdio.h> 

int main(void){
    int n = 50;
    printf("%i\n",n);       // print the number 
    printf("*%p\n", &n) ;   // print the address of number in memory 
}