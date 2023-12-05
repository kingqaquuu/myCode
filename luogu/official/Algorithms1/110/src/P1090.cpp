/*
 * @Author: kingqaquuu
 * @Date: 2023/12/5 0:31
 * @FileName: P1090.cpp
 */

#include <bits/stdc++.h>

using namespace std;
int n;
priority_queue<int,vector<int>,greater<>> q;
int main() {
    scanf("%d",&n);
    int a,b,ans=0;
    for (int i = 0; i < n; ++i) {
        scanf("%d",&a);
        q.push(a);
    }
    while (q.size()!=1){
        a=q.top();
        q.pop();
        b=q.top();
        q.pop();
        ans+=a+b;
        q.push(a+b);
    }
    printf("%d",ans);
    return 0;
}