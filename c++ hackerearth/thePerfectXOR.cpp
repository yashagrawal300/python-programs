#include<bits/stdc++.h>
#define ll long long int
using namespace std;
vector<int>adj[300002];
ll visited[300002],w[300002],aw[300002],dis[300002],low[300002];
ll tim=0,ans=-1,sum=0;
void dfs(ll u,ll p)
{
    visited[u]=true;
    dis[u]=low[u]=++tim;
    aw[u]=w[u];
    ll x=0,flag=0,sw=0,child=0;
    for(auto it:adj[u])
    {
        if(!visited[it])
        {
            child++;
            dfs(it,u);
            aw[u]+=aw[it];
            low[u]=min(low[u],low[it]);
            if(low[it]>=dis[u])
            {
                x^=aw[it];
                sw+=aw[it];
                flag=1;
            }
        }
        else if(it!=p)
            low[u]=min(low[u],dis[it]);
    }
    if((p && flag) || (!p && child>1))
    {
        sw=sum-w[u]-sw;
        x^=sw;
        ans=max(ans,x);
    }
}
int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(0);
    cout.tie(0);
    ll n,m,u,v;
    cin>>n>>m;
    for(ll i=1;i<=n;i++)
        cin>>w[i],sum+=w[i];
    while(m--)
    {
        cin>>u>>v;
        adj[u].push_back(v),adj[v].push_back(u);
    }
    dfs(1,0);
    cout<<ans;
}
