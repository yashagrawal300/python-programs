#include <stdio.h>
#include <stdlib.h>
int main()
{
    int num, month, value, i, j, count=0, sum=0;
    int * ptr;
    scanf("%d", &num);
    ptr = (int *) malloc (num*sizeof(int));
    if(ptr == NULL)
    {
        printf("Sorry!");
    }
    for(i=0;i<num;i++)
    {
        scanf("%d", (ptr+i));
    }
    scanf("%d", &month);
    scanf("%d", &value);
    i=0;
    while(i<num)
    {
        for(j=i;j<value+i;j++)
        {
            sum+=(*(ptr+j));
        }
        if(sum == month)
        {
            count++;
        }
        i++;
        sum=0;
    }
    printf("%d", count);
    free(ptr);
    return 0;
}