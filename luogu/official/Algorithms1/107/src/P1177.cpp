/*
 * @Author: kingqaquuu
 * @Date: 2023/12/4 19:16
 * @FileName: P1177.cpp
 */

#include <bits/stdc++.h>

using namespace std;
long n;
int a[1000002];
int main() {

    cin >> n;
    for (int i = 0; i < n; ++i) {
        cin >> a[i];
    }
    sort(a, a + n);
    for (int i = 0; i < n; ++i) {
        cout << a[i] << ' ';
    }
    return 0;
}