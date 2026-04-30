// Student ID: 110199280
// Student Name: Samuel Huang
// if math.h functions are undefined, compile with "-lm" suffix => gcc -Wall clc.c -lm

#include <stdio.h>
#include <stdbool.h>
#include <math.h>

int main(void){
    char option;
    char operator;
    double num1, num2 = 0;
    char var;
    double a = 0,b = 0,c = 0,d = 0,e = 0;
    bool optA = false;

    // Starting menu
    printf("Select one of the following items:\n");
    printf("B) Binary Mathematical Operations, such as addition and subtraction.\n");
    printf("U) Unary Mathematical Operations, such as square root, and log.\n");
    printf("A) Advanced Mathematical Operations, using variables, arrays.\n");
    printf("V) Define variables and assign them values.\n");
    printf("E) Exit\n");
    while(true){
        scanf("%c", &option);
        while(getchar() != '\n'); // removes all characters from buffer
        if (option == 'B' || option == 'U' || option == 'A' || option == 'V' || option == 'E'){
            break;
        }
        else{
            printf("Invalid option. Please try again: ");
        }
    }

    while (true){
        switch (option){
        case 'B':
        // printf("Case B\n");
            if(optA == false){ // Number 1
                printf("Enter a number: ");
                while (scanf("%lf", &num1) == 0){
                    printf("Invalid input. Please enter a number: ");
                }
            }
            else{
                printf("Enter a number or variable: ");
                while(true){
                    if(scanf("%lf", &num1) == 0){ // Proceeds if no number was scanned
                        scanf("%c", &var);
                        if(var >= 97 && var <= 101){ // a (97) - e (101)
                            switch(var){
                            case 'a':
                                num1 = a;
                                break;
                            case 'b':
                                num1 = b;
                                break;
                            case 'c':
                                num1 = c;
                                break;
                            case 'd':
                                num1 = d;
                                break;
                            case 'e':
                                num1 = e;
                                break;
                            }
                            break; // breaks while loop
                        }
                        else{
                            printf("Invalid input. Please enter a number or variable: ");
                            while (getchar() != '\n'); // removes all extra characters from buffer
                        }
                    }
                    else{
                        break; // breaks while loop
                    }
                }  
            }

            while (getchar() != '\n'); // removes all extra characters from buffer

            printf("Enter an operator ( + , - , * , / , %% ): "); // Operator
            while(true){
                scanf("%c", &operator);
                if(operator == '+' || operator == '-' || operator == '*' || operator == '/' || operator == '%' || operator == 'P' || operator == 'X' || operator == 'I'){
                    break;
                }
                else{
                    printf("Invalid input. Please enter an operator: ");
                    while (getchar() != '\n'); // removes all extra characters from buffer
                }
            }

            if(optA == false){ // Number 2
                printf("Enter a number: ");
                while (scanf("%lf", &num2) == 0){ // Ensures number is inputted
                    printf("Invalid input. Please enter a number: ");
                    while (getchar() != '\n'); // removes all extra characters from buffer
                }
            }
            else{
                printf("Enter a number or variable: ");
                while(true){
                    if(scanf("%lf", &num2) == 0){ // Proceeds if no number was scanned
                        scanf("%c", &var);
                        if(var >= 97 && var <= 101){ // a (97) - e (101)
                            switch(var){
                            case 'a':
                                num2 = a;
                                break;
                            case 'b':
                                num2 = b;
                                break;
                            case 'c':
                                num2 = c;
                                break;
                            case 'd':
                                num2 = d;
                                break;
                            case 'e':
                                num2 = e;
                                break;
                            }
                            break; // breaks while loop
                        }
                        else{
                            printf("Invalid input. Please enter a number or variable: ");
                            while (getchar() != '\n'); // removes all extra characters from buffer
                        }
                    }
                    else{
                        break; // breaks while loop
                    }
                }
            }

            if(operator == '/' || operator == '%'){ // Prevents division by 0
                while (num2 == 0){
                    if(optA == false){
                        printf("Attempted division by 0. Please enter a non-zero number: ");
                    }
                    else{
                        printf("Attempted division by 0. Please enter a non-zero number/variable: ");
                    }
                    if(scanf("%lf", &num2) == 0){ // Proceeds if no number was scanned
                        scanf("%c", &var);
                        if(var >= 97 && var <= 101){ // a (97) - e (101)
                            switch(var){
                            case 'a':
                                num2 = a;
                                break;
                            case 'b':
                                num2 = b;
                                break;
                            case 'c':
                                num2 = c;
                                break;
                            case 'd':
                                num2 = d;
                                break;
                            case 'e':
                                num2 = e;
                                break;
                            }
                            
                        }
                        else{
                            while (getchar() != '\n'); // removes all extra characters from buffer
                        }
                    }
                }
            }

            switch (operator){
            case '+': // add
                printf("The result is %0.2lf\n", num1 + num2);
                break;
            case '-': // sub
                printf("The result is %0.2lf\n", num1 - num2);
                break;
            case '*': // multiply
                printf("The result is %0.2lf\n", num1 * num2);
                break;
            case '/': // division
                printf("The result is %0.2lf\n", num1 / num2);
                break;
            case '%': // remainder division (modulo)
                printf("The result is %lf\n", fmod(num1, num2));
                break;
            case 'P': // power
                printf("The result is %lf\n", pow(num1, num2));
                break;
            case 'X': // max
                printf("The result is %lf\n", fmax(num1, num2));
                break;
            case 'I': // min
                printf("The result is %lf\n", fmin(num1, num2));
                break;
            }

            while (getchar() != '\n'); // removes all extra characters from buffer
            break; // break for Case B

        case 'U':
        // printf("Case U\n");
            printf("Enter an operator ( S , L , E , C , F ): ");
            while(true){
                scanf("%c", &operator);
                if(operator == 'S' || operator == 'L' || operator == 'E' || operator == 'C' || operator == 'F'){
                    break;
                }
                else{
                    printf("Invalid input. Please enter an operator: ");
                    while (getchar() != '\n'); // removes all extra characters from buffer
                }
            }

            if(optA == false){
                printf("Enter a number: ");
                while (scanf("%lf", &num1) == 0){
                    printf("Invalid input. Please enter a number: ");
                }
            }
            else{
                printf("Enter a number or variable: ");
                while(true){
                    if(scanf("%lf", &num1) == 0){ // Proceeds if no number was scanned
                        scanf("%c", &var);
                        if(var >= 97 && var <= 101){ // a (97) - e (101)
                            switch(var){
                            case 'a':
                                num1 = a;
                                break;
                            case 'b':
                                num1 = b;
                                break;
                            case 'c':
                                num1 = c;
                                break;
                            case 'd':
                                num1 = d;
                                break;
                            case 'e':
                                num1 = e;
                                break;
                            }
                            break; // breaks while loop
                        }
                        else{
                            printf("Invalid input. Please enter a number or variable: ");
                            while (getchar() != '\n'); // removes all extra characters from buffer
                        }
                    }
                    else{
                        break; // breaks while loop
                    }
                }
            }

            while((operator == 'L' && num1 <= 0) || (operator == 'S' && num1 < 0)){ // Prevents sqrt and ln of negative numbers, and ln of 0
                if(optA == false){
                    printf("Attempted ln or sqrt on an invalid number. Please enter a positive number: ");
                    scanf("%lf",&num1);
                }
                else{
                    printf("Attempted ln or sqrt on a invalid number/variable. Please enter a positive number/variable: ");
                    while(true){
                        if(scanf("%lf", &num1) == 0){ // Proceeds if no number was scanned
                            scanf("%c", &var);
                            if(var >= 97 && var <= 101){ // a (97) - e (101)
                                switch(var){
                                case 'a':
                                    num1 = a;
                                    break;
                                case 'b':
                                    num1 = b;
                                    break;
                                case 'c':
                                    num1 = c;
                                    break;
                                case 'd':
                                    num1 = d;
                                    break;
                                case 'e':
                                    num1 = e;
                                    break;
                                }
                                break; // breaks while loop
                            }
                            else{
                                while (getchar() != '\n'); // removes all extra characters from buffer
                            }
                        }
                        else{
                            break; // breaks while loop
                        }
                    }
                }
            }

            switch (operator){
            case 'S': // sqrt
                printf("The result is %0.2lf\n", sqrt(num1));
                break;
            case 'L': // log base e
                printf("The result is %0.2lf\n", log(num1));
                break;
            case 'E': // e^x
                printf("The result is %0.2lf\n", exp(num1));
                break;
            case 'C': // ceiling
                printf("The result is %0.2lf\n", ceil(num1));
                break;
            case 'F': // floor
                printf("The result is %0.2lf\n", floor(num1));
                break;
            }

            while (getchar() != '\n'); // removes all extra characters from buffer
            break; // break for Case U

        case 'A':
        // printf("Case A\n");
            optA = true; // activates optionA
            break;  // break for Case A

        case 'V': //No arrays
        // printf("Case V\n");
            printf("Enter a variable (a, b, c, d, e): ");
            while(true){
                scanf("%c", &var);
                if(var >= 97 && var <= 101){ // a - e (their decimal values)
                    break;
                }
                else{
                    printf("Invalid input. Please enter a variable: ");
                    while (getchar() != '\n'); // removes all extra characters from buffer
                }
            }

            double tmp = 0;
            printf("Enter a number: ");
            
            while(scanf("%lf", &tmp) == 0){
                printf("Invalid input. Please enter a number: ");
                while (getchar() != '\n'); // removes all extra characters from buffer
            }
            if(var == 'a'){a = tmp;}
            else if(var == 'b'){b = tmp;}
            else if(var == 'c'){c = tmp;}
            else if(var == 'd'){d = tmp;}
            else if(var == 'e'){e = tmp;}

            while (getchar() != '\n'); // removes all extra characters from buffer
            break;  // break for Case V

        case 'E':
        // printf("Case E\n");
            if(optA == true){ // return to starting menu
                optA = false;
                break;
            } 
            else{
                printf("Thanks for using my Simple Calculator. Hope to see you soon again, Goodbye!\n");
                return 0;
            }
        } // End of switch

        printf("\n"); // newline for legibility in terminal between new and old calculations

        if(optA == true){
            printf("Enter an option (B, U, E): ");
        }
        else{
            printf("Please select your option ( B , U , A , V , E ): ");
        }
        while(true){
            scanf("%c", &option);
            while(getchar() != '\n'); // removes all extra characters from buffer

            if (option == 'B' || option == 'U' || option == 'A' || option == 'V' || option == 'E'){
                break;
            }
            else{
                printf("Invalid option. Please try again: ");
            }
        }
    }

    return 0;
}
