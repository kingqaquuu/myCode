package main

import "fmt"

func main() {
	var x int
	fmt.Scanln(&x)
	for i, value := range fobinacii(x) {
		fmt.Printf("fib(%d) = %d\n", i, value)
	}
}
func fobinacii(n int) (fib []int) {
	fib = make([]int, n)
	fib[0] = 1
	fib[1] = 1
	for i := 2; i < n; i++ {
		fib[i] = fib[i-1] + fib[i-2]
	}
	return
}
