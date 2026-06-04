/* Use a while loop and getchar() to read standard input one character at a time.

Keep reading until the program hits EOF (End of File). Note: In your Linux Mint terminal, you simulate EOF by pressing Ctrl + D.

Condition A: If the character is a lowercase letter (a to z), convert it to uppercase using raw ASCII math.

Condition B: If the character is a number (0 to 9), censor it by replacing it with an asterisk *.

Condition C: All other characters (spaces, punctuation, existing uppercase letters, newlines) get printed exactly as they are using putchar().*/
# include <stdio.h>
while i != EOF
    if i >= a and i <= z:
        i +=32 