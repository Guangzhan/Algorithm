#include<iostream>
#include<cstdio>
#include<cstdlib>
using namespace std;

void insertionSort(int *arr, int length){
	//判断参数是否合法
	if(arr == NULL || 0==length)
    {
        printf("Check datas or length.\n");
        exit(1);
    }
	//数组下标是从0开始的，从第二个元素（对应下标1）开始向前插入
	for(int j=1; j<length; j++)
	{
		int key = arr[j];			 //记录当前要插入的元素
		int i = j - 1;				 //前面已经有序的元素
		//寻找待插入元素的位置，从小到到排序，如果是从大到小改为arr[i]<key
		while(i>=0 && arr[i]>key)
		{
			arr[i+1] = arr[i];
			i--;					 //向前移动
		}
		arr[i+1] = key;
	}
}

int main()
{
	int arr[10] = {9, 7, 6, 8, 18, 21, 5, 10, 43, 11};
	insertionSort(arr, 10);
	for(int i=0; i<10; i++)
	{
		cout << arr[i] << " ";
	}
	cout << endl;
	return 0;
}
