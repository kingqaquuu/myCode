/*
 * @Author: kingqaquuu
 * @Date: 2023/12/4 23:56
 * @FileName: P1803.cpp
 */

#include <bits/stdc++.h>
using namespace std;
int n;
struct node{
    int startTime;
    int endTime;
}com[1000010];
bool cmp(node a,node b){
    return a.endTime<b.endTime;
}
int main() {
    scanf("%d",&n);
    for (int i = 0; i < n; ++i) {
        scanf("%d%d",&com[i].startTime,&com[i].endTime);
    }
    sort(com,com+n,cmp);
    int end1,ans=1;
    end1=com[0].endTime;
    for (int i = 1; i < n; ++i) {
        if(com[i].startTime>=end1){
            end1=com[i].endTime;
            ans++;
        }
    }
    printf("%d",ans);
    return 0;
}