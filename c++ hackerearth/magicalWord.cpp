#include<iostream>
using namespace std;
char s[500];
int T,n,i;
int main()
{
    cin>>T;
    while(T--)
    {
        cin>>n;
        for(i=0;i<n;i++)
        {
            cin>>s[i];
            if(s[i]<70) s[i]='C';
            else if(s[i]>=70&&s[i]<73) s[i]='G';
            else if(s[i]>=73&&s[i]<77) s[i]='I';
            else if(s[i]>=77&&s[i]<82) s[i]='O';
            else if(s[i]>=82&&s[i]<87) s[i]='S';
            else if(s[i]>=87&&s[i]<94) s[i]='Y';
            
            else if(s[i]>=94&&s[i]<100) s[i]='a';
            else if(s[i]>=100&&s[i]<103) s[i]='e';
            else if(s[i]>=103&&s[i]<106) s[i]='g';
            else if(s[i]>=106&&s[i]<109) s[i]='k';
            else if(s[i]>=109&&s[i]<112) s[i]='m';
            else if(s[i]>=112) s[i]='q';
            
            cout<<s[i];
        }
        cout<<endl;
    }
    
    return 0;
}
