function letRndomColor() {
    const letters = "0123456789abcdef"
    let color = "#"
    for (let i = 0; i < 6 ; i++){
        color += letters[Math.floor(Math.random() * 16)]
    }
    return color
}
function changeBGC() {
    document.body.style.backgroundColor = letRndomColor()
    document.getElementById("text").style.color = letRndomColor()
}
setInterval(changeBGC, 500)