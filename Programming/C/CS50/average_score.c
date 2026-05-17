/* Make an program to calculate the average score of 3 subject, with marks 33,72,73 */
#include <stdio.h>
main(void){
    int scores[3];
    scores[1] = 33;
    scores[2] = 73;
    scores[0] = 72;
    printf("The average score is %f\n", (scores[0]+scores[1]+scores[2])/3.0);
}