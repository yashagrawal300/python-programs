#include<cstdio>
#include<cstring>
int main() {
char c;
char s[1001];
int f[1001];
int p,sLength;
int cCounter=0;
int z=0;
int lastIndex=-1;

scanf("%s\n",s);
scanf("%c",&c);
scanf("%d",&p);

sLength=strlen(s);

for(int i=0; i<sLength; i++) {
if (i < p) {
if (s[i]==c) {
cCounter++;
}
}else {
if (s[i-p] == c) {
cCounter--;
}
if (s[i] == c) {
cCounter++;
}
}

if (cCounter>=z) {
z=cCounter;
}
f[i]=cCounter;
}

if(z<p) { 
for(int i=sLength-1; i>1; i--) {
if(f[i]==z && f[i-1]==z) {
lastIndex=i;
if(lastIndex==sLength-1){
lastIndex++;
}
break;
}
}
}
printf("%d\n",lastIndex);
return 0;
}
