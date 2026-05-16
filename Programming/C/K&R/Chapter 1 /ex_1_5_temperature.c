/* print the temprature in reverse order ie 300 to 0 */
# include <stdio.h>
main (){
    int fahr;
    for (fahr = 300; fahr >= 0; fahr -=20)
        printf("%d\t%.2f\n", fahr, (5.0/9.0)*(fahr-32));
} 