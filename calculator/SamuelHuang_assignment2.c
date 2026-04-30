#include <stdio.h>
#include <stdlib.h>
#include <string.h>

typedef struct{
    float grade; // grade
    int rgrade; // rounded grade
    char letter[3]; // letter grade
} Grade;

typedef struct{
    float score;
    int maxpoint;
    int weight;
    char name[50];
} Assessment;

typedef struct{ 
    Assessment* components;
    Grade finalGrade;
    int numComponents;
    char name[50];
}Student;

void clearBuffer(){
    while(getchar() != '\n');
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
    printf("1. Single Student\n2. Multiple Students\n3. Sort Students by Grade\n4. Search for a student\n5. Exit\n");
    printf("Enter your choice (1/2/3/4/5): ");
    while(scanf("%d", &choice) == 0 || choice < 1 || choice > 5){
        clearBuffer();
        printf("Invalid choice. Choose 1, 2, 3, 4 or 5: ");
    }
    clearBuffer();
    return choice;
}

void bubble(Student* students, int size, int option){ // used to sort the array of student scores; making it easier to find max, median
    int swap;
    do{
        swap = 0;
        for(int i = 0; i < size ; i++){
            Student tmp = students[i];
            if(tmp.finalGrade.rgrade < students[i + 1].finalGrade.rgrade){
                students[i] = students[i + 1];
                students[i + 1] = tmp;
                swap = 1;
            }
        }
    } while(swap == 1);

    if(option == 3){
        printf("\n======================================\nSorting students by final grade...\n======================================\n");
        printf("Class Ranking:\n");
        for(int i = 0; i < size; i++){
            printf("%d. %s - %d%% (%s)\n", i+1, students[i].name, students[i].finalGrade.rgrade, students[i].finalGrade.letter);
        }
    }   
}

void searchStudent(Student* students, int len){ // search algorithm
    char name[50];
    printf("\nEnter student name to search: ");
    scanf("%[^\n]", name);
    for(int i = 0; i < len; i++){
        if(strcmp(students[i].name, name) == 0){
            printf("Result: %s - %d%% (%s)\n", students[i].name, students[i].finalGrade.rgrade, students[i].finalGrade.letter);
            return;
        }
    }
    printf("Student \"%s\" not found.\n", name);
}

void summary(Student* students, int size, int option){
    if(option == 1){ // single student
        printf("\n-- Summary of Score --\n");
        printf("Final Weighted Grade: %d%%\n", students[0].finalGrade.rgrade);
        printf("Letter Grade: %s\n", students[0].finalGrade.letter);
    } else{
        printf("\nClass Summary:\n");
        for(int i = 0; i < size; i++){
            printf("%s - %d%% (%s)\n", students[i].name, students[i].finalGrade.rgrade, students[i].finalGrade.letter);
        }

        bubble(students, size, option); // bubble sorts array (greatest to least) so that it's easier to find median and maximum
        printf("\nMaximum: %d (Students: ", students[0].finalGrade.rgrade);
        for(int i = 0; i < size; i++){
            if(students[i].finalGrade.rgrade == students[0].finalGrade.rgrade){
                printf("%s", students[i].name);
                if(students[i+1].finalGrade.rgrade == students[0].finalGrade.rgrade){
                    printf(", ");
                }
            }
        }
        printf(")\n");

        float avg = 0;
        for(int i = 0; i < size; i++){
            avg += students[i].finalGrade.rgrade;
        }  
        printf("Average: %.2lf\n", avg/size);
    
        printf("Median: %d\n", size % 2 == 0 ? (students[size/2].finalGrade.rgrade + students[size/2-1].finalGrade.rgrade)/2 : students[size/2].finalGrade.rgrade);
    }
}

