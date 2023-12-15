let employees =[
    {name: "reza", task:[]},
    {name: "amir", task:[]},
    {name: "mahsa", task:[]},
    {name: "ahmad", task:[]},
]
let choiceEmployee
while(true){
    let choice = prompt("1-add task\n2-remove task\n3-exit")
    if(choice == 1){
        let employeeName = prompt("enter employee name : ")
        let taskName = prompt("enter task name : ")
        let employeeResault = employees.some(function(i){
            choiceEmployee = i
            return i.name == employeeName
        })
        if(employeeResault){
            choiceEmployee.task.push(taskName)
        }else{alert("employee not found...!")}
        
    }else if(choice == 2){
        let employeeName = prompt("enter employee name : ")
        let taskName = prompt("enter task name : ")
        let employeeResault = employees.some(function(i){
            choiceEmployee = i
            return i.name == employeeName
        })
        if(employeeResault){
            let taskIndex = choiceEmployee.task.findIndex(function(i){
                return i == taskName
        })
            choiceEmployee.task.splice(taskIndex, 1)
        }else{alert("employee not found...!")}
    }else if(choice == 3){
        for(i of employees){
            console.log(i)
        }
        console.log("---------------------------")
        break
    }else{alert("please choice from options!")}
    for(i of employees){
        console.log(i)
    }
    console.log("---------------------------")

    
    
}