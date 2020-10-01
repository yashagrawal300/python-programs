#include<iostream>
#include<string>
using namespace std;
int main()
{
    string s;
    string::iterator i;
    int k,l,m;
    cin>>s>>k;
    l=k%26;
    m=k%10;
    for(i=s.begin();i!=s.end();i++)
    {
        if(((int)*i>31 && (int)*i<48) ||((int)*i>57 && (int)*i<65) || ((int)*i>90 && (int)*i<97))
        continue;
        
        else if((int)*i>=97 && (int)*i+l>122)
        *i+=l-26;
       
        else if((int)*i>=65 && (int)*i+l>90 && !((int)*i>=97))
        *i+=l-26;
        
        else if((int)*i>=48 && (int)*i+m>57 && !((int)*i>=65))
        *i+=m-10;
    
        else if((int)*i>=48 && (int)*i<65) *i+=m;
        
        else *i+=l;
    }
    cout<<s;
}
