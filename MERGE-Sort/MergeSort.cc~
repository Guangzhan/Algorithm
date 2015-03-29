#include<iostream>
#include<cstdlib>
#include<limits.h>
#include<cstdio>
using namespace std;

void Merge(int *arr, int p, int q, int r)
{
	
	int n1 = q - p + 1;		//第一个有序子数组元素个数
	int n2 = r - q;			//第二个有序子数组元素个数
	int *Left = (int *)malloc(sizeof(int)*(n1 + 1));
	int *Right = (int *)malloc(sizeof(int)*(n2 + 1));
	
	//将子数组复制到临时辅助空间
	for(int i=0; i<n1; i++){
		Left[i] = arr[p+i];
	}
	
	for(int j=0; j<n2; j++){
		Right[j] = arr[q+j+1];
	}
	
	//添加哨兵
	Left[n1] = INT_MAX;
	Right[n2] = INT_MAX;
	
	//从第一个元素开始合并
	int i = 0;
	int j = 0;
	for(int k=p; k<=r; k++){
		if(Left[i] <= Right[j])
		{
			arr[k] = Left[i];
			++i;
		}
		else{
			arr[k] = Right[j];
			++j;
		}
	}
	free(Left);
	free(Right);
}

void MergeSort(int *arr, int p, int r)
{
	if(p < r){
		int q = (p + r) / 2;
		MergeSort(arr, p , q);
		MergeSort(arr, q + 1, r);
		Merge(arr, p, q, r);
	}

}

int  main(){
	int arr[8] = {2, 4, 5, 7, 1, 2, 3, 6};
	MergeSort(arr, 0,  7);
	for(int i=0; i<8; i++)
	{
		cout<< arr[i] << " ";
	}
	cout << endl;
	return 0;
}


