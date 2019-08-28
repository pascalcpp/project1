#include<stdio.h>
#include<math.h>
double eps = 1e-6;
double f(double x){ return x*x*x - 5 * x*x + 10 * x - 80; }
int main()
{
	double root, x1 = 0, x2 = 100, y;
	root = x1 + (x2 - x1) / 2;
	int triedtimes = 1;
	y = f(root);
	while (fabs(y) > eps)
	{
		if (y > 0)  x2 = root;
		else x1 = root;
		root = x1 + (x2 - x1) / 2;
		y = f(root);
		triedtimes++;
	}
	printf("%.8f\n",root);
	printf("%d",triedtimes);  // O(log2 n)
	
	return 0;
}
