package main

import "fmt"

func main() {
	var fibonacciArray [51]int
	fibonacciArray[1] = 1
	fibonacciArray[2] = 1
	for i := 3; i <= 50; i++ {
		fibonacciArray[i] = fibonacciArray[i-1] + fibonacciArray[i-2]
	}
	for i := 1; i <= 50; i++ {
		fmt.Println(fibonacciArray[i])
	}

}
