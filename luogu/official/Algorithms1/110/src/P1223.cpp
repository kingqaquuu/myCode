/*
 * @Author: kingqaquuu
 * @Date: 2023/12/4 20:38
 * @FileName: P1223.cpp
 */

#include <bits/stdc++.h>
using namespace std;
struct water{
    int tag;
    int t;
}a[1010];
bool cmp(water x,water y){
    return x.t<y.t;
}
int n;
int main() {
    double ans,time;
    cin>>n;
    for (int i = 1; i <= n; ++i) {
        scanf("%d",&a[i].t);
        a[i].tag=i;
    }
    sort(a+1,a+1+n,cmp);
    for (int i = 1; i <= n; ++i) {
        printf("%d ",a[i].tag);
        time+=a[i].t*(n-i);
    }
    ans=time/n;
    printf("\n%.2lf",ans);
    return 0;
}