let userNumber = +prompt("enter your number : ")
sum = 0
for (;;) {
    let oneNumber = userNumber % 10
    sum += oneNumber
    userNumber = Math.floor(userNumber / 10)
    if (!(userNumber)) {break}
}
alert(sum)