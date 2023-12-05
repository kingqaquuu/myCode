/*
 * @Author: kingqaquuu
 * @Date: 2023/12/6 0:43
 * @FileName: P5019.cpp
 */

#include <bits/stdc++.h>

using namespace std;
int n,x[100010],ans;
int main() {
    scanf("%d",&n);
    for (int i = 0; i < n; ++i) {
        scanf("%d",&x[i]);
    }
    for (int i = 1; i < n; ++i) {
        if (x[i]>x[i-1]){
            ans+=x[i]-x[i-1];
        }
    }
    cout<<ans+x[0];
    return 0;
}