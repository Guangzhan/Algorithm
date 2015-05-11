#include<stdio.h>

struct example1
{
	short a;
	long b;
};

struct stu
{
	
} a;
struct example2

{
	char c;
	example1 struct1;
	short e;	
};

int main(int argc, char*argv[])

{
	struct stu *b = &a;
	printf("%d\n", sizeof(a));
	printf("%d\n", sizeof(b));
	printf("+++++++++++\n");

	
	example2 e2;
	printf("%d\n", sizeof(short));
	printf("%d\n", sizeof(long));
	printf("%d\n", sizeof(e2.struct1));
	printf("**********\n");
	
	int d=(unsigned int)&e2.struct1-(unsigned int)&e2.c;
	
	printf("%d,%d,%d\n",sizeof(example1),sizeof(example2),d);
	
	return 0;
	
}
