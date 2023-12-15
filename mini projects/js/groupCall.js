let groupMembrs = [
    {username: "ahmad", age: 24},
    {username: "reza", age: 25},
    {username: "amir", age: 23},
    {username: "mohammad", age: 26},
    {username: "mahsa", age: 20},
]
while (true) {
    adminChoice = prompt("type `call` for call or `exit` : ")
    if (adminChoice == "call") {
        if (groupMembrs.every(function(i) {
            return i.age > 18
        })) {alert("call sucessfully start")
        break
    } else {alert("all members must older than 18")
    break}
    } else {alert("exiting...")
            break}
}