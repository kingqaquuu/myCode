/*
 * @Author: kingqaquuu
 * @Date: 2023/12/8 14:38
 * @FileName: 1.cpp
 */

#include <bits/stdc++.h>
using namespace std;
int n,a,b,ans;
int main() {
    cin>>n>>a>>b;
    int x1,y1,x2,y2;
    int x,y;
    for (int i = 0; i < n; ++i) {
        scanf("%d%d%d%d",&x1,&y1,&x2,&y2);
        x=min(a,x2)-max(0,x1);
        y= min(b,y2)-max(0,y1);
        if (x>=0&&y>=0){
        ans+=x*y;
        }
    }
    cout<<ans;
    return 0;
}