/*
 * @Author: kingqaquuu
 * @Date: 2023/12/4 20:12
 * @FileName: P2240.cpp
 */

#include <bits/stdc++.h>
using namespace std;
struct coin{
    int m;
    int v;
}Coins[101];
int n,t;
bool cmp(coin a,coin b){
    return a.v*b.m>a.m*b.v;
}
int main() {
    double ans;
    scanf("%d%d",&n,&t);
    for (int i = 0; i < n; ++i) {
        scanf("%d%d",&Coins[i].m,&Coins[i].v);
    }
    sort(Coins,Coins+n,cmp);
    for (int i = 0; i < n; ++i) {
        if(Coins[i].m<=t){
            ans+=Coins[i].v;
            t-=Coins[i].m;
        }else{
            ans+=Coins[i].v*t*1.0/(Coins[i].m*1.0);
            break;
        }
    }
    printf("%.2lf",ans);
    return 0;
}