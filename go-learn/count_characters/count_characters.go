/*
 * @Author: kingqaquuu
 * @Date: 2024-01-05 02:34:40
 * @FilePath: \myCode\go-learn\count_characters\count_characters.go
 */
package main

import (
	"fmt"
	"unicode/utf8"
)

func main() {
	a := "asSASA ddd dsjkdsjs dk"
	b := "asSASA ddd dsjkdsjsこん dk"
	fmt.Printf("字符串a的长度是%d\n", len(a))
	fmt.Printf("字符串a的字符有%d\n", utf8.RuneCountInString(a))
	fmt.Printf("字符串b的长度是%d\n", len(b))
	fmt.Printf("字符串b的字符有%d\n", utf8.RuneCountInString(b))

}
