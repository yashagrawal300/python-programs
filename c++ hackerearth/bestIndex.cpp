#include<iostream>
#include<cmath>
using namespace std;
long arr[100000],sum[100000];
using namespace std;
int main()
{
    long int n,x,max;
    cin>>n;
    for(int i=0;i<n;i++)
    {
        cin>>arr[i];
        if(i==0) sum[i]=arr[i];
        else sum[i]=arr[i]+sum[i-1];

    }
    for(int i=0;i<n;i++)
    {
        x=sqrt(2*(n-i));
        if(x*(x+1)>2*(n-i)) x=x-1;

        x=(x*(x+1))/2;
        if(i==0)
        {
            max=sum[x-1];
        }
        else if(max<sum[i+x-1]-sum[i-1]){ max=sum[i+x-1]-sum[i-1];}

    }
    cout<<max;
}
