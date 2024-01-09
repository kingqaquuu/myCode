package main

import "fmt"

func main() {
	recursive(10)
}
func recursive(n int) {
	if n == 1 {
		fmt.Println(1)
	} else {
		fmt.Println(n)
		recursive(n - 1)
	}
}
