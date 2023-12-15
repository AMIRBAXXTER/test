let letter = (prompt("enter a word : "))
let newLetter = letter.split("").reverse().join("")
if (letter == newLetter){
    console.log(`${letter} = ${newLetter}`)
} else {
    console.log(`${letter} != ${newLetter}`)
}