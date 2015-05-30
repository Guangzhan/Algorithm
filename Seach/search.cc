#include <stdio.h>
#include <stdlib.h>
#include <string.h>

//非递归二叉查找
int binary_search(int *datas,int length,int obj)
{
    int low,mid,high;
    low = 0;
    high = length;
    while(low < high)
    {
        mid = (low + high)/2;
        if(datas[mid] == obj)
            return mid;
        else if(datas[mid] > obj)
            high = mid;
        else
            low = mid+1;
    }
    return -1;
}

//递归形式二分查找
int binary_search_recursive(int *datas,int beg,int end,int obj)
{
    int mid;
    if(beg < end)
    {
        mid = (beg+end)/2;
        if(datas[mid] == obj)
            return mid;
        if(datas[mid] > obj)
            return binary_search_recursive(datas,beg,mid,obj);
        else
            return binary_search_recursive(datas,mid+1,end,obj);

    }
    return -1;
}
//合并子程序
int merge(int *datas,int p,int q,int r)
{
    int n1 = q-p+1;
    int n2 = r-q;
    int *left = (int*)malloc(sizeof(int)*(n1+1));
    int *right = (int*)malloc(sizeof(int)*(n2+1));
    int i,j,k;
    memcpy(left,datas+p,n1*sizeof(int));
    memcpy(right,datas+q+1,n2*sizeof(int));
    i = 0;
    j = 0;
    for(k=p;k<=r;++k)
    {
        if(i <n1 && j< n2)
        {
            if(left[i] < right[j])
            {
                datas[k] = left[i];
                i++;
            }
            else
            {
                datas[k] = right[j];
                j++;
            }
        }
        else
         break;
    }
    while(i != n1)
        datas[k++] = left[i++];
    while(j != n2)
        datas[k++] = right[j++];
    free(left);
    free(right);
}
//归并排序
void merge_sort(int *datas,int beg,int end)
{
    int pos;
    if(beg < end)
    {
        pos = (beg+end)/2;
        merge_sort(datas,beg,pos);
        merge_sort(datas,pos+1,end);
        merge(datas,beg,pos,end);
    }
}

int main(int argc,char *argv[])
{
    int i,j,x,obj;
    int datas[10] = {34,11,23,24,90,43,78,65,90,86};
    if(argc != 2)
    {
        printf("input error.\n");
        exit(0);
    }
    x = atoi(argv[1]);
    merge_sort(datas,0,9);
    for(i=0;i<10;i++)
    {
        obj = x - datas[i];
        j = binary_search_recursive(datas,0,10,obj);
        //j = binary_search(datas,10,obj);
        if( j != -1 && j!= i)  //判断是否查找成功
        {
             printf("there exit two datas (%d and %d) which their sum is %d.\n",datas[i],datas[j],x);
             break;
        }
    }
    if(i==10)
        printf("there not exit two datas whose sum is %d.\n",x);
    exit(0);
}
