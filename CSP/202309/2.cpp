/*
 * @Author: kingqaquuu
 * @Date: 2023/12/6 13:06
 * @FileName: 2.cpp
 */

#include <bits/stdc++.h>

using namespace std;
int main()
{
    int n, m;
    scanf("%d %d", &n, &m);
    double stretchPrefix[100010] = {1}, rotatePrefix[100010] = {0}; //拉伸操作的前缀积，旋转操作的前缀和
    for (int ni = 0; ni < n; ++ni) {
        int type;
        double val;
        scanf("%d %lf", &type, &val);
        switch (type) {
            case 1:
                stretchPrefix[ni + 1] = val * stretchPrefix[ni];
                rotatePrefix[ni + 1] = rotatePrefix[ni];
                break;
            case 2:
                stretchPrefix[ni + 1] = stretchPrefix[ni];
                rotatePrefix[ni + 1] = val + rotatePrefix[ni];
                break;
            default:
                break;
        }
    }
    for (int mi = 0; mi < m; ++mi) {
        int i, j;
        double x, y;
        scanf("%d %d %lf %lf", &i, &j, &x, &y);
        double k = stretchPrefix[j] / stretchPrefix[i - 1]; //求经过了i~j步的操作后的拉伸系数
        double theta = rotatePrefix[j] - rotatePrefix[i - 1]; //求经过了i~j步操作后的旋转角度
        double x1 = k * x;
        double y1 = k * y;
        double x2 = x1 * cos(theta) - y1 * sin(theta);
        double y2 = x1 * sin(theta) + y1 * cos(theta);
        printf("%lf %lf\n", x2, y2);
    }
    return 0;
}