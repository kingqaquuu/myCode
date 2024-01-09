/*
 * @Author: kingqaquuu
 * @Date: 2024-01-06 00:31:59
 * @FilePath: \myCode\go-learn\error_returnval\error_returnval.go
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
func MySqrt(a float64) (float64, error) {
	if a < 0 {
		return 0, errors.New("负数没有平方根")
	} else {
		return math.Sqrt(a), nil
	}
}
