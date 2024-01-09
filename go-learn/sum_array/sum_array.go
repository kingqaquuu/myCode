/*
 * @Author: kingqaquuu
 * @Date: 2024-01-07 22:44:21
 * @FilePath: \myCode\go-learn\sum_array\sum_array.go
 */
package main

import "fmt"

func main() {
	var a = []float32{1.0, 2.0, 3.0, 4.0}
	fmt.Printf("The sum of the array is: %f\n", Sum(a))
	var b = []int{1, 2, 3, 4, 5}
	sum, average := SumAndAverage(b)
	fmt.Printf("The sum of the array is: %d, and the average is: %f", sum, average)
}

func Sum(arrF []float32) (sum float32) {
	sum = 0
	for _, v := range arrF {
		sum += v
	}
	return
}
func SumAndAverage(a []int) (int, float32) {
	sum := 0
	for _, v := range a {
		sum += v
	}
	average := sum / len(a)
	return sum, float32(average)
}
