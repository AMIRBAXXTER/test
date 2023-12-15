let id = 1
let sum = 0
let onlineShop = [
    {id: 1,name: "product 1", price: 2500},
    {id: 2,name: "product 2", price: 5000},
    {id: 3,name: "product 3", price: 7500},
]
let userBasket = []
let requestProduct;
while (true) {
    userChoice = prompt("enter your choice `buy` or `delete` : (or exit)")
    
    if (userChoice.toLowerCase() == "exit") {break
    } else if (userChoice.toLowerCase() == "buy") {
        userChoice = prompt("enter product name : ")
        let resualt = onlineShop.some(function(i) {             
            requestProduct = i
            return i["name"] === userChoice
        })
    
        if (resualt) {
            let newProduct = {
                id: id,
                name: requestProduct.name,
                price: requestProduct.price
            }
            userBasket.push(newProduct)
            id++
        } else {
            alert("we dont have this product")
        }
} else if (userChoice.toLowerCase() == "delete"){
    userChoice = prompt("enter product name : ")
    let resualt = onlineShop.findIndex(function(i) {             
        requestProduct = i
        return i["name"] === userChoice
    })
    userBasket.splice(resualt, 1)
}
userBasket.forEach(function (product) {
    sum = sum + product.price
})
}
console.log(userBasket)
console.log("total price " + sum)