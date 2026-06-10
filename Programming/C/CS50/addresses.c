#include <stdio.h> 
int main(void){
    int n = 50;
    int *p = &n; 
    printf("%i\n",n);       // print the number 
    printf("*%p\n", &n) ;   // print the address of number in memory 
    printf("%i\n", *p);
}
