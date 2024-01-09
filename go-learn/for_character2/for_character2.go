package main

import "fmt"

func main() {
	s := "GGGGGGGGGGGGGGGGGGGGGGGGG"
	for i := 0; i < 25; i++ {
		fmt.Println(s[:i])
	}
}
