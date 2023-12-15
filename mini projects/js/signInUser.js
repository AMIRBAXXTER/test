let users = [
    {id: 1,name:"amir", family:"pormahdi",age:25, email:"amir@gmail.com"},
    {id: 2,name:"mohammad", family:"amini",age:28, email:"mohammad@gmail.com"},
    {id: 3,name:"reza", family:"dolati",age:27, email:"reza@gmail.com"}
]
let newUser = {}
newUser["id"] = 4
while (true) {
    let newUserName = prompt("enter your name :")
    if (3 < newUserName.length && newUserName.length < 10) {newUser["name"]= newUserName
    break}
}
while (true) {
    let newUserFamily = prompt("enter your family :")
    if (3 < newUserFamily.length && newUserFamily.length < 15) {newUser["family"]= newUserFamily
    break}
}
while (true) {
    let newUserAge = +prompt("enter your age :")
    if (newUserAge < 1000) {newUser["age"]= newUserAge
    break}
}
let newUserEmail = prompt("enter your email :")
newUser["email"]= newUserEmail

users.push(newUser)
console.log(users)