void SelectionSort(int a[] ,int size)
{
for( int i = 0; i < size - 1; ++i ){
int tmpMin = i;

for( int j = i+1; j < size ; ++j) {
if( a[j] < a[tmpMin] )
tmpMin = j;
}

int tmp = a[i];
a[i] = a[tmpMin];
a[tmpMin] = tmp;
}
} 
