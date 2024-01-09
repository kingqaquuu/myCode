/*
 * @Author: kingqaquuu
 * @Date: 2024-01-06 00:33:01
 * @FilePath: \myCode\go-learn\error_returnval1\error_returnval.go
 */
package main

import (
	"errors"
	"fmt"
	"math"
)

func main() {
	var a float64
	fmt.Scanf("%f", &a)
	result, err := MySqrt(a)
	if err != nil {
		fmt.Println(err)
	} else {
		fmt.Println(result)
	}
}
func MySqrt(a float64) (result float64, err error) {
	if a < 0 {
		result = 0
		err = errors.New("负数没有平方根")
	} else {
		result = math.Sqrt(a)
		err = nil
	}
	return
}
