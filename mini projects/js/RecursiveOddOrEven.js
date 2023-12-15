function oddoreven() {   
    let number = prompt("enter your number :");
    if (number == 0){
        alert(`${number} is not odd or even`)
    } else if (number % 2){
        alert(`${number} is odd`)
    } else {
        alert(`${number} is even`)
    }
     oddoreven()
}
oddoreven()