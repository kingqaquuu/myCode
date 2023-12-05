/*
 * @Author: kingqaquuu
 * @Date: 2023/12/5 0:54
 * @FileName: P3817.cpp
 */

#include <bits/stdc++.h>
using namespace std;
long long x,n,a[100010],sum;
int main() {
    cin>>n>>x;
    for (int i = 1; i <= n; ++i) {
        scanf("%d",&a[i]);
        if(a[i]+a[i-1]>x){
            sum+=a[i]+a[i-1]-x;
            a[i]=x-a[i-1];
        }
    }
    printf("%lld",sum);

    return 0;
}