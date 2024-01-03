/*
 * @Author: kingqaquuu
 * @Date: 2023/12/8 16:45
 * @FileName: P1216.cpp
 */

#include <bits/stdc++.h>
#include "unistd.h"
using namespace std;
int main()

{

  char Buf[1024];
  short a = (short)0xFFFF;
  int b;
  b = a;
  printf("b=%d    \r\n",b);
  b = (a & 0xFFFF);
  printf("b=%d    \r\n",b);
  return 1;

}