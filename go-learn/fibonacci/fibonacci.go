/*
 * @Author: kingqaquuu
 * @Date: 2024-01-06 20:54:21
 * @FilePath: \myCode\go-learn\fibonacci\fibonacci.go
 */
package main

import "fmt"

func main() {
	var n, result, postion int
	fmt.Scanln(&n)
	for i := 0; i < n; i++ {
		postion, result = fibonacci(i)
		fmt.Printf("位置%d的斐波那契数是%d\n", postion, result)
	}
}
func fibonacci(n int) (postion, result int) {
	if n == 0 {
		result = 1
	} else if n == 1 {
		result = 1
	} else {
		_, v1 := fibonacci(n - 1)
		_, v2 := fibonacci(n - 2)
		result = v1 + v2
	}
	postion = n + 1
	return
}
