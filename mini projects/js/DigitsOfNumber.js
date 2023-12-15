let userNumber = +prompt("enter your number : ")
let totalNumber = 0
for (;;) {
    userNumber = Math.floor(userNumber / 10)
    totalNumber += 1
    if (!(userNumber)) {break}
}
alert(`your number has ${totalNumber} digits`)