void letterGrade(int grade, char* letGrd){
    char letter[5] = {'F','D','C','B','A'};// 0-40, 50, 60, 70 , 80
    char sign[3] = {'-',' ','+'}; // <5, 0, >=5
    
    if(grade < 60){ // Letter only - no signs needed
        // printf("\tLetter Grade: %c",letter[grade/50]);
        *(letGrd+0) = letter[grade/50];
        *(letGrd+1) = sign[1];
    }
    else if(grade < 80){ // Letter grade C (60-64) to B+ (75-79)
    //     printf("\tLetter Grade: %c%c",letter[grade/10 - 4], sign[(grade%10)/5 + 1]);
        *(letGrd+0) = letter[grade/10 - 4];
        *(letGrd+1) = sign[(grade%10)/5 + 1];
    }
    else{ // Letter grade A (80 - 100)
        // printf("\tLetter Grade: %c%c",letter[4],sign[grade/85 + (grade >= 90 ? 1 : 0)]);
        *(letGrd+0) = letter[4];
        *(letGrd+1) = sign[grade/85 + (grade >= 90 ? 1 : 0)];
    }
    // printf("\n");
    if(*(letGrd+1) == ' '){ // purely for visual fix, (B) instead (B )
        *(letGrd+1) = '\0';
    } else{
        *(letGrd+2) = '\0'; // add \0 to the end, otherwise printf("%s") will print unnecessary letters
    }
}

// recursion function
double finalGrade(Assessment* components,int n, int size){
    if(n == size){
        return 0;
    }
    return ((float)components[n].score/components[n].maxpoint)*((float)components[n].weight/100) + finalGrade(components, n+1, size); // (Earned Score / MaxPoint)*(Weight/100)
}

Grade studentGrade(Student stu, Assessment* components){
    Grade fgrade;
    fgrade.grade = finalGrade(components, 0, stu.numComponents)*100;
    // printf("%lf\t", fgrade.grade);
    fgrade.rgrade = round(fgrade.grade);
    // printf("%d\t", fgrade.rgrade);
    letterGrade(fgrade.rgrade, fgrade.letter);
    // printf("%s\n", fgrade.letter);
    return fgrade;
}

Student setStudent(char name[50], int numComponents, Assessment* component, int option, int numStudent){
    Student stu;
    if(option == 1) strcpy(stu.name, name);
    stu.components = malloc(numComponents*sizeof(Assessment));
    stu.numComponents = numComponents;
    int maxWeight = 100;
    
    for(int i = 0; i < numComponents && numStudent == 1; i++){
        printf("Component %d:\n", i+1);
        printf("\tName: ");
        scanf("%[^\n]", component[i].name); // reads up to but not including \n
        strcpy(stu.components[i].name, component[i].name); // student copy
        clearBuffer();
        
        printf("\tWeight: ");
        while(scanf("%d", &component[i].weight) == 0 || component[i].weight <= 0 || component[i].weight > maxWeight || (component[i].weight != maxWeight && i+1 == numComponents)){
            clearBuffer();
            i+1 == numComponents ? printf("Invalid weight. Choose %d as your weight: ", maxWeight) : printf("Invalid weight. Choose between 1    and %d (inclusive): ", maxWeight);
        }
        stu.components[i].weight = component[i].weight; // student copy
        maxWeight -= component[i].weight;
        clearBuffer();
        
        printf("\tMax Allocated Point: ");
        while(scanf("%d", &component[i].maxpoint) == 0 || component[i].maxpoint <= 0){
            clearBuffer();
            printf("Invalid score. Enter a positive (non-zero) number: ");
        }
        stu.components[i].maxpoint = component[i].maxpoint; // student copy 
        clearBuffer();
        
        if(option == 1){
            printf("\tEarned Score: ");
            while(scanf("%f", &stu.components[i].score) == 0 || stu.components[i].score < 0 || stu.components[i].score > stu.components[i].maxpoint){
                clearBuffer();
                printf("Invalid score. Enter a score between 0 and %d (inclusively): ", component[i].maxpoint);
            }
            clearBuffer();
        }
        
        if(i+1 < numComponents){
            component = (Assessment*) realloc(component, (i+2)*sizeof(Assessment));
            if(component == NULL){
                printf("Reallocation failed\n");
            }
        }
    }
    
    if(option == 2){
        printf("\nEnter student's full name (or type DONE to stop): ");
        scanf("%[^\n]", stu.name);
        clearBuffer();
        if(strcmp(stu.name, "DONE") == 0) return stu;
        
        for(int i = 0; i < numComponents; i++){
            strcpy(stu.components[i].name, component[i].name); // student copy
            stu.components[i].weight = component[i].weight; // student copy
            stu.components[i].maxpoint = component[i].maxpoint; // student copy

            printf("Score for \"%s\": ", stu.components[i].name);
            while(scanf("%f", &stu.components[i].score) == 0 || stu.components[i].score < 0 || stu.components[i].score > stu.components[i].maxpoint){
                clearBuffer();
                printf("Invalid score. Enter a score between 0 and %d (inclusively): ", stu.components[i].maxpoint);
            }
            clearBuffer();
        }
    }
    stu.finalGrade = studentGrade(stu, stu.components);
    return stu;
}


