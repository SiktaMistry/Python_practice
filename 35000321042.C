//35000321042_SiktaMistry
#include<stdio.h>

typedef struct students{
	char name[30];
	int roll;
	char address[100];
	char dept[30];
	char grade;
}std;

int main()
{
	std num[5];	int i; int j;
	for(i=0;i<5;i++){
		printf("Enter the name of the student:\n");
		scanf("%s",&num[i].name);
		printf("Enter the roll of the student:\n");
		scanf("%d",&num[i].roll);
		printf("Enter the address of the student:\n");
		scanf("%s",&num[i].address);
		printf("Enter the department of the student:\n");
		scanf("%s",&num[i].dept);
		printf("Enter the grade of the student:\n");
		scanf("%s",&num[i].grade);
		
	}
	for(i=0;i<5;i++){
    if(num[i].grade=="A"){
    	printf("%s have received grade 'A'\n",num[i].name);
	}
}
	return 0;
}
