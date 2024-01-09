/*
 * @Author: kingqaquuu
 * @Date: 2024-01-06 00:23:10
 * @FilePath: \myCode\go-learn\mult_returnval\mult_returnval.go
 */
package main

import "fmt"

func main() {
	var a, b int
	fmt.Scanf("%d%d", &a, &b)
	numx1, numx2, numx3 := mulAndAddAndSub(a, b)
	fmt.Printf("%d与%d加法,乘法,减法结果分别为%d,%d,%d\n", a, b, numx1, numx2, numx3)

}
func mulAndAddAndSub(a, b int) (x1, x2, x3 int) {
	x1 = a + b
	x2 = a * b
	x3 = a - b
	return
}
