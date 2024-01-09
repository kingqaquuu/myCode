/*
 * @Author: kingqaquuu
 * @Date: 2024-01-06 21:22:26
 * @FilePath: \myCode\go-learn\factorial\factorial.go
 */
package main

import (
	"fmt"
)

func main() {
	for i := uint(1); i < 30; i++ {
		fmt.Println("Factorial of", i, "is", factorial(i))
	}
}
func factorial(n uint) (result uint) {
	if n == 1 {
		result = 1
	} else {
		result = n * factorial(n-1)
	}
	return
}
