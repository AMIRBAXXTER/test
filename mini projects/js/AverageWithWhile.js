let totallNumber = 0
let counter = 0
while (true) {
    let userNumber = prompt("enter a number : ('exit' for calculate average)")
    if (userNumber == "exit") {
        alert("average is : " + totallNumber / counter)
        break
    } else {
        totallNumber += +userNumber
        counter++
    }
}