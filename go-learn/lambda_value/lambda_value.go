package main

import "fmt"

func main() {
	fv := func() {
		fmt.Println("Hello, World!")
	}
	fv()
	fmt.Printf("fv的类型是%T", fv)
}
