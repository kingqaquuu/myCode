/*
 * @Author: kingqaquuu
 * @Date: 2024-01-06 20:36:30
 * @FilePath: \myCode\go-learn\varargs\varargs.go
 */
package main

import "fmt"

func main() {
	a := []int{1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
	fmt.Println(a)
	PrintVarar(a...)
}
func PrintVarar(a ...int) {
	for _, v := range a {
		fmt.Println(v)
	}
}
