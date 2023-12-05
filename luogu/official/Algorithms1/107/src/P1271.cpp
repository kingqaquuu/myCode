/*
 * @Author: kingqaquuu
 * @Date: 2023-12-04 18:28:54
 * @FilePath: \luogu_code\official\Algorithms1\107\P1271.cpp
 */
#include <bits/stdc++.h>

using namespace std;
int n, temp;
long m;
int a[2000010];

int main() {
    cin >> n >> m;
    for (int i = 0; i < m; ++i) {
        scanf("%d", &a[i]);
    }
    sort(a, a + m);
    for (int i = 0; i < m; ++i) {
        printf("%d ", a[i]);
    }
    return 0;
}
