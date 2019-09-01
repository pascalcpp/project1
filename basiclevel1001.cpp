#include<iostream>
int main()
{
	int n, count;
	count = 0;
	cin>>n;
	while (n > 1)
	{
		if (n % 2)
			n = (n * 3 + 1) / 2;
		else
			n = n / 2;
		count++;


	}
	cout<<count;
	return 0;
}
