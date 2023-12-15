let toDoList = []
let setId = 1
while (true) {
    let userChoice = prompt("todo list menu \n1-add\n2-remove\n3-done\n4-exit")
    if (userChoice.toLowerCase() == 1){
        let toDoName = prompt("enter todo name for add : ")
        let newToDo = {
            id: setId,
            title: toDoName,
            state: false
        }
        toDoList.push(newToDo)
        setId++
    }else if (userChoice.toLowerCase() == 2) {
        let toDoName = prompt("enter todo name for remove : ")
        let resualt = toDoList.some(function(i) {             
            return i.title == toDoName
    })
        if (resualt) {
            toDoIndex = toDoList.findIndex(function(i){
                return i.title == toDoName
            })
            toDoList.splice(toDoIndex, 1)
        } else {console.log("this todo not exist.!")}
    } else if (userChoice.toLowerCase() == 3) {
        let toDoName = prompt("enter todo name for change to done : ")
        let userToDo
        let resualt = toDoList.some(function(i) {             
            userToDo = i
            return i.title == toDoName
    })
        if (resualt) {
            userToDo.state = true
        } else {console.log("this todo not exist.!")}
    } else if (userChoice.toLowerCase() == 4) {
        for (i of toDoList) {
            console.log(i)
        }
            console.log("---------------------------")
        break
    } else {
        alert("please choice between options")
    }
    for (i of toDoList) {
        console.log(i)
    }
        console.log("---------------------------")
}