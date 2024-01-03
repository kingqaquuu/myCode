/*
 * @Author: kingqaquuu
 * @Date: 2024-01-04 00:17:57
 * @FilePath: \myCode\go-learn\polymorphism\Polymorphism.go
 */
package main

import (
	"fmt"
	"strconv"
)

// 定义商品的接口Good
type Good interface {
	settleAccount() int
	orderInfo() string
}

// 定义手机的结构体Phone
type Phone struct {
	name     string
	quantity int
	price    int
}

// 定义赠品的结构体Gift
type Gift struct {
	name     string
	quantity int
	price    int
}

// 实现Phone的商品接口
func (p Phone) settleAccount() int {
	return p.quantity * p.price
}
func (p Phone) orderInfo() string {
	return "您要购买" + p.name + "的数量为" + strconv.Itoa(p.quantity) + "件，单价为" + strconv.Itoa(p.price) + "元"
}

// 实现Gift的商品接口
func (g Gift) settleAccount() int {
	return g.quantity * g.price
}
func (g Gift) orderInfo() string {
	return "您要购买" + g.name + "的数量为" + strconv.Itoa(g.quantity) + "件，单价为" + strconv.Itoa(g.price) + "元"
}

// 计算最终的总价并且 输出购物车里的物品
func calculateTotalPrice(goods []Good) int {
	totalPrice := 0
	for _, good := range goods {
		fmt.Println(good.orderInfo())
		totalPrice += good.settleAccount()
	}
	return totalPrice
}
func main() {
	iPhone := Phone{
		name:     "iphone",
		quantity: 1,
		price:    7000}
	airpods := Gift{
		name:     "airpods",
		quantity: 1,
		price:    0}
	goods := []Good{iPhone, airpods}
	totalprice := calculateTotalPrice(goods)
	fmt.Printf("该订单需要支付%d元", totalprice)

}
