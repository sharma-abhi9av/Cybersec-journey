# include <stdio.h>
void swap();
main() {
    int x = 2;
    int y = 3 ;
    printf("x is %i,  y is %i\n",x,y);
    swap(&x,&y);
    printf("x is %i, y is %i\n",x,y);
}
void swap(int *a, int *b){
    int tmp;
    tmp = *a ;
    *a = *b  ;
    *b = tmp ;
}