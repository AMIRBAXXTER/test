let users = [
    {name: "amir", passWord: "Amir@13761376"},
    {name: "mahsa", passWord: "mahsa1234"},
    {name: "niloo", passWord: "niloo1379"},
    {name: "reza", passWord: "12345678"},
    {name: "hamid", passWord: "87654321"},
]
let requestUser = prompt("enter your username to show your password : ")
let findUser = users.find(function(i){
    return i.name == requestUser
})
if (findUser === undefined){
    alert("user not found !")
} else {
    alert(findUser.passWord)
}