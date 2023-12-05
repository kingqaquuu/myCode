/*
 * @Author: kingqaquuu
 * @Date: 2023/12/6 0:10
 * @FileName: P1478.cpp
 */

#include <bits/stdc++.h>
using namespace std;
int n,s,a,b,ans;
struct node{
    int x;
    int y;
}apple[5005];
bool cmp(node c,node d){
    return c.y<d.y;
}
int main() {
    scanf("%d%d%d%d",&n,&s,&a,&b);
    for (int i = 0; i < n; ++i) {
        scanf("%d%d",&apple[i].x,&apple[i].y);
    }
    sort(apple,apple+n,cmp);
    for (int i = 0; i < n&&s>=0; ++i) {
        if(apple[i].y<=s&&apple[i].x<=a+b){
            ans++;
            s-=apple[i].y;
        }
    }
    cout<<ans;
    return 0;
}