/*
 * @Author: kingqaquuu
 * @Date: 2024-01-05 19:06:04
 * @FilePath: \myCode\go-learn\for_loop_gotoversion\for_loop_gotoversion.go
 */
package main

import "fmt"

func main() {
	i := 0
end:
	i++
	fmt.Println(i)
	if i <= 14 {
		goto end
	}
}
