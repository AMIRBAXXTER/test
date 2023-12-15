let firstNumber = +prompt("enter first number : ")
let secondNumber = +prompt("enter second number : ")
while (true) {
    if (firstNumber < secondNumber) {
        if (firstNumber % 2) {
            firstNumber -= 1
            console.log(firstNumber +=2)
        } else {
            console.log(firstNumber +=2)
        }
    } else if (secondNumber < firstNumber){
        if (secondNumber % 2) {
            secondNumber -= 1
            console.log(secondNumber +=2)
        } else {
            console.log(secondNumber +=2)
        }
    } else {break}
}