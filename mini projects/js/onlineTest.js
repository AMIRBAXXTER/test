let score = 0
let questions =[
    {id: 1, question:"5+9", rightAnswer: 1, answers:`1-14\n2-16\n3-18\n4-17`},
    {id: 2, question:"6*5", rightAnswer: 3, answers:`1-32\n2-31\n3-30\n4-28`},
    {id: 3, question:"12/3", rightAnswer: 2, answers:`1-5\n2-4\n3-2\n4-5`},
    {id: 4, question:"25*4", rightAnswer: 4, answers:`1-105\n2-108\n3-125\n4-100`},
]
questions.forEach(function(i){
    answer = +prompt(`question${i["id"]}: ${i.question}\n${i.answers}`)
    if(answer === i.rightAnswer){
        alert("your answer was right.weldone")
        score++
    }else{
        alert("your answer was wrong!")   
    }
})
console.log("total score " + score)