Student* components(int option, Student* students, int* size){
    int n;
    char name[50];

    if(option == 1){
        printf("\nEnter Student's full name: ");
        scanf("%[^\n]", name);
        clearBuffer();
    }
    
    printf("\nEnter number of course components: ");
    while(scanf("%d", &n) == 0 || n <= 0){
        clearBuffer();
        printf("Invalid number of components. Enter a positive (non-zero) number: ");
    }
    clearBuffer();
    Assessment* component = (Assessment*) malloc(n*sizeof(Assessment)); // master component
    if(component == NULL){
        printf("Memory Reallocation failed\n");
        // return;
    }

    students = (Student*) malloc(sizeof(Student));
    if(students == NULL){
        printf("Memory Allocation failed\n");
        // return;
    }
    
    int j = 1;
    do{
        Student temp = setStudent(name, n, component, option, j);
        if(option == 1){
            students[j-1] = temp;
        }
        if(strcmp(temp.name, "DONE") != 0 && option == 2){ // only reallocates if name is not "DONE"
            students[j-1] = temp;
            students = (Student*) realloc(students, (j+1)*sizeof(Student));
            if(students == NULL){
                printf("Memory Reallocation failed\n");
            }
            j += 1;
        }
        else if(strcmp(temp.name, "DONE") == 0 && option == 2){
            option = 1; // just to break while loop, no other purposes
            students = (Student*) realloc(students, (j-1)*sizeof(Student)); // shrinks students by 1
            if(students == NULL){
                printf("Memory Reallocation failed\n");
            }
            j -= 1;
        }
    }while(option == 2);
    *size = j; // counter for number of students
    return students;
}


int main(){
    Student* students = NULL;
    int* numStudents;
    
    while(1){
        switch (menu()){
        case 1: // Single student
            if(students != NULL){
                free(students);
                students = NULL;
                // printf("FREE\n");
            }
            students = components(1, students, numStudents);
            summary(students, *numStudents, 1);
            break;
        case 2: // Multiple students
            if(students != NULL){
                free(students);
                students = NULL;
                // printf("FREE\n");
            }
            students = components(2, students, numStudents);
            summary(students, *numStudents, 2);
            break;
        case 3: // sort student by grade
            bubble(students, *numStudents, 3);
            break;
        case 4: // search for student
            if(students != NULL){
                searchStudent(students, *numStudents);
            } else{
                printf("No students in database. Try again after inputting student(s)\n");
            }
            break; 
        case 5: // exit
            printf("\n--- HAVE A GOOD DAY! ---\n========================\n");
            free(students);
            students = NULL;
            return 0;
        }
        printf("\n");
    }
}