let numbersArray = []
let totalNumber = 0
while (true) {
    userNumber = prompt("enter your number : (or exit)")
    if (userNumber === "exit") {break} else {
        numbersArray.push(+userNumber)
    }
}
for (i of numbersArray) {
    totalNumber += i
}
document.getElementById("demo1").innerHTML = `average is : ${totalNumber / numbersArray.length}`