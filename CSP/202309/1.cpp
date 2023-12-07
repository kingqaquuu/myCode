/*
 * @Author: kingqaquuu
 * @Date: 2023/12/6 1:46
 * @FileName: 1.cpp
 */

#include <bits/stdc++.h>

using namespace std;
int n,m;
int dx,dy,a;
int main() {
    scanf("%d%d",&n,&m);
    for (int i = 0; i < n; ++i) {
        scanf("%d",&a);
        dx+=a;
        scanf("%d",&a);
        dy+=a;
    }
    int x,y;
    for (int i = 0; i < m; ++i) {
        scanf("%d%d",&x,&y);
        printf("%d %d\n",x+dx,y+dy);
    }
    return 0;
}