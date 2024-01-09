/*
 * @Author: kingqaquuu
 * @Date: 2024-01-05 19:22:57
 * @FilePath: \myCode\go-learn\bitwise_complement\bitwise_complement.go
 */
package main

import "fmt"

func main() {
	for i := 1; i <= 10; i++ {
		fmt.Printf("%b的补码是%b\n", i, ^i)
	}
}
