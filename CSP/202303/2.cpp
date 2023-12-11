/*
 * @Author: kingqaquuu
 * @Date: 2023/12/8 15:01
 * @FileName: 2.cpp
 */

#include <bits/stdc++.h>
using namespace std;
int n, k;
long long int m;
map<int, int>tim, res, flag;

int main(){
    cin >> n >> m >> k;
    int max=0;
    for (int i = 0; i < n; ++i) {
        scanf("%d%d",&tim[i],&res[i]);
        max = max > tim[i] ? max : tim[i];
        flag[tim[i]] += res[i];
    }
    for(int i = max; i > 0; i--){
        if(max == k)break;
        if(m > flag[i]){
            m = m - flag[i];
            flag[i - 1] += flag[i];
            max--;
        }else break;
    }
    cout << max;

    return 0;
}