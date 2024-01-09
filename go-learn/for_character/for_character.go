/*
 * @Author: kingqaquuu
 * @Date: 2024-01-05 19:14:04
 * @FilePath: \myCode\go-learn\for_character\for_character.go
 */
package main

import "fmt"

func main() {
	for i := 1; i <= 25; i++ {
		for j := 1; j <= i; j++ {
			fmt.Printf("G")
		}
		fmt.Println()
	}
}
