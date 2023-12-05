/*
 * @Author: kingqaquuu
 * @Date: 2023/12/4 19:43
 * @FileName: P1923.cpp
 */

#include <bits/stdc++.h>

using namespace std;
int n,m,a[5000005];

int main() {
    cin>>n>>m;
    for (int i = 0; i < n; ++i) {
        scanf("%d",&a[i]);
    }
    sort(a,a+n);
    cout<<a[m];
    return 0;
}