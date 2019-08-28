#include<stdio.h>
int main()
{
	int n, count;
	count = 0;
	scanf("%d", &n);
	while (n > 1)
	{
		if (n % 2)
			n = (n * 3 + 1) / 2;
		else
			n = n / 2;
		count++;


	}
	printf("%d",count);
	return 0;
}
