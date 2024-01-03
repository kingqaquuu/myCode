/*
 * @Author: kingqaquuu
 * @Date: 2023-12-04 18:16:18
 * @FilePath: \luogu_code\official\Getting Started\100\src\P5708.cpp
 */
#include <bits/stdc++.h>

using namespace std;

int main() {
    double a, b, c;
    cin >> a >> b >> c;
    double p, ans;
    p = (a + b + c) / 2;
    ans = sqrt(p * (p - a) * (p - b) * (p - c));
    printf("%.1lf", ans);
    return 0;
}
