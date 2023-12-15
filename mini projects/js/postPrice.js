let totalPrice = 0
let userBasket = [
    {id: 1, name: "product 1", price: 150000},
    {id: 2, name: "product 2", price: 150000},
    {id: 3, name: "product 3", price: 50000},
    {id: 4, name: "product 4", price: 50000},
    {id: 5, name: "product 5", price: 50000},
    {id: 6, name: "product 6", price: 50000},
]
let under100 = userBasket.filter(function(i){
    return i.price < 100000
})
for (i of userBasket) {
    totalPrice += i.price
}
for (i of under100) {
    totalPrice += 1000
}
console.log(`total price = ${totalPrice}`)