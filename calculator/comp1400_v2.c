// if math.h functions are undefined, compile with "-lm" suffix => gcc -Wall clc_v2.c -lm
// scanf method was found on https://www.w3schools.com/c/ref_stdio_scanf.php

#include <stdio.h>
#include <stdbool.h>
#include <math.h>

void clearBuffer();
char menu(int version);
double caseB(double num1, char operator, double num2, double variables[5], bool optA);
double caseU(double num, char operator, double variables[5], bool optA);
bool caseE(bool optA);
double setNum(bool optA, double variables[5]);
double isValid(double num, char operator, double variables[5], bool optA);


int main(void){
    char option;
    char operator;
    double num1 = 0, num2 = 0;
    char var;
    double variables[5] = {0};
    bool optA = false;

    // Starting menu
    option = menu(1);

    while (true){
        switch (option){
        case 'B':
        // printf("Case B\n");
        
            num1 = setNum(optA, variables);

            clearBuffer(); // removes all extra characters from buffer

            printf("Enter an operator ( + , - , * , / , %%, P, X, I ): "); // Operator
            while(scanf("%1[+-*/%PXI]", &operator) == 0){// the "1" prevents stack smashing if many correct options are submitted
                printf("Invalid input. Please enter an operator: ");
                clearBuffer(); // removes all extra characters from buffer
            }
            
            clearBuffer(); // removes all extra characters from buffer

            num2 = setNum(optA, variables);
            
            printf("The result is %lf\n", caseB(num1, operator , num2, variables, optA));

            clearBuffer(); // removes all extra characters from buffer
            break; // break for Case B
        
        case 'U':
        // printf("Case U\n");
            printf("Enter an operator ( S , L , E , C , F ): ");
            while(scanf("%1[SLECF]", &operator) == 0){// the "1" prevents stack smashing if many correct options are submitted
                printf("Invalid input. Please enter an operator: ");
                clearBuffer(); // removes all extra characters from buffer
            }

            clearBuffer(); // removes all extra characters from buffer

            num1 = setNum(optA, variables);
            printf("The result is %lf", caseU(num1, operator, variables, optA));

            clearBuffer(); // removes all extra characters from buffer
            break; // break for Case U
        
        case 'A':
        // printf("Case A\n");
            optA = true; // activates optionA
            break;  // break for Case A

        case 'V':
        // printf("Case V\n");
            printf("Enter a variable (a, b, c, d, e): ");
            while(scanf("%1[abcde]", &var) == 0){// the "1" prevents stack smashing if many correct options are submitted
                printf("Invalid input. Please enter a variable: ");
                clearBuffer(); // removes all extra characters from buffer
            }

            double tmp = 0;
            printf("Enter a number: ");
            
            while(scanf("%lf", &tmp) == 0){
                printf("Invalid input. Please enter a number: ");
                clearBuffer(); // removes all extra characters from buffer
            }
            variables[var % 97] = tmp; // since a(97), b(98), ..., e(101), when you mod by 97, you get the position the variables would be in the array

            clearBuffer(); // removes all extra characters from buffer
            break;  // break for Case V
        
        case 'E':
        // printf("Case E\n");
            if(caseE(optA)){ // return to starting menu
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
            option = menu(3);
        }
        else{
            option = menu(2);
        }
    }

    return 0;
}

void clearBuffer(){
    while(getchar() != '\n');
}

char menu(int version){
    char option;
    
    if(version == 1){
        printf("Select one of the following items:\n");
        printf("B) Binary Mathematical Operations, such as addition and subtraction.\n");
        printf("U) Unary Mathematical Operations, such as square root, and log.\n");
        printf("A) Advances Mathematical Operations, using variables, arrays.\n");
        printf("V) Define variables and assign them values.\n");
        printf("E) Exit\n");
    }
    else if(version == 2){
        printf("Please select your option ( B , U , A , V , E ): ");
    }
    else if(version == 3){
        printf("Please select your option ( B , U , E): ");
    }
    while( (version <= 2 && scanf("%1[BUAVE]", &option) == 0) || (version == 3 && scanf("%1[BUE]", &option) == 0) ){ // the "1" prevents stack smashing if many correct options are submitted
        printf("Incorrect option. Please try again: ");
        clearBuffer();
    }

    clearBuffer();
    return option;
}

double caseB(double num1, char operator, double num2, double variables[5], bool optA){
    double result = 0;

    switch (operator){
    case '+': // add
        result = num1 + num2;
        break;
    case '-': // sub
        result = num1 - num2;
        break;
    case '*': // multiply
        result = num1 * num2;
        break;
    case '/': // division
        result = num1 / isValid(num2, operator, variables, optA);
        break;
    case '%': // remainder division (modulo)
        result = fmod(num1, isValid(num2, operator, variables, optA));
        break;
    case 'P': // power
        result = pow(num1, num2);
        break;
    case 'X': // max
        result = fmax(num1, num2);
        break;
    case 'I': // min
        result = fmin(num1, num2);
        break;
    }
    return result;
}

double caseU(double num, char operator, double variables[5], bool optA){
    double result = 0;

    switch (operator){
    case 'S': // sqrt
        result = sqrt(isValid(num, operator, variables, optA));
        break;
    case 'L': // log base e
        result = log(isValid(num, operator, variables, optA));
        break;
    case 'E': // e^x
        result = exp(num);
        break;
    case 'C': // ceiling
        result = ceil(num);
        break;
    case 'F': // floor
        result = floor(num);
        break;
    }
    return result;
}

bool caseE(bool optA){
    if(optA == true){
        return true;
    }
    return false;
}

double setNum(bool optA, double variables[5]){
    double num = 0;
    char var;

    if(optA == false){
        printf("Enter a number: ");
        while (scanf("%lf", &num) == 0){
            printf("Invalid input. Please enter a number: ");
            clearBuffer(); // removes all extra characters from buffer
        }
    }
    else{
        printf("Enter a number or variable: ");
        while(true){
            if(scanf("%lf", &num) == 0){ // Proceeds if no number was scanned
                if(scanf("%1[abcde]", &var) > 0){ // the "1" prevents stack smashing if many correct options are submitted
                    num = variables[var % 97]; // since a(97), b(98), ..., e(101), when you mod by 97, you get the position the variables would be in the array
                    break; // breaks while loop
                }
                else{
                    printf("Invalid input. Please enter a number or variable: ");
                    clearBuffer(); // removes all extra characters from buffer
                }
            }
            else{
                break; // breaks while loop
            }
        }  
    }
    return num;
}

double isValid(double num, char operator, double variables[5], bool optA){
    char var;

    while((operator == '/'|| operator == '%') && num == 0){
        if(optA == false){
            printf("Attempted division by 0. Please enter a non-zero number: ");
        }
        else{
            printf("Attempted division by 0. Please enter a non-zero number/variable: ");
        }
        if(scanf("%lf", &num) == 0){ // Proceeds if no number was scanned
            if(scanf("%1[abcde]", &var) > 0){// the "1" prevents stack smashing if many correct options are submitted
                num = variables[var % 97]; // since a(97), b(98), ..., e(101), when you mod by 97, you get the position the variables would be in the array
            }
            else{
                clearBuffer(); // removes all extra characters from buffer
            }
        }
    }
    
    while((operator == 'L' && num <= 0) || (operator == 'S' && num < 0)){ // Prevents sqrt and ln of negative numbers, and ln of 0
        if(optA == false){
            printf("Attempted ln or sqrt on an invalid number. Please enter a positive number: ");
        }
        else{
            printf("Attempted ln or sqrt on a invalid number/variable. Please enter a positive number/variable: ");
        }
        if(scanf("%lf", &num) == 0){ // Proceeds if no number was scanned
            if(scanf("%1[abcde]", &var) > 0){// the "1" prevents stack smashing if many correct options are submitted
                num = variables[var % 97]; // since a(97), b(98), ..., e(101), when you mod by 97, you get the position the variables would be in the array
            }
            else{
                clearBuffer(); // removes all extra characters from buffer
            }
        }
    }
    
    return num;
}
