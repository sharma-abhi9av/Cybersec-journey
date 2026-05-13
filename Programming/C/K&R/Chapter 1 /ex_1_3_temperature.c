/* From Fahrenheit to celsius */
# include <stdio.h> 
// C = 5/9 * (F - 32)
// Lower = 0, Upper = 100
int main() {
    float F, C, diff, highest, lowest ;
    lowest = 0 ;
    highest = 100;
    F =0;
    printf("=====Fahrenheit to Celsius=====\n");
    while (F <= highest) {
        C = 5.0/9.0 * (F - 32.0);
        printf("%3.2f    %3.2f\n", F, C);
        F += 5.0 ;
    }
}
