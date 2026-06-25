# include <stdio.h>
int get_safe_int();
float get_safe_float();
void update_balance(float balance);
int main(){
    float balance = 1000.5 ; 
    float deposit;
    float withdraw;
    int choice;
    int correct_pin = 1234; // hardcoded intentionally    
    int entered_pin;
    int incorrect_count = 0 ;
    // Read balance from txt file, if not exists use the default 1000.5 as balance.
    FILE *file = fopen("balance.txt", "r");
    if (file != NULL) {
        fscanf(file, "%f", &balance);
        fclose(file);
    }

    while (1){
        printf("Enter your ATM pin:\n");

        entered_pin = get_safe_int();
        if (entered_pin == correct_pin){
            printf("Password Matched!\n");
            break;
            }
        else if (incorrect_count > 1){
            return 1;
            }
        else {
            printf("Wrong PIN!\n");
            incorrect_count += 1;
             }
        }

    while (1) {
        printf("Vxon ATM\n");
        printf("1. Check Balance\n");
        printf("2. Deposit\n");
        printf("3. Withdraw\n");
        printf("4. Exit\n");
    choice = get_safe_int();
    if (choice==1){
        printf("You selected Check Balance!\n");
        printf("Your balance is %.2f\n", balance);        
    }
    else if (choice==2){
        printf("You selected Deposit!\n");
        printf("Choose amount you want to deposit:");
        deposit = get_safe_float();
        if (deposit > 0){
        balance = balance + deposit;
        update_balance(balance);}
        else {printf("Not an valid amount!");}
    }
    else if (choice==3){
        printf("You selected Withdraw!\n");
        printf("Choose amount you want to withdraw:");
        withdraw = get_safe_float();
        if (withdraw > balance)  {
            printf("You don't have enough money to withdraw\n");
        }
        else if (withdraw < 0) {
            printf("Not an valid amount!");
        }
        else {
            balance = balance - withdraw;
            update_balance(balance);
        }
    }
    else if (choice==4){
        printf("You selected Exit!\n");
        break;
    }
    else {
        printf("Invalid option, try again.\n");
    }
}  
return 0;
}


// Function for getting safe input, i,e, only numbers and not alphabets or something else.
int get_safe_int() {
    int value ;
    while (1) {
        if (scanf("%d", &value) ==1) {
            while (getchar() != '\n');
            return value;
        }
        else {
            printf("Error, please enter number only: ");
            while (getchar() != '\n');
        }
    }
}
float get_safe_float() {
    float value ; 
    while (1) {
        if (scanf("%f", &value) == 1 ){
        while (getchar() != '\n');
        return value;
    } else {
        printf("Error, please enter valid amount: \n");
        while (getchar() != '\n');
    }
}}
void update_balance(float balance) {
    FILE *file = fopen("balance.txt", "w");
    if (file != NULL) {
        fprintf(file, "%f", balance);
        fclose(file);
    }
}
