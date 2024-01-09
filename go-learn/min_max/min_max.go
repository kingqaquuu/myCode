/*
 * @Author: kingqaquuu
 * @Date: 2024-01-07 22:50:50
 * @FilePath: \myCode\go-learn\min_max\min_max.go
 */
package main

import "fmt"

func main() {
	s1 := []int{78, 34, 643, 12, 90, 492, 13, 2}
	min := minSlice(s1)
	max := maxSlice(s1)
	fmt.Printf("The maximum is %d\n", max)
	fmt.Printf("The minimum is %d\n", min)
}
func minSlice(nums []int) (min int) {
	min = nums[0]
	for _, v := range nums {
		if v <= min {
			min = v
		}
	}
	return
}
func maxSlice(nums []int) (max int) {
	max = nums[0]
	for _, v := range nums {
		if v >= max {
			max = v
		}
	}
	return
}
