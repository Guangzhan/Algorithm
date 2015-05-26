#include <stdio.h>
#include <stdlib.h>

size_t partition(int* datas,int beg,int last);
void quick_sort(int* datas,int beg,int last);
void swap(int *a,int *b);

int main()
{
    size_t i;
    int datas[10] = {78,13,9,23,45,14,35,65,56,79};
    printf("After quick sort,the datas is:\n");
    quick_sort(datas,0,9);
    for(i=0;i<10;++i)
        printf("%d ",datas[i]);
    exit(0);
}

void swap(int *a,int *b)
{
    int temp = *a;
    *a = *b;
    *b = temp;
}

size_t partition(int* datas,int beg,int last)
{
    int pivot = datas[last];
    int i,j;
    i = beg -1;
    for(j=beg;j<last;j++)
    {
        if(datas[j] < pivot)
        {
            i = i+1;
            swap(datas+i,datas+j);
        }
    }
    swap(datas+i+1,datas+last);
    return (i+1);
}
void quick_sort(int* datas,int beg,int last)
{
    int pivot;
    if(beg < last)
    {
        pivot = partition(datas,beg,last);
        quick_sort(datas,beg,pivot-1);
        quick_sort(datas,pivot+1,last);
    }

}
