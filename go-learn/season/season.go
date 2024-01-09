/*
 * @Author: kingqaquuu
 * @Date: 2024-01-05 18:14:47
 * @FilePath: \myCode\go-learn\season\season.go
 */
package main

import (
	"fmt"
)

func Season(month int) string {
	switch month {
	case 3, 4, 5:
		return "春季"
	case 6, 7, 8:
		return "夏季"
	case 9, 10, 11:
		return "秋季"
	case 12, 1, 2:
		return "冬季"
	default:
		return "输入错误"
	}
}
func main() {
	var month int
	fmt.Scanf("%d", &month)
	fmt.Println(Season(month))
}
