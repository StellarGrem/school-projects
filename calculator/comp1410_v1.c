#include <stdio.h>

void clearBuffer(){
    while(getchar() != '\n');
}

void bubble(float array[], int len){ // used to sort the array of student scores; making it easier to find max, median
    int swap;
    do{
        swap = 0;
        for(int i = 0; i < len - 1; i++){
            int tmp = array[i];
            if(tmp > array[i + 1]){
                array[i] = array[i + 1];
                array[i + 1] = tmp;
                swap = 1;
            }
        }
    } while(swap == 1);
}

/*  could have used <math.h> version of round, but compiling doesn't work without "-lm" suffix, and since 
    not compiling risks not getting graded. I didn't want that, so I made my own instead.
*/
int round(double grade){ 
    int tmp = (int)grade; // converting to int removes numbers after decimal
    float diff = grade - tmp; // leaves only numbers after decimal
    if(diff >= 0.5){
        return tmp + 1; // round up
    }
    else{
        return tmp; // round down
    }
}

int menu(){
    int choice = 0;
    printf("======================================\nWeighted Grade Calculation Program\n======================================\n");
    printf("1. Single Student\n2. Multiple Students\n3. Exit\n");
    printf("Enter your choice (1/2/3): ");
    while(scanf("%d", &choice) == 0 || choice < 1 || choice > 3){
        clearBuffer();
        printf("Invalid choice. Choose 1, 2 or 3: ");
    }
    return choice;
}

void letterGrade(int grade){
    char letter[6] = {'F','D','C','B','A'};// 0-40, 50, 60, 70 , 80
    char sign[4] = {'-',' ','+'}; // <5, 0, >=5

    if(grade < 60){ // Letter only - no signs needed
        printf("\tLetter Grade: %c",letter[grade/50]);
        /*  Since F and D are in position 0 and 1 (respectively) in the array
            Since F is 0-49, dividing by 50 will return 0 and D (50-59) will
            return 1 when divided by 50. 
            So grade/50 will return the correct position for the grade
        */
    }
    else if(grade < 80){ // Letter grade C (60-64) to B+ (75-79)
        printf("\tLetter Grade: %c%c",letter[grade/10 - 4], sign[(grade%10)/5 + 1]);
        /*  if we act that F is 40, C is 50, ..., A is 80.
            By doing the operation of (grade/10) - 4, we get the position of the corresponding grade in the array
            We don't have to worry about the grade being <40 since it's taken care of in the first if statement

            Grades that have a "+" sign ends with 5-9, thus by %10, we get the last digit
            By dividing by 5, we will get 1 if it ends with 5-9. Otherwise it's 0.
            We add 1 to get the correct sign from the array since we are off by 1 in the array without doing so
        */
    }
    else{ // Letter grade A (80 - 100)
        printf("\tLetter Grade: %c%c",letter[4],sign[grade/85 + (grade >= 90 ? 1 : 0)]);
        /*  Since the case (without a sign) has a minimum of 85. By dividing by 85, we get 0 or 1.
            (grade >= 90 ? 1 : 0) acts like an if statement, if grade >= 90. It will add 1 if true, 0 otherwise.
                this ensures we only add "+" sign if the grade is >=90
            
            80-84: 0 + 0 = 0 = '-'
            85-89: 1 + 0 = 1 = ' '
            90-100: 1 + 1 = 2 = '+'
        */
    }
    printf("\n");
}

// recursion function
double finalGrade(float points[][3],int n, int size){
    if(n == size){
        return 0;
    }
    return (points[n][2]/points[n][1])*(points[n][0]/100) + finalGrade(points, n+1, size); // (Earned Score / MaxPoint)*(Weight/100)
}

void studentGrade(char name[][100], float score[][3], int size, int option){
    int numStudents = -1;
    if(option == 1){ // single student
        printf("-- Summary of Score --\n");
        numStudents = 1;
    }
    else{ // multiple students
        printf("Number of students: ");
        while(scanf("%d", &numStudents) == 0 || numStudents < 0){
            clearBuffer();
            printf("Invalid number of students. Enter a positive number: ");
        }
    }
    float studentScores[numStudents]; // array of student scores (for multiple students)

    for(int j = 0; j < numStudents; j++){
        if(option == 2){
            printf("-- Student %d --\n", j+1);
        }

        for(int i = 0; i < size; i++){
            printf("\tScore for \"%s\": ", name[i]);
            while(scanf("%f", &score[i][2]) == 0 || score[i][2] < 0 || score[i][2] > score[i][1]){ // score[i][2] = score; score[i][1] = max allocated point
                clearBuffer();
                printf("Invalid score. Enter a score between 0 and %.f (inclusively): ", score[i][1]);
            }
            clearBuffer();
        }

        double grade = finalGrade(score, 0, size)*100;
        int rGrade = round(grade); // rounded grade
        printf("\tFinal Weighted Grade: %d%%\n", rGrade);
        letterGrade(rGrade);
        studentScores[j] = rGrade;
    }

    if(option == 2){ // multiple students
        bubble(studentScores, numStudents); // bubble sorts array (least to greatest) so that it's easier to find median and maximum
        printf("Class Summary:\n");
        printf("\tMaximum: %.2f\n", studentScores[numStudents-1]);

        float avg = 0;
        for(int i = 0; i < numStudents; i++){
            avg += studentScores[i];
        }   
        printf("\tAverage: %.2f\n", avg/numStudents);

        printf("\tMedian: %.2f\n", numStudents % 2 == 0 ? (studentScores[numStudents/2]+studentScores[numStudents/2-1])/2 : studentScores[numStudents/2]);
    }

}

int components(int option){
    int n;
    printf("Number of components: ");
    while(scanf("%d", &n) == 0 || n < 0){
        clearBuffer();
        printf("Invalid number of components. Enter a positive number: ");
    }
    clearBuffer();

    char name_arr[n][100]; // n rows by 100 columns
    float score_arr[n][3]; // n rows by 3 columns (weight, max point, score)

    int maxWeight = 100; // max weight that can be assigned
    for(int i = 0; i < n; i++){ // row (each task)
        printf("Component %d:\n", i+1);
        printf("\tName: ");
        scanf("%[^\n]", name_arr[i]); // reads up to but not including \n
        clearBuffer();
        
        printf("\tWeight: ");
        while(scanf("%f", &score_arr[i][0]) == 0 || score_arr[i][0] < 0 || score_arr[i][0] > maxWeight || (score_arr[i][0] != maxWeight && i+1 == n)){ // score[i][0] = weight
            clearBuffer();
            i+1 == n ? printf("Invalid weight. Choose %d as your weight: ", maxWeight) : printf("Invalid weight. Choose between 0 and %d (inclusive): ", maxWeight);
        }
        maxWeight -= score_arr[i][0]; // score[i]0] = weight

        printf("\tMax Allocated Point: ");
        while(scanf("%f", &score_arr[i][1]) == 0 || score_arr[i][1] < 0){
            clearBuffer();
            printf("Invalid score. Enter a positive number: ");
        }
        clearBuffer();
    }
    
    studentGrade(name_arr, score_arr, n, option);
    return 0;
}


int main(){
    while(1){
        switch (menu()){
        case 1: // Single student
            components(1);
            break;
        case 2: // Multiple students
            components(2);
            break;
        case 3: // exit
            printf("\n--- HAVE A GOOD DAY! ---\n========================\n");
            return 0;
        }
        printf("\n");
    }
